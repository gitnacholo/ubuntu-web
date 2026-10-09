#!/usr/bin/env python3
"""Verifica la versión multidioma: selector, lang, rutas, enlaces."""
import os
import re

BASE = r"C:\Users\NachoPC\HERMES\KlonKlonubuntu\renew001"
PAGES = ["accessibilitat.html", "acol-3.html", "aviso-legal.html",
         "belombe.html", "canal-de-youtube.html", "cau.html",
         "centre-obert.html", "colaboradores.html", "contacte.html",
         "documentacion.html", "dons.html", "espiral.html", "index.html",
         "memories-anuals.html", "metanoia.html", "politica-cookies.html",
         "politica-privacitat.html", "projectes.html", "qui-som.html",
         "trampoli.html", "voluntariat.html", "xarxa-comunitaria.html"]

fails = []


def check(cond, msg):
    if not cond:
        fails.append(msg)
        print("FALLO:", msg)


for lang, prefix, exp_lang in (("ca", "", "ca"), ("es", "es/", "es"), ("en", "en/", "en")):
    for page in PAGES:
        p = os.path.join(BASE, prefix + page)
        check(os.path.exists(p), f"falta {prefix + page}")
        if not os.path.exists(p):
            continue
        with open(p, encoding="utf-8") as f:
            h = f.read()
        check(f'<html lang="{exp_lang}">' in h, f"{prefix + page}: lang")
        check('class="lang-selector"' in h, f"{prefix + page}: sin selector")
        check('REVISAR TRADUCCIÓN' in h if lang != "ca" else True, f"{prefix + page}: sin marca revisión")
        # rutas de recursos
        if lang == "ca":
            check('href="assets/' in h or 'src="assets/' in h, f"{prefix + page}: rutas ca")
            check('../assets/' not in h, f"{prefix + page}: ../ indebido en ca")
        else:
            check('../assets/' in h, f"{prefix + page}: sin ../assets")
            bad = re.findall(r'(?:href|src)="(assets/[^"]+)"', h)
            check(not bad, f"{prefix + page}: rutas sin ../: {bad[:3]}")
        # selector: 3 opciones, 1 activa, hrefs correctos
        m = re.search(r'<div class="lang-selector".*?</div>', h, re.S)
        check(bool(m), f"{prefix + page}: selector malformado")
        if m:
            opts = re.findall(r'<a href="([^"]+)" class="lang-option( active)?"', m.group(0))
            check(len(opts) == 3, f"{prefix + page}: opciones={len(opts)}")
            check(sum(1 for _, a in opts if a) == 1, f"{prefix + page}: active count")
            exp = {"ca": [page, f"es/{page}", f"en/{page}"],
                   "es": [f"../{page}", page, f"../en/{page}"],
                   "en": [f"../{page}", f"../es/{page}", page]}[lang]
            got = [o[0] for o in opts]
            check(got == exp, f"{prefix + page}: hrefs {got} != {exp}")
        # enlaces internos existen en el mismo idioma
        for dest in set(re.findall(r'href="([a-z0-9-]+\.html)"', h)):
            dp = os.path.join(BASE, prefix + dest)
            check(os.path.exists(dp), f"{prefix + page} -> {dest} roto")

print("FALLOS:", len(fails))
