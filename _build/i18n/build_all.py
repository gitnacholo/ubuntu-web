#!/usr/bin/env python3
"""Reconstruye las 22 páginas en un idioma: python3 build_all.py es|en|ca.

Uso típico tras editar el catalán o los glosarios:
  python3 i18n_norm.py missing es   # debe dar 0
  python3 i18n_norm.py gen-trans es
  python3 build_all.py es
"""
import os
import sys
import re

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from i18n_gloss import PAGES  # noqa: E402
from i18n_tool import cmd_build  # noqa: E402

lang = sys.argv[1] if len(sys.argv) > 1 else "es"
assert lang in ("es", "en", "ca"), "uso: build_all.py es|en|ca"

# Configuración específica por idioma para el formulario de contacto
CONTACT_FORM_CONFIG = {
    "ca": {"_next": "gracias.html", "_subject": "Nou contacte des de la web Ubuntu"},
    "es": {"_next": "gracias.html", "_subject": "Nuevo contacto desde la web Ubuntu"},
    "en": {"_next": "thank-you.html", "_subject": "New contact from Ubuntu website"},
}

def fix_contact_form(page_path, lang):
    """Corrige los campos ocultos del formulario de contacto según el idioma."""
    if "contacte.html" not in page_path:
        return
    with open(page_path, encoding="utf-8") as f:
        html = f.read()
    
    config = CONTACT_FORM_CONFIG[lang]
    
    # Corregir/agregar _next
    if 'name="_next"' not in html:
        # Agregar _next después del último input hidden o antes del botón submit
        html = html.replace(
            '<div class="full">',
            f'<input type="hidden" name="_next" value="{config["_next"]}">\n            <div class="full">'
        )
    else:
        # Corregir _next existente
        html = re.sub(
            r'name="_next" value="[^"]*"',
            f'name="_next" value="{config["_next"]}"',
            html
        )
    
    # Corregir/agregar _subject
    if 'name="_subject"' not in html:
        # Agregar _subject después del _next o antes del botón submit
        html = html.replace(
            f'name="_next" value="{config["_next"]}">',
            f'name="_next" value="{config["_next"]}">\n            <input type="hidden" name="_subject" value="{config["_subject"]}">'
        )
    else:
        # Corregir _subject existente
        html = re.sub(
            r'name="_subject" value="[^"]*"',
            f'name="_subject" value="{config["_subject"]}"',
            html
        )
    
    with open(page_path, "w", encoding="utf-8", newline="") as f:
        f.write(html)


for p in PAGES:
    try:
        cmd_build(p, lang)
        # Post-procesar el formulario de contacto
        dest = os.path.join(HERE, "..", "..", lang if lang != "ca" else "", p)
        if os.path.exists(dest):
            fix_contact_form(dest, lang)
    except Exception as e:  # noqa
        print(f"ERROR {p}: {e}")
