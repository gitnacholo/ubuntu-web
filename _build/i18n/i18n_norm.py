#!/usr/bin/env python3
"""Normalización + auto-identidad + fusión de parciales + gen-trans.

Claves de gloss_*.json: texto catalán NORMALIZADO (" ".join(split)).
gen-trans busca por texto normalizado; detecta colisiones.
"""
import json
import os
import re
import sys

sys.path.insert(0, r"C:\Users\NachoPC\AppData\Local\Temp\opencode")
from i18n_gloss import PAGES  # noqa
from i18n_tool import BASE, TMP, mask_scripts, scan_masked

ENTITY = "Associació Educació i Lleure Ubuntu"


def norm(t):
    return " ".join(t.split())


def auto_identity(t):
    n = norm(t)
    if n in (ENTITY, "Ubuntu", "PDF", "A+", "A-"):
        return True
    if re.fullmatch(r"[\w.%+-]+@[\w.-]+\.\w+", n):
        return True
    if re.fullmatch(r"https?://\S+", n):
        return True
    if re.fullmatch(r"[+\d][\d\s./()+-]*", n) and re.search(r"\d", n) and not re.search(r"[A-Za-zÀ-ÿ]", n):
        return True
    if re.fullmatch(r"C/ [\w.,  ·-]+", n):
        return True
    if not re.search(r"[A-Za-zÀ-ÿ0-9]", n):
        return True
    if n == f"© 2026 {ENTITY}":
        return True
    return False


def load_gloss(lang):
    """Fusiona gloss_<lang>.json + gloss_<lang>_c*.json (los últimos ganan)."""
    merged = {}
    names = [f"gloss_{lang}.json"] + sorted(
        f for f in os.listdir(TMP)
        if f.startswith(f"gloss_{lang}_c") and f.endswith(".json"))
    for name in names:
        p = os.path.join(TMP, name)
        if os.path.exists(p):
            with open(p, encoding="utf-8") as f:
                merged.update(json.load(f))
    return merged


if sys.argv[1] == "seed-identity":
    for lang in ("es", "en"):
        with open(os.path.join(TMP, "glossary.json"), encoding="utf-8") as f:
            gloss = json.load(f)
        seed = {norm(k): norm(k) for k in gloss if auto_identity(k)}
        with open(os.path.join(TMP, f"gloss_{lang}.json"), "w", encoding="utf-8") as f:
            json.dump(seed, f, ensure_ascii=False, indent=1)
        print(f"{lang}: {len(seed)} identidades automáticas")
elif sys.argv[1] == "missing":
    lang = sys.argv[2]
    with open(os.path.join(TMP, "glossary.json"), encoding="utf-8") as f:
        gloss = json.load(f)
    merged = load_gloss(lang)
    miss = [norm(k) for k in gloss if norm(k) not in merged]
    print(f"{lang}: faltan {len(miss)}")
    out = os.path.join(TMP, f"missing_{lang}.txt")
    with open(out, "w", encoding="utf-8") as f:
        for m in miss:
            f.write("FALTA :: " + m + "\n")
    print(f"detalle en {out}")
elif sys.argv[1] == "gen-trans":
    lang = sys.argv[2]
    assert lang in ("es", "en")
    with open(os.path.join(TMP, "glossary.json"), encoding="utf-8") as f:
        gloss = json.load(f)
    merged = load_gloss(lang)
    # colisiones: raws distintos con misma norma y ¿traducciones distintas? (misma aquí)
    seen = {}
    for k in gloss:
        nk = norm(k)
        seen.setdefault(nk, set()).add(k)
    coll = {nk: v for nk, v in seen.items() if len(v) > 1}
    if coll:
        print(f"AVISO colisiones de normalización: {len(coll)}")
        for nk, v in list(coll.items())[:10]:
            print("  COL:", [x[:60] for x in v])
    missing = [norm(k) for k in gloss if norm(k) not in merged]
    assert not missing, f"faltan {len(missing)}: {missing[:5]}"
    with open(os.path.join(TMP, "page_segs.json"), encoding="utf-8") as f:
        page_segs = json.load(f)
    for page, segs in page_segs.items():
        t = {str(i): merged[norm(s["text"])] for i, s in enumerate(segs)}
        with open(os.path.join(TMP, f"trans_{page}_{lang}.json"), "w", encoding="utf-8") as f:
            json.dump({"t": t}, f, ensure_ascii=False)
    print(f"trans generados para {lang}")
elif sys.argv[1] == "chunk":
    a, b = int(sys.argv[2]), int(sys.argv[3])
    with open(os.path.join(TMP, "glossary.json"), encoding="utf-8") as f:
        gloss = json.load(f)
    items = sorted(gloss.items(), key=lambda kv: (-kv[1]["n"], kv[0]))
    # agrupa por norma (muestra 1 vez)
    seen_norm, ordered = set(), []
    for k, g in items:
        if norm(k) not in seen_norm:
            seen_norm.add(norm(k))
            ordered.append((k, g))
    print(f"únicos-norm={len(ordered)} mostrando [{a}:{b}]")
    lines = [f"únicos-norm={len(ordered)} bloque [{a}:{b}]"]
    for k, g in ordered[a:b]:
        auto = " [AUTO]" if auto_identity(k) else ""
        ctx = " | ".join(g["ctx"][:3])
        lines.append(f"[{g['n']}x]{auto} :: {norm(k)}")
        lines.append(f"    ctx: {ctx}")
    out = os.path.join(TMP, f"chunk_{a}_{b}.txt")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"escrito {out}")
