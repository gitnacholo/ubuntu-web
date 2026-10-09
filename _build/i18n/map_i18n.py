#!/usr/bin/env python3
"""Mapa d'URLs CA/ES/EN -> renew001/mapa_urls.md. Uso: python3 map_i18n.py."""
import os
import re
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.normpath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(BASE, "mapa_urls.md")
LANGS = [("", "català"), ("es/", "castellano"), ("en/", "english")]
href_re = re.compile(r'href="([^"]+)"')


def analyze(prefix):
    d = os.path.join(BASE, prefix.rstrip("/") or ".")
    pages = sorted(f for f in os.listdir(d) if f.endswith(".html"))
    out = {}
    for fn in pages:
        with open(os.path.join(d, fn), encoding="utf-8") as f:
            html = f.read()
        ins = Counter()
        for h in href_re.findall(html):
            if h.startswith(("http://", "https://", "//", "mailto:", "tel:", "#")) or h == "":
                continue
            dest = h.split("#")[0].split("?")[0]
            if not dest.endswith(".html"):
                continue
            if "/" in dest:  # ../x o es/x : resoldre des de la carpeta de la pàgina
                tgt = os.path.normpath(os.path.join(d, dest))
                if not tgt.replace("\\", "/").startswith(BASE.replace("\\", "/")):
                    continue  # fora de renew001
                dest = os.path.relpath(tgt, BASE).replace("\\", "/")
            else:
                dest = (prefix + dest).replace("\\", "/")
            ins[dest] += 1
        out[prefix + fn] = ins
    return pages, out


L = ["# Mapa d'URLs — renew001 (CA/ES/EN)\n"]
L.append("Enllaços `href` interns per idioma (sense `#`, `mailto:` ni `tel:`). "
         "Les pàgines ES/EN enllacen dins del seu idioma (`../assets/` només per recursos).\n")
all_broken, all_orphan = [], []
for prefix, nom in LANGS:
    pages, out = analyze(prefix)
    tag = prefix or "ca/"
    in_links = Counter()
    for c in out.values():
        for dd in c:
            in_links[dd] += 1
    broken, orphans = [], []
    for fn, c in out.items():
        for dd in c:
            full = os.path.join(BASE, *dd.split("/"))
            if not os.path.exists(full):
                broken.append(f"{fn} → {dd}")
    for fn in [prefix + p for p in pages]:
        if in_links[fn] == 0 and fn != "index.html":
            orphans.append(fn)
    all_broken += broken
    all_orphan += orphans
    L.append(f"## {tag} — {len(pages)} pàgines\n")
    L.append("| Pàgina | Sortints únics | Entrants |")
    L.append("|---|---|---|")
    for fn in pages:
        key = prefix + fn
        L.append(f"| `{key}` | {len(out[key])} | {in_links[key]} |")
    L.append("")
    L.append(f"### Enllaços `{tag}` (origen → destinacions)\n")
    for fn in pages:
        key = prefix + fn
        L.append(f"#### `{key}`")
        for dd in sorted(out[key]):
            L.append(f"- → `{dd}` (×{out[key][dd]})")
        L.append("")
L.append("## Incidències globals\n")
L.append("- Trencats: " + (", ".join(f"`{b}`" for b in all_broken) if all_broken else "cap ✅"))
L.append("- Òrfenes: " + (", ".join(f"`{p}`" for p in all_orphan) if all_orphan else "cap ✅"))
L.append("")

with open(OUT, "w", encoding="utf-8", newline="") as f:
    f.write("\n".join(L))
print(f"Escrit: {OUT} | trencats={all_broken} | òrfenes={all_orphan}")
