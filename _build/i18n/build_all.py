#!/usr/bin/env python3
"""Reconstruye las 22 páginas en un idioma: python3 build_all.py es|en|ca.

Uso típico tras editar el catalán o los glosarios:
  python3 i18n_norm.py missing es   # debe dar 0
  python3 i18n_norm.py gen-trans es
  python3 build_all.py es
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from i18n_gloss import PAGES  # noqa: E402
from i18n_tool import cmd_build  # noqa: E402

lang = sys.argv[1] if len(sys.argv) > 1 else "es"
assert lang in ("es", "en", "ca"), "uso: build_all.py es|en|ca"
for p in PAGES:
    try:
        cmd_build(p, lang)
    except Exception as e:  # noqa
        print(f"ERROR {p}: {e}")
