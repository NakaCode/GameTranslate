"""
Verificador de atualizações do PolyQuest.
Consulta o Supabase para checar se há versão mais recente.
"""

import json
import urllib.error
import urllib.request

from src.license import SUPABASE_URL, SUPABASE_ANON_KEY

_CHECK_UPDATE_URL = f"{SUPABASE_URL}/functions/v1/check-update"

# Versão atual do app (manter sincronizado com about_dialog)
CURRENT_VERSION = "1.4.0"


def _parse_version(v: str) -> tuple:
    """Converte '1.2.0' em (1, 2, 0) para comparação."""
    try:
        return tuple(int(x) for x in v.strip().lstrip("v").split("."))
    except (ValueError, AttributeError):
        return (0, 0, 0)


def check_for_update() -> dict | None:
    """
    Verifica se há atualização disponível.

    Retorna dict com info da atualização ou None se estiver atualizado
    ou se não conseguir conectar.

    Retorno exemplo:
    {
        "version": "1.3.0",
        "message": "Nova versão com melhorias...",
        "url": "https://...",
    }
    """
    try:
        body = json.dumps({"version": CURRENT_VERSION}).encode()
        req = urllib.request.Request(
            _CHECK_UPDATE_URL,
            data=body,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {SUPABASE_ANON_KEY}",
                "apikey": SUPABASE_ANON_KEY,
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode())

        if not data.get("has_update"):
            return None

        return {
            "version": data.get("version", ""),
            "message": data.get("message", ""),
            "url": data.get("url", ""),
        }

    except Exception:
        # Sem internet ou erro — silencia, não bloqueia o app
        return None
