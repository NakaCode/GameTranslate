import hashlib
import re
import unicodedata
from collections import OrderedDict
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List

from deep_translator import GoogleTranslator

from src.ocr import TextBlock

_NOISE_PATTERN = re.compile(r'^[\W\d_]+$')
_CONTROL_CHARS = re.compile(r'[\x00-\x1F\x7F]')

# ── Cache de traduções (LRU, por sessão) ──────────────────────────
_CACHE_MAX = 2048
_cache: OrderedDict[str, str] = OrderedDict()
_cache_hits = 0
_cache_misses = 0


def _cache_key(text: str, source: str, target: str) -> str:
    raw = f"{source}:{target}:{text}"
    return hashlib.md5(raw.encode("utf-8")).hexdigest()


def _cache_get(text: str, source: str, target: str) -> str | None:
    global _cache_hits
    key = _cache_key(text, source, target)
    if key in _cache:
        _cache.move_to_end(key)
        _cache_hits += 1
        return _cache[key]
    return None


def _cache_put(text: str, source: str, target: str, translated: str):
    global _cache_misses
    key = _cache_key(text, source, target)
    _cache[key] = translated
    _cache.move_to_end(key)
    _cache_misses += 1
    if len(_cache) > _CACHE_MAX:
        _cache.popitem(last=False)


def get_cache_stats() -> dict:
    total = _cache_hits + _cache_misses
    return {
        "hits": _cache_hits,
        "misses": _cache_misses,
        "ratio": f"{(_cache_hits / total * 100):.0f}%" if total else "0%",
        "size": len(_cache),
    }

# Presets de velocidade vs precisão
_MODES: dict = {
    "fast":     {"max_workers": 15, "min_letter_ratio": 0.6, "min_length": 3},
    "balanced": {"max_workers": 10, "min_letter_ratio": 0.4, "min_length": 2},
    "precise":  {"max_workers": 15, "min_letter_ratio": 0.25, "min_length": 1},
}


def _is_translatable(text: str, min_letter_ratio: float = 0.4, min_length: int = 2) -> bool:
    text = text.strip()
    if len(text) < min_length:
        return False
    letters = sum(1 for c in text if c.isalpha())
    if letters / len(text) < min_letter_ratio:
        return False
    if _NOISE_PATTERN.match(text):
        return False
    return True


def _sanitize(text: str) -> str:
    return _CONTROL_CHARS.sub("", text).strip()


def _looks_valid(translated: str) -> bool:
    """
    Usa unicodedata para validar o resultado.
    Aceita letras de qualquer idioma (incluindo acentos do português),
    números, pontuação e espaços. Rejeita símbolos e caracteres de controle.
    """
    if not translated or not translated.strip():
        return False

    weird = 0
    for c in translated:
        cat = unicodedata.category(c)
        # L=letra, N=número, P=pontuação, Z=espaço, M=acento/marca
        if not cat.startswith(("L", "N", "P", "Z", "M")):
            weird += 1

    return (weird / len(translated)) <= 0.15


def _apply_glossary(text: str, glossary: list) -> tuple[str, dict]:
    """
    Substitui termos do glossário por placeholders antes da tradução.
    Retorna o texto modificado e um mapa placeholder→tradução fixa.
    """
    placeholders = {}
    for i, entry in enumerate(glossary):
        orig = entry.get("original", "")
        if not orig:
            continue
        ph = f"__GL{i}__"
        if re.search(re.escape(orig), text, re.IGNORECASE):
            text = re.sub(re.escape(orig), ph, text, flags=re.IGNORECASE)
            placeholders[ph] = entry.get("translation", orig)
    return text, placeholders


def _restore_glossary(text: str, placeholders: dict) -> str:
    for ph, translation in placeholders.items():
        text = text.replace(ph, translation)
    return text


def _translate_one(
    block: TextBlock, source: str, target: str,
    min_letter_ratio: float, min_length: int,
    glossary: list | None = None,
) -> TextBlock:
    """Traduz um único bloco. Executado em paralelo."""
    if not _is_translatable(block.original, min_letter_ratio, min_length):
        block.translated = block.original
        return block

    clean = _sanitize(block.original)

    # Verifica cache antes de chamar a API
    cached = _cache_get(clean, source, target)
    if cached is not None:
        block.translated = cached
        return block

    placeholders = {}
    if glossary:
        clean, placeholders = _apply_glossary(clean, glossary)

    try:
        result = GoogleTranslator(source=source, target=target).translate(clean)
        if result and _looks_valid(result):
            result = result.strip()
            if placeholders:
                result = _restore_glossary(result, placeholders)
            block.translated = result
            _cache_put(_sanitize(block.original), source, target, result)
        else:
            block.translated = block.original
    except Exception:
        block.translated = block.original
    return block


def translate_blocks(
    blocks: List[TextBlock],
    source: str = "en",
    target: str = "pt",
    mode: str = "balanced",
    glossary: list | None = None,
) -> List[TextBlock]:
    if not blocks:
        return blocks

    preset = _MODES.get(mode, _MODES["balanced"])
    max_workers = preset["max_workers"]
    min_ratio = preset["min_letter_ratio"]
    min_len = preset["min_length"]

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(
                _translate_one, b, source, target, min_ratio, min_len, glossary,
            ): b
            for b in blocks
        }
        for future in as_completed(futures):
            future.result()

    return blocks
