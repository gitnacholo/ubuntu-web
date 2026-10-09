#!/usr/bin/env python3
"""Extracción y reconstrucción de strings traducibles (ca -> es/en).

Uso:
  python3 i18n_tool.py extract <pagina.html>   -> strings_<pagina>.json
  python3 i18n_tool.py build <pagina.html> <ca|es|en>
      lee trans_<pagina>_<lang>.json (para ca no hace falta: copia + selector)
      escribe <lang>/<pagina>.html (o <pagina>.html con selector si lang=ca)

Formato trans_*.json: {"t": {id: texto}, } ; "IDENTITY-KEEP" = copiar ca.
Token [[REVISAR]] dentro de un texto (solo nodos texto) inserta
<!-- REVISAR TRADUCCIÓN --> tras el segmento y se elimina del texto.
"""
import html.parser
import json
import os
import re
import sys

BASE = r"C:\Users\NachoPC\HERMES\KlonKlonubuntu\renew001"
TMP = os.path.dirname(os.path.abspath(__file__))
UID = "IDENTITY-KEEP"
REVIEW_TOKEN = "[[REVISAR]]"
REVIEW_COMMENT = "<!-- REVISAR TRADUCCIÓN -->"

LANG_NAMES = {"ca": "Català", "es": "Español", "en": "English"}
GROUP_LABEL = {"ca": "Selector d'idioma", "es": "Selector de idioma",
               "en": "Language selector"}


