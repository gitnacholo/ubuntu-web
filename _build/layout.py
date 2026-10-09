# -*- coding: utf-8 -*-
"""Shell común de las páginas v2: head, header, nav, footer + render()."""
import os

V2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NAV = [
    ('index.html', 'Inici'),
    ('qui-som.html', 'Qui som'),
    ('projectes.html', 'Projectes'),
    ('voluntariat.html', 'Voluntariat'),
    ('dons.html', 'Donacions'),
    ('contacte.html', 'Contacte'),
]

LOGO = 'assets/img/logo/logo-sq.webp'
FAVICON = 'assets/img/logo/favicon.png'

def _nav_links(active, prefix=''):
    items = []
    for href, label in NAV:
        cls = ' aria-current="page"' if href == active else ''
        items.append('<li><a href="%s%s"%s>%s</a></li>' % (prefix, href, cls, label))
    return '\n            '.join(items)

def head(title, desc, active='index.html'):
    canonical = active
    return """<!DOCTYPE html>
<html lang="ca">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%s</title>
<meta name="description" content="%s">
<link rel="icon" type="image/png" href="%s">
<link rel="stylesheet" href="assets/fonts/fonts.css">
<link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>
<a class="skip-link" href="#contingut">Salta al contingut principal</a>""" % (title, desc, FAVICON)

def header(active='index.html'):
    return """
<header class="site-header">
  <div class="container">
    <div class="header-inner">
      <a href="index.html" class="brand" aria-label="Associació Ubuntu - inici">
        <img src="%s" alt="Logo de l'Associació Educació i Lleure Ubuntu" width="44" height="44">
        <span><strong>Ubuntu</strong><small>Educació i Lleure</small></span>
      </a>
      <nav class="nav-desktop" aria-label="Navegació principal">
        <ul class="nav-list">
        %s
        </ul>
        <a class="btn btn-primary" href="dons.html">Dona ara</a>
      </nav>
      <button class="nav-toggle" aria-expanded="false" aria-controls="mobile-nav" aria-label="Obre el menú">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>
<nav class="mobile-nav" id="mobile-nav" aria-label="Menú mòbil">
  <ul>
    %s
  </ul>
  <a class="btn btn-primary btn-lg" href="dons.html">Dona ara</a>
  <a class="btn btn-secondary btn-lg" href="voluntariat.html">Fes-te voluntari/a</a>
</nav>""" % (LOGO, _nav_links(active), _nav_links(active))

SOCIAL = """
<div class="footer-social">
  <a href="https://www.facebook.com/associacioubuntu" aria-label="Facebook de l'Associació Ubuntu" rel="noopener"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg></a>
  <a href="https://www.instagram.com/associacioubuntu" aria-label="Instagram de l'Associació Ubuntu" rel="noopener"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg></a>
  <a href="canal-de-youtube.html" aria-label="Canal de YouTube de l'Associació Ubuntu"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M23.5 6.19a3.02 3.02 0 0 0-2.12-2.14C19.5 3.55 12 3.55 12 3.55s-7.5 0-9.38.5A3.02 3.02 0 0 0 .5 6.19C0 8.07 0 12 0 12s0 3.93.5 5.81a3.02 3.02 0 0 0 2.12 2.14c1.88.5 9.38.5 9.38.5s7.5 0 9.38-.5a3.02 3.02 0 0 0 2.12-2.14C24 15.93 24 12 24 12s0-3.93-.5-5.81zM9.55 15.57V8.43L15.82 12l-6.27 3.57z"/></svg></a>
</div>"""

def footer():
    return """
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <h3>Associació Educació i Lleure Ubuntu</h3>
        <p>“Jo sóc perquè tu ets”. Oci educatiu, acompanyament familiar i comunitat
        al barri de Ciutat Meridiana des de l'any 2008.</p>
        <p>Entitat sense ànim de lucre registrada amb el nº 49677, declarada d'utilitat pública (Llei 49/2002).</p>
        <address style="font-style:normal;">
          C/ Vallcivera, 24-26 · 08033 Barcelona<br>
          <a href="mailto:ubuntu@associacioubuntu.org">ubuntu@associacioubuntu.org</a><br>
          <a href="tel:+34620015846">+34 620 01 58 46</a>
        </address>
      </div>
      <div>
        <h3>Enllaços ràpids</h3>
        <ul>
          <li><a href="qui-som.html">Qui som</a></li>
          <li><a href="projectes.html">Projectes</a></li>
          <li><a href="voluntariat.html">Voluntariat i pràctiques</a></li>
          <li><a href="dons.html">Donacions i socis</a></li>
          <li><a href="contacte.html">Contacte</a></li>
          <li><a href="memories-anuals.html">Memòries i revista</a></li>
        </ul>
      </div>
      <div>
        <h3>Projectes</h3>
        <ul>
          <li><a href="cau.html">CAU</a></li>
          <li><a href="centre-obert.html">Centre Obert</a></li>
          <li><a href="trampoli.html">Trampolí</a></li>
          <li><a href="espiral.html">Espiral</a></li>
          <li><a href="xarxa-comunitaria.html">Xarxa comunitària</a></li>
        </ul>
      </div>
      <div>
        <h3>La teva ajuda importa</h3>
        <div class="footer-cta">
          <p>Amb el teu donatiu, més infants de la Zona Nord tindran ocio educatiu cada setmana.</p>
          <a class="btn btn-white btn-primary" style="background:#fff;color:var(--vermell-fosc);" href="dons.html">Dona ara</a>
        </div>
        <h3 class="mt-3">Segueix-nos</h3>
        %s
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Associació Educació i Lleure Ubuntu</span>
      <span class="registro">Registre d'associacions nº 49677</span>
      <span>
        <a href="politica-privacitat.html">Privacitat</a> ·
        <a href="aviso-legal.html">Avís legal</a> ·
        <a href="politica-cookies.html">Cookies</a> ·
        <a href="accessibilitat.html">Accessibilitat</a>
      </span>
    </div>
  </div>
</footer>
<div class="cookie-notice" id="cookieNotice" role="dialog" aria-label="Avís de cookies" style="display:none;position:fixed;bottom:1rem;left:1rem;right:1rem;z-index:70;background:#241B12;color:#fff;border-radius:14px;padding:1rem 1.3rem;max-width:640px;margin-inline:auto;box-shadow:0 10px 30px rgba(0,0,0,.35);">
  <p style="margin:0 0 .7rem;font-size:.9rem;">Aquest web utilitza cookies tècniques per millorar la teva experiència. Pots llegir la <a href="politica-cookies.html" style="color:var(--groc);">política de cookies</a>.</p>
  <button class="cookie-btn btn" style="min-height:40px;background:var(--groc);color:#3A2400;border:0;font-weight:700;cursor:pointer;">D'acord</button>
</div>
<script src="assets/js/main.js" defer></script>
</body>
</html>""" % SOCIAL

def render(fname, title, desc, content, active='index.html'):
    html_doc = head(title, desc, active) + header(active) + content + footer()
    path = os.path.join(V2, fname)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(html_doc)
    print('WROTE', fname, len(html_doc), 'bytes')
