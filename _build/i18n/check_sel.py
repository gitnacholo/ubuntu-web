#!/usr/bin/env python3
import os

BASE = r"C:\Users\NachoPC\HERMES\KlonKlonubuntu\renew001"
PAGES = ["accessibilitat.html", "acol-3.html", "aviso-legal.html",
         "belombe.html", "canal-de-youtube.html", "cau.html",
         "centre-obert.html", "colaboradores.html", "contacte.html",
         "documentacion.html", "dons.html", "espiral.html", "index.html",
         "memories-anuals.html", "metanoia.html", "politica-cookies.html",
         "politica-privacitat.html", "projectes.html", "qui-som.html",
         "trampoli.html", "voluntariat.html", "xarxa-comunitaria.html"]
bad = 0
for prefix in ("", "es/", "en/"):
    for p in PAGES:
        with open(os.path.join(BASE, prefix + p), encoding="utf-8") as f:
            n = f.read().count('class="lang-selector"')
        if n != 1:
            print(f"MAL {prefix + p}: {n}")
            bad += 1
with open(os.path.join(BASE, "butlleti-ubuntu.html"), encoding="utf-8") as f:
    b = f.read()
print("butlleti selector:", b.count('class="lang-selector"'), "| lang:", "lang=\"ca\"" in b)
print("MAL:", bad)