class Scanner(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.cdata_elements = ("script", "style")
        self.segs = []
        self.stack = []

    def handle_starttag(self, tag, attrs):
        self.stack.append(tag)
        ad = dict(attrs)
        if tag == "meta" and ad.get("name", "").lower() == "description":
            if "content" in ad:
                self.segs.append({"kind": "attr", "tag": tag, "attr": "content",
                                  "text": ad["content"]})
            return
        for a in ("alt", "aria-label", "title", "placeholder"):
            if a in ad and ad[a].strip():
                self.segs.append({"kind": "attr", "tag": tag, "attr": a,
                                  "text": ad[a]})

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        elif tag in self.stack:
            while self.stack and self.stack[-1] != tag:
                self.stack.pop()
            self.stack.pop()

    def handle_data(self, data):
        if data.strip() and not re.fullmatch(r"[\d\s.,+×-]*", data.strip()):
            if data.strip() == "0":
                return
            self.segs.append({"kind": "text", "tag": "/".join(self.stack[-2:]),
                              "attr": None, "text": data})


def mask_scripts(html):
    out, spans, i = [], [], 0
    for m in re.finditer(r"<(script|style)\b.*?</\1\s*>", html, re.S | re.I):
        out.append(html[i:m.start()])
        out.append(f"\x00BLOCK{len(spans)}\x00")
        spans.append(m.group(0))
        i = m.end()
    out.append(html[i:])
    return "".join(out), spans


def scan_masked(masked):
    sc = Scanner()
    sc.feed(masked)
    return [s for s in sc.segs if "\x00BLOCK" not in s["text"]]


def esc_text(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def esc_attr(t):
    return t.replace("&", "&amp;").replace('"', "&quot;")


def cmd_extract(page):
    with open(os.path.join(BASE, page), encoding="utf-8") as f:
        html = f.read()
    html = re.sub(SEL_PAT, "", html)
    masked, _ = mask_scripts(html)
    segs = scan_masked(masked)
    items = [{"id": i, "kind": s["kind"], "tag": s["tag"], "attr": s["attr"],
              "ca": s["text"]} for i, s in enumerate(segs)]
    out = os.path.join(TMP, f"strings_{page}.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=1)
    print(f"{page}: {len(items)} segmentos -> {out}")


SEL_PAT = r"\n[ \t]*<div class=\"lang-selector\".*?</div>"


def splice(page, lang, html=None):
    """Devuelve el HTML con textos/atributos sustituidos (sin post-proceso)."""
    if html is None:
        with open(os.path.join(BASE, page), encoding="utf-8") as f:
            html = f.read()
    with open(os.path.join(TMP, f"trans_{page}_{lang}.json"), encoding="utf-8") as f:
        trans = json.load(f)["t"]
    masked, spans = mask_scripts(html)
    segs = scan_masked(masked)
    assert len(segs) == len(trans), f"desfase en {page}/{lang}: {len(segs)} vs {len(trans)}"

    review_idx = set()
    tr = {}
    for i, s in enumerate(segs):
        key = str(i) if str(i) in trans else i
        assert key in trans, f"falta id {i} en {page}/{lang}"
        t = trans[key]
        t = s["text"] if t == UID else t
        if REVIEW_TOKEN in t:
            assert s["kind"] == "text", f"REVISAR solo en texto (id {i})"
            t = t.replace(REVIEW_TOKEN, "")
            review_idx.add(i)
        tr[i] = t

    def _skip(txt):
        s = txt.strip()
        return (not s) or (s == "0") or bool(re.fullmatch(r"[\d\s.,+×-]*", s))

    n_text = sum(1 for s in segs if s["kind"] == "text")
    res, last, idx, done = [], 0, 0, 0
    for m in re.finditer(r">([^<]+)<", masked):
        if "\x00BLOCK" in m.group(1) or _skip(m.group(1)):
            continue
        while idx < len(segs) and segs[idx]["kind"] != "text":
            idx += 1
        assert idx < len(segs), f"texto sobrante en {page}"
        s = segs[idx]
        assert s["text"] == m.group(1), \
            f"texto {idx} no coincide en {page}: {s['text'][:40]!r}"
        res.append(masked[last:m.start(1)])
        orig = s["text"]
        lead = orig[:len(orig) - len(orig.lstrip())]
        trail = orig[len(orig.rstrip()):]
        res.append(lead + esc_text(tr[idx].strip()) + trail)
        if idx in review_idx:
            res.append(REVIEW_COMMENT)
        last = m.end(1)
        idx += 1
        done += 1
    res.append(masked[last:])
    out = "".join(res)
    assert done == n_text, f"textos sin sustituir en {page}: {done}/{n_text}"

    for i, s in enumerate(segs):
        if s["kind"] != "attr":
            continue
        pat = re.compile(r"\b" + re.escape(s["attr"]) + r'\s*=\s*"'
                         + re.escape(s["text"]) + r'"')
        def _rep(m, t=esc_attr(tr[i])):
            q = m.group(0).index('"')
            return m.group(0)[:q + 1] + t + '"'
        out, n = pat.subn(_rep, out, count=1)
        assert n == 1, f"attr {i} no encontrado en {page}"
    for j, b in enumerate(spans):
        out = out.replace(f"\x00BLOCK{j}\x00", b)
    assert "\x00BLOCK" not in out
    return out


def selector_html(page, lang):
    def href(target):
        if lang == "ca":
            return f"{target}/{page}" if target in ("es", "en") else page
        if lang == target:
            return page
        if target == "ca":
            return f"../{page}"
        return f"../{target}/{page}"
    opts = []
    for code in ("ca", "es", "en"):
        act = ' active' if code == lang else ''
        opts.append(
            f'<a href="{href(code)}" class="lang-option{act}"'
            f' aria-label="{LANG_NAMES[code]}" title="{LANG_NAMES[code]}">{code.upper()}</a>')
    return (f'<div class="lang-selector" role="group" aria-label="{GROUP_LABEL[lang]}">'
            + "".join(opts) + "</div>")


def cmd_build(page, lang):
    assert lang in ("ca", "es", "en")
    with open(os.path.join(BASE, page), encoding="utf-8") as f:
        html = f.read()
    # el selector se genera siempre de cero (rebuilds idempotentes)
    html = re.sub(SEL_PAT, "", html)
    if lang != "ca":
        html = splice(page, lang, html=html)

    # lang attr
    html = html.replace('<html lang="ca">', f'<html lang="{lang}">', 1)
    # rutas a recursos (solo en es/en)
    if lang in ("es", "en"):
        html = html.replace('href="assets/', 'href="../assets/')
        html = html.replace('src="assets/', 'src="../assets/')
    # selector de idioma tras el botón de dislexia
    pat = re.compile(r'(id="a11y-dislexia"[^>]*>.*?</button>\n)( *)</div>', re.S)
    sel = selector_html(page, lang)
    html, n = pat.subn(lambda m: m.group(1) + m.group(2) + sel + "\n" + m.group(2) + "</div>", html, count=1)
    assert n == 1, f"selector no insertado en {page}/{lang}"
    # plurales del filtro inline (scripts enmascarados ya restaurados aquí)
    if page in ("documentacion.html", "xarxa-comunitaria.html") and lang == "es":
        if page == "documentacion.html":
            html = html.replace("? ' document' : ' documents'", "? ' documento' : ' documentos'")
        else:
            html = html.replace("? ' entitat' : ' entitats'", "? ' entidad' : ' entidades'")
    if page == "xarxa-comunitaria.html" and lang == "en":
        html = html.replace("? ' entitat' : ' entitats'", "? ' entity' : ' entities'")
    # comentario de revisión al final (solo traducidas)
    if lang in ("es", "en"):
        html = html.replace("</body>", f"<!-- REVISAR TRADUCCIÓN: {lang} -->\n</body>", 1)
    dest = os.path.join(BASE, page) if lang == "ca" else os.path.join(BASE, lang, page)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8", newline="") as f:
        f.write(html)
    print(f"escrito: {dest}")


if __name__ == "__main__":
    if sys.argv[1] == "extract":
        cmd_extract(sys.argv[2])
    elif sys.argv[1] == "build":
        cmd_build(sys.argv[2], sys.argv[3])
    else:
        raise SystemExit("uso: extract|build")
