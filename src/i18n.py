"""
Internacionalização do PolyQuest.
Uso:  from src.i18n import t, setup
      setup("en")
      label = t("tray_action_quit")
      msg   = t("tray_msg_ready", hotkey="*")
"""

_lang = "pt"

# ---------------------------------------------------------------------------
# Strings por idioma
# ---------------------------------------------------------------------------
STRINGS: dict = {
    "pt": {
        # Tray
        "tray_tooltip_ready":       "PolyQuest — pronto",
        "tray_tooltip_translating": "PolyQuest — traduzindo...",
        "tray_tooltip_settings":    "PolyQuest — configurações",
        "tray_action_translate":    "Traduzir tela  [{hotkey}]",
        "tray_action_settings":     "Configurações...",
        "tray_action_about":        "Sobre...",
        "tray_action_quit":         "Encerrar",
        "tray_msg_ready":           "Pronto! Pressione {hotkey} para traduzir.",
        "tray_msg_no_text":         "Nenhum texto encontrado na tela.",
        "tray_msg_still_loading":   "Ainda carregando o OCR, aguarde...",
        "tray_msg_error":           "Erro ao traduzir. Verifique o console.",
        "tray_msg_settings_saved":  "Configurações salvas.",
        # Settings
        "settings_title":               "PolyQuest — Configurações",
        "settings_heading":             "Configurações",
        "settings_section_hotkey":      "TECLA DE ATALHO",
        "settings_hotkey_label":        "Tecla de atalho:",
        "settings_hotkey_change":       "Alterar",
        "settings_hotkey_hint":         "Clique em 'Alterar' e pressione a tecla desejada.",
        "settings_hotkey_waiting":      "Aguardando — pressione a tecla desejada...",
        "settings_hotkey_selected":     "Tecla '{key}' selecionada. Clique em Salvar para confirmar.",
        "settings_section_capture":     "CAPTURA",
        "settings_monitor_label":       "Monitor:",
        "settings_monitor_auto":        "Automático (janela ativa)",
        "settings_monitor_item":        "Monitor {i}  ({w}×{h})",
        "settings_resolution_label":    "Resolução manual:",
        "settings_section_languages":   "IDIOMAS",
        "settings_source_lang":         "Idioma de origem:",
        "settings_target_lang":         "Idioma de destino:",
        "settings_section_appearance":  "APARÊNCIA",
        "settings_theme_label":         "Tema do overlay:",
        "settings_font_size_label":     "Ajuste de fonte:",
        "settings_font_size_hint":      "0 pt = tamanho automático baseado no texto do jogo.",
        "settings_mode_label":          "Modo de tradução:",
        "settings_section_interface":   "INTERFACE",
        "settings_ui_language_label":   "Idioma da interface:",
        "settings_btn_cancel":          "Cancelar",
        "settings_btn_save":            "Salvar",
        # Modos de tradução
        "mode_fast":     "Velocidade  — capta menos texto, mais rápido",
        "mode_balanced": "Equilibrado — padrão recomendado",
        "mode_precise":  "Preciso     — capta mais texto, pode ser mais lento",
        # Temas
        "theme_dark":  "Escuro",
        "theme_light": "Claro",
        "theme_green": "Matrix",
        "theme_amber": "Âmbar",
        "theme_custom": "Personalizar",
        "custom_bg_color":    "Cor do fundo:",
        "custom_text_color":  "Cor do texto:",
        "custom_opacity":     "Opacidade do fundo:",
        "custom_preview":     "Prévia do overlay",
        # Perfis
        "profile_section":          "PERFIL DO JOGO",
        "profile_label":            "Perfil ativo:",
        "profile_new":              "Novo",
        "profile_delete":           "Excluir",
        "profile_new_title":        "Novo perfil",
        "profile_new_prompt":       "Nome do jogo:",
        "profile_delete_confirm":   "Excluir o perfil '{name}'?",
        "profile_default":          "Padrão",
        # Tray — Glossário
        "tray_action_glossary":     "Glossário...",
        # Glossary
        "glossary_title":           "PolyQuest — Glossário",
        "glossary_heading":         "Glossário",
        "glossary_add":             "Adicionar",
        "glossary_original":        "Original",
        "glossary_translation":     "Tradução fixa",
        "glossary_search":          "Buscar termos...",
        "glossary_remove":          "Remover",
        "glossary_count":           "{count} termo(s) cadastrado(s)",
        "glossary_btn_close":       "Fechar",
        # About
        "about_title":        "Sobre o PolyQuest",
        "about_version":      "Versão 1.4",
        "about_desc":         "Overlay de tradução em tempo real para jogadores.\nCaptura a tela, faz OCR e exibe as traduções diretamente sobre o jogo.",
        "about_developed_by": "Desenvolvido por",
        "about_authors":      "Lucas Silva  ·  Claude",
        "about_tech":         "PyQt6  ·  Windows OCR (WinRT)  ·  Google Translate  ·  PyInstaller",
        "about_btn_close":    "Fechar",
        # License
        "license_section":          "LICENÇA",
        "license_status_label":     "Status:",
        "license_status_beta":      "Gratuito",
        "license_status_premium":   "Premium ativado",
        "license_key_label":        "Chave de licença:",
        "license_key_placeholder":  "PQ-XXXX-XXXX-XXXX",
        "license_btn_activate":     "Ativar",
        "license_btn_deactivate":   "Desativar",
        "license_activating":       "Ativando...",
        "license_activated":        "Licença Premium ativada com sucesso!",
        "license_error":            "Falha na ativação: {error}",
        "license_deactivated":      "Licença removida. Reinicie o app.",
        "license_premium_badge":    "PREMIUM",
        "license_hint_beta":        "Recursos Premium bloqueados. Insira sua chave para desbloquear.",
        "license_premium_only":     "(Premium)",
        # Update
        "update_available_title":   "Atualização disponível",
        "update_available_msg":     "Nova versão {version} disponível!\n\n{message}",
        "update_btn_download":      "Baixar",
        "update_btn_later":         "Depois",
        # Overlay
        "overlay_hint": "  PolyQuest  |  Pressione {hotkey} para fechar  ",
        # OCR
        "ocr_missing_lang": (
            "O pacote de idioma '{tag}' não está instalado no Windows OCR.\n\n"
            "Para instalar:\n"
            "  Configurações → Hora e idioma → Idioma e região\n"
            "  → Adicionar idioma → selecione o idioma desejado\n"
            "  → Opções → Baixar 'Reconhecimento óptico de caracteres'\n\n"
            "Reinicie o PolyQuest após instalar."
        ),
        "ocr_unavailable": (
            "Windows OCR indisponível para '{tag}'. Execute o PolyQuest "
            "novamente para ver as instruções de instalação do pacote de idioma."
        ),
        "ocr_req_title": "PolyQuest — Requisito ausente",
        "ocr_install_prompt": (
            "O pacote de idioma OCR '{tag}' não está instalado.\n\n"
            "Deseja instalar automaticamente?\n"
            "(Será necessário permitir acesso de administrador)"
        ),
        "ocr_install_btn": "Instalar agora",
        "ocr_install_btn_quit": "Sair",
        "ocr_install_success": "Pacote OCR instalado com sucesso! O PolyQuest vai continuar.",
        "ocr_install_failed": "Não foi possível instalar o pacote OCR. Tente instalar manualmente pelas Configurações do Windows.",
        # Nomes de idiomas (dropdowns de origem/destino)
        "lang_en": "Inglês",     "lang_pt": "Português", "lang_es": "Espanhol",
        "lang_fr": "Francês",    "lang_de": "Alemão",    "lang_it": "Italiano",
        "lang_nl": "Holandês",   "lang_pl": "Polonês",   "lang_ru": "Russo",
        "lang_tr": "Turco",      "lang_ja": "Japonês",   "lang_zh": "Chinês",
        "lang_ko": "Coreano",    "lang_ar": "Árabe",     "lang_vi": "Vietnamita",
        # Nomes dos idiomas de interface (sempre no idioma nativo)
        "ui_lang_pt": "Português (BR)",
        "ui_lang_en": "English",
        "ui_lang_es": "Español",
    },

    "en": {
        # Tray
        "tray_tooltip_ready":       "PolyQuest — ready",
        "tray_tooltip_translating": "PolyQuest — translating...",
        "tray_tooltip_settings":    "PolyQuest — settings",
        "tray_action_translate":    "Translate screen  [{hotkey}]",
        "tray_action_settings":     "Settings...",
        "tray_action_about":        "About...",
        "tray_action_quit":         "Quit",
        "tray_msg_ready":           "Ready! Press {hotkey} to translate.",
        "tray_msg_no_text":         "No text found on screen.",
        "tray_msg_still_loading":   "OCR still loading, please wait...",
        "tray_msg_error":           "Translation error. Check the console.",
        "tray_msg_settings_saved":  "Settings saved.",
        # Settings
        "settings_title":               "PolyQuest — Settings",
        "settings_heading":             "Settings",
        "settings_section_hotkey":      "HOTKEY",
        "settings_hotkey_label":        "Hotkey:",
        "settings_hotkey_change":       "Change",
        "settings_hotkey_hint":         "Click 'Change' and press the desired key.",
        "settings_hotkey_waiting":      "Waiting — press the desired key...",
        "settings_hotkey_selected":     "Key '{key}' selected. Click Save to confirm.",
        "settings_section_capture":     "CAPTURE",
        "settings_monitor_label":       "Monitor:",
        "settings_monitor_auto":        "Automatic (active window)",
        "settings_monitor_item":        "Monitor {i}  ({w}×{h})",
        "settings_resolution_label":    "Manual resolution:",
        "settings_section_languages":   "LANGUAGES",
        "settings_source_lang":         "Source language:",
        "settings_target_lang":         "Target language:",
        "settings_section_appearance":  "APPEARANCE",
        "settings_theme_label":         "Overlay theme:",
        "settings_font_size_label":     "Font size adjust:",
        "settings_font_size_hint":      "0 pt = automatic size based on the game's text.",
        "settings_mode_label":          "Translation mode:",
        "settings_section_interface":   "INTERFACE",
        "settings_ui_language_label":   "Interface language:",
        "settings_btn_cancel":          "Cancel",
        "settings_btn_save":            "Save",
        # Translation modes
        "mode_fast":     "Speed      — captures less text, faster",
        "mode_balanced": "Balanced   — recommended default",
        "mode_precise":  "Precise    — captures more text, may be slower",
        # Themes
        "theme_dark":  "Dark",
        "theme_light": "Light",
        "theme_green": "Matrix",
        "theme_amber": "Amber",
        "theme_custom": "Custom",
        "custom_bg_color":    "Background color:",
        "custom_text_color":  "Text color:",
        "custom_opacity":     "Background opacity:",
        "custom_preview":     "Overlay preview",
        # Profiles
        "profile_section":          "GAME PROFILE",
        "profile_label":            "Active profile:",
        "profile_new":              "New",
        "profile_delete":           "Delete",
        "profile_new_title":        "New profile",
        "profile_new_prompt":       "Game name:",
        "profile_delete_confirm":   "Delete profile '{name}'?",
        "profile_default":          "Default",
        # Tray — Glossary
        "tray_action_glossary":     "Glossary...",
        # Glossary
        "glossary_title":           "PolyQuest — Glossary",
        "glossary_heading":         "Glossary",
        "glossary_add":             "Add",
        "glossary_original":        "Original",
        "glossary_translation":     "Fixed translation",
        "glossary_search":          "Search terms...",
        "glossary_remove":          "Remove",
        "glossary_count":           "{count} term(s) registered",
        "glossary_btn_close":       "Close",
        # About
        "about_title":        "About PolyQuest",
        "about_version":      "Version 1.4",
        "about_desc":         "Real-time translation overlay for gamers.\nCaptures the screen, performs OCR and displays translations directly over the game.",
        "about_developed_by": "Developed by",
        "about_authors":      "Lucas Silva  ·  Claude",
        "about_tech":         "PyQt6  ·  Windows OCR (WinRT)  ·  Google Translate  ·  PyInstaller",
        "about_btn_close":    "Close",
        # License
        "license_section":          "LICENSE",
        "license_status_label":     "Status:",
        "license_status_beta":      "Free",
        "license_status_premium":   "Premium activated",
        "license_key_label":        "License key:",
        "license_key_placeholder":  "PQ-XXXX-XXXX-XXXX",
        "license_btn_activate":     "Activate",
        "license_btn_deactivate":   "Deactivate",
        "license_activating":       "Activating...",
        "license_activated":        "Premium license activated successfully!",
        "license_error":            "Activation failed: {error}",
        "license_deactivated":      "License removed. Please restart the app.",
        "license_premium_badge":    "PREMIUM",
        "license_hint_beta":        "Premium features locked. Enter your key to unlock.",
        "license_premium_only":     "(Premium)",
        # Update
        "update_available_title":   "Update available",
        "update_available_msg":     "New version {version} available!\n\n{message}",
        "update_btn_download":      "Download",
        "update_btn_later":         "Later",
        # Overlay
        "overlay_hint": "  PolyQuest  |  Press {hotkey} to close  ",
        # OCR
        "ocr_missing_lang": (
            "Language pack '{tag}' is not installed in Windows OCR.\n\n"
            "To install:\n"
            "  Settings → Time & language → Language & region\n"
            "  → Add a language → select the desired language\n"
            "  → Options → Download 'Optical character recognition'\n\n"
            "Restart PolyQuest after installing."
        ),
        "ocr_unavailable": (
            "Windows OCR unavailable for '{tag}'. Restart PolyQuest "
            "to see language pack installation instructions."
        ),
        "ocr_req_title": "PolyQuest — Missing requirement",
        "ocr_install_prompt": (
            "The OCR language pack '{tag}' is not installed.\n\n"
            "Would you like to install it automatically?\n"
            "(Administrator access will be required)"
        ),
        "ocr_install_btn": "Install now",
        "ocr_install_btn_quit": "Quit",
        "ocr_install_success": "OCR pack installed successfully! PolyQuest will continue.",
        "ocr_install_failed": "Could not install the OCR pack. Please try installing manually via Windows Settings.",
        # Language names
        "lang_en": "English",    "lang_pt": "Portuguese", "lang_es": "Spanish",
        "lang_fr": "French",     "lang_de": "German",     "lang_it": "Italian",
        "lang_nl": "Dutch",      "lang_pl": "Polish",     "lang_ru": "Russian",
        "lang_tr": "Turkish",    "lang_ja": "Japanese",   "lang_zh": "Chinese",
        "lang_ko": "Korean",     "lang_ar": "Arabic",     "lang_vi": "Vietnamese",
        # UI language names (always in native language)
        "ui_lang_pt": "Português (BR)",
        "ui_lang_en": "English",
        "ui_lang_es": "Español",
    },

    "es": {
        # Tray
        "tray_tooltip_ready":       "PolyQuest — listo",
        "tray_tooltip_translating": "PolyQuest — traduciendo...",
        "tray_tooltip_settings":    "PolyQuest — configuración",
        "tray_action_translate":    "Traducir pantalla  [{hotkey}]",
        "tray_action_settings":     "Configuración...",
        "tray_action_about":        "Acerca de...",
        "tray_action_quit":         "Salir",
        "tray_msg_ready":           "¡Listo! Presiona {hotkey} para traducir.",
        "tray_msg_no_text":         "No se encontró texto en la pantalla.",
        "tray_msg_still_loading":   "El OCR aún está cargando, espera...",
        "tray_msg_error":           "Error al traducir. Revisa la consola.",
        "tray_msg_settings_saved":  "Configuración guardada.",
        # Settings
        "settings_title":               "PolyQuest — Configuración",
        "settings_heading":             "Configuración",
        "settings_section_hotkey":      "TECLA DE ACCESO",
        "settings_hotkey_label":        "Tecla de acceso:",
        "settings_hotkey_change":       "Cambiar",
        "settings_hotkey_hint":         "Haz clic en 'Cambiar' y presiona la tecla deseada.",
        "settings_hotkey_waiting":      "Esperando — presiona la tecla deseada...",
        "settings_hotkey_selected":     "Tecla '{key}' seleccionada. Haz clic en Guardar para confirmar.",
        "settings_section_capture":     "CAPTURA",
        "settings_monitor_label":       "Monitor:",
        "settings_monitor_auto":        "Automático (ventana activa)",
        "settings_monitor_item":        "Monitor {i}  ({w}×{h})",
        "settings_resolution_label":    "Resolución manual:",
        "settings_section_languages":   "IDIOMAS",
        "settings_source_lang":         "Idioma de origen:",
        "settings_target_lang":         "Idioma de destino:",
        "settings_section_appearance":  "APARIENCIA",
        "settings_theme_label":         "Tema del overlay:",
        "settings_font_size_label":     "Ajuste de fuente:",
        "settings_font_size_hint":      "0 pt = tamaño automatico basado en el texto del juego.",
        "settings_mode_label":          "Modo de traducción:",
        "settings_section_interface":   "INTERFAZ",
        "settings_ui_language_label":   "Idioma de la interfaz:",
        "settings_btn_cancel":          "Cancelar",
        "settings_btn_save":            "Guardar",
        # Translation modes
        "mode_fast":     "Velocidad  — captura menos texto, más rápido",
        "mode_balanced": "Equilibrado — predeterminado recomendado",
        "mode_precise":  "Preciso    — captura más texto, puede ser más lento",
        # Themes
        "theme_dark":  "Oscuro",
        "theme_light": "Claro",
        "theme_green": "Matrix",
        "theme_amber": "Ámbar",
        "theme_custom": "Personalizar",
        "custom_bg_color":    "Color de fondo:",
        "custom_text_color":  "Color del texto:",
        "custom_opacity":     "Opacidad del fondo:",
        "custom_preview":     "Vista previa del overlay",
        # Perfiles
        "profile_section":          "PERFIL DEL JUEGO",
        "profile_label":            "Perfil activo:",
        "profile_new":              "Nuevo",
        "profile_delete":           "Eliminar",
        "profile_new_title":        "Nuevo perfil",
        "profile_new_prompt":       "Nombre del juego:",
        "profile_delete_confirm":   "¿Eliminar el perfil '{name}'?",
        "profile_default":          "Predeterminado",
        # Tray — Glosario
        "tray_action_glossary":     "Glosario...",
        # Glossary
        "glossary_title":           "PolyQuest — Glosario",
        "glossary_heading":         "Glosario",
        "glossary_add":             "Agregar",
        "glossary_original":        "Original",
        "glossary_translation":     "Traducción fija",
        "glossary_search":          "Buscar términos...",
        "glossary_remove":          "Eliminar",
        "glossary_count":           "{count} término(s) registrado(s)",
        "glossary_btn_close":       "Cerrar",
        # About
        "about_title":        "Acerca de PolyQuest",
        "about_version":      "Versión 1.4",
        "about_desc":         "Overlay de traducción en tiempo real para jugadores.\nCaptura la pantalla, realiza OCR y muestra las traducciones directamente sobre el juego.",
        "about_developed_by": "Desarrollado por",
        "about_authors":      "Lucas Silva  ·  Claude",
        "about_tech":         "PyQt6  ·  Windows OCR (WinRT)  ·  Google Translate  ·  PyInstaller",
        "about_btn_close":    "Cerrar",
        # License
        "license_section":          "LICENCIA",
        "license_status_label":     "Estado:",
        "license_status_beta":      "Gratuito",
        "license_status_premium":   "Premium activado",
        "license_key_label":        "Clave de licencia:",
        "license_key_placeholder":  "PQ-XXXX-XXXX-XXXX",
        "license_btn_activate":     "Activar",
        "license_btn_deactivate":   "Desactivar",
        "license_activating":       "Activando...",
        "license_activated":        "¡Licencia Premium activada con éxito!",
        "license_error":            "Error de activación: {error}",
        "license_deactivated":      "Licencia eliminada. Reinicie la app.",
        "license_premium_badge":    "PREMIUM",
        "license_hint_beta":        "Funciones Premium bloqueadas. Ingrese su clave para desbloquear.",
        "license_premium_only":     "(Premium)",
        # Update
        "update_available_title":   "Actualización disponible",
        "update_available_msg":     "¡Nueva versión {version} disponible!\n\n{message}",
        "update_btn_download":      "Descargar",
        "update_btn_later":         "Después",
        # Overlay
        "overlay_hint": "  PolyQuest  |  Presiona {hotkey} para cerrar  ",
        # OCR
        "ocr_missing_lang": (
            "El paquete de idioma '{tag}' no está instalado en Windows OCR.\n\n"
            "Para instalar:\n"
            "  Configuración → Hora e idioma → Idioma y región\n"
            "  → Agregar un idioma → selecciona el idioma deseado\n"
            "  → Opciones → Descargar 'Reconocimiento óptico de caracteres'\n\n"
            "Reinicia PolyQuest después de instalar."
        ),
        "ocr_unavailable": (
            "Windows OCR no disponible para '{tag}'. Reinicia PolyQuest "
            "para ver las instrucciones de instalación del paquete de idioma."
        ),
        "ocr_req_title": "PolyQuest — Requisito faltante",
        "ocr_install_prompt": (
            "El paquete de idioma OCR '{tag}' no está instalado.\n\n"
            "¿Desea instalarlo automáticamente?\n"
            "(Se requerirá acceso de administrador)"
        ),
        "ocr_install_btn": "Instalar ahora",
        "ocr_install_btn_quit": "Salir",
        "ocr_install_success": "¡Paquete OCR instalado con éxito! PolyQuest continuará.",
        "ocr_install_failed": "No se pudo instalar el paquete OCR. Intente instalarlo manualmente desde la Configuración de Windows.",
        # Language names
        "lang_en": "Inglés",     "lang_pt": "Portugués", "lang_es": "Español",
        "lang_fr": "Francés",    "lang_de": "Alemán",    "lang_it": "Italiano",
        "lang_nl": "Holandés",   "lang_pl": "Polaco",    "lang_ru": "Ruso",
        "lang_tr": "Turco",      "lang_ja": "Japonés",   "lang_zh": "Chino",
        "lang_ko": "Coreano",    "lang_ar": "Árabe",     "lang_vi": "Vietnamita",
        # UI language names (always in native language)
        "ui_lang_pt": "Português (BR)",
        "ui_lang_en": "English",
        "ui_lang_es": "Español",
    },
}

# Idiomas de interface disponíveis (code, chave de nome nativo)
UI_LANGUAGES = [
    ("pt", "ui_lang_pt"),
    ("en", "ui_lang_en"),
    ("es", "ui_lang_es"),
]


def setup(lang: str) -> None:
    """Define o idioma ativo da interface."""
    global _lang
    if lang in STRINGS:
        _lang = lang


def t(key: str, **kwargs) -> str:
    """
    Retorna a string traduzida para o idioma ativo.
    Fallback: inglês → a própria chave.
    Suporta formatação: t("tray_msg_ready", hotkey="*")
    """
    s = STRINGS.get(_lang, {}).get(key) or STRINGS.get("en", {}).get(key, key)
    return s.format(**kwargs) if kwargs else s
