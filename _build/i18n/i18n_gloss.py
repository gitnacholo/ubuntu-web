#!/usr/bin/env python3
"""Extrae las 22 páginas y genera glosario de strings únicos + genera
trans_<page>_<lang>.json a partir de gloss_es.json / gloss_en.json."""
import json
import os
import sys

sys.path.insert(0, r"C:\Users\NachoPC\AppData\Local\Temp\opencode")
from i18n_tool import BASE, TMP, SEL_PAT, mask_scripts, scan_masked
import re as _re

PAGES = ["accessibilitat.html", "acol-3.html", "aviso-legal.html",
         "belombe.html", "canal-de-youtube.html", "cau.html",
         "centre-obert.html", "colaboradores.html", "contacte.html",
         "documentacion.html", "dons.html", "espiral.html", "index.html",
         "memories-anuals.html", "metanoia.html", "politica-cookies.html",
         "politica-privacitat.html", "projectes.html", "qui-som.html",
         "trampoli.html", "voluntariat.html", "xarxa-comunitaria.html"]

if __name__ == "__main__" and sys.argv[1] == "extract-all":
    gloss = {}  # ca -> {n, pages:[...], kinds:set, tags:set}
    page_segs = {}
    for page in PAGES:
        with open(os.path.join(BASE, page), encoding="utf-8") as f:
            html = f.read()
        html = _re.sub(SEL_PAT, "", html)
        masked, _ = mask_scripts(html)
        segs = scan_masked(masked)
        page_segs[page] = segs
        for s in segs:
            g = gloss.setdefault(s["text"], {"n": 0, "pages": [], "ctx": []})
            g["n"] += 1
            if page not in g["pages"]:
                g["pages"].append(page)
            if len(g["ctx"]) < 3:
                g["ctx"].append(f"{page}:{s['kind']}:{s['tag']}")
    with open(os.path.join(TMP, "glossary.json"), "w", encoding="utf-8") as f:
        json.dump(gloss, f, ensure_ascii=False, indent=1)
    total = sum(len(v) for v in page_segs.values())
    print(f"páginas: {len(page_segs)} | segmentos totales: {total} | únicos: {len(gloss)}")
    with open(os.path.join(TMP, "page_segs.json"), "w", encoding="utf-8") as f:
        json.dump({p: v for p, v in page_segs.items()}, f, ensure_ascii=False)
elif __name__ == "__main__" and sys.argv[1] == "gen-trans":
    lang = sys.argv[2]
    assert lang in ("es", "en")
    with open(os.path.join(TMP, "glossary.json"), encoding="utf-8") as f:
        gloss = json.load(f)
    with open(os.path.join(TMP, f"gloss_{lang}.json"), encoding="utf-8") as f:
        gl = json.load(f)
    missing = [k for k in gloss if k not in gl]
    assert not missing, f"faltan {len(missing)} en gloss_{lang}: {missing[:5]}"
    with open(os.path.join(TMP, "page_segs.json"), encoding="utf-8") as f:
        page_segs = json.load(f)
    for page, segs in page_segs.items():
        t = {str(i): gl[s["text"]] for i, s in enumerate(segs)}
        with open(os.path.join(TMP, f"trans_{page}_{lang}.json"), "w", encoding="utf-8") as f:
            json.dump({"t": t}, f, ensure_ascii=False)
    print(f"trans generados para {lang}")
