# -*- coding: utf-8 -*-
"""Completa v2: 3 fotos de galería extra + páginas de detalle/legales dentro de v2
(cau, centre-obert, trampoli, espiral, xarxa, acol, memòries, butlletí, documentació,
canal-youtube, política privacitat, avís legal, política cookies, accessibilitat)."""
import os, re, sys, html as hm
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from layout import render, footer, header, head

CLONE = r'C:\Users\NachoPC\HERMES\KlonKlonubuntu'
FTP   = r'g:\_borrar_\ubuntu_cdmon\web\wp-content\uploads'
V2    = os.path.join(CLONE, 'v2')

# ---------- 1) galería extra (fotos reales del FTP) ----------
def webp(rel, out, max_w=1000, q=76):
    p = os.path.join(FTP, rel)
    if not os.path.isfile(p):
        p = os.path.join(CLONE, rel)
    im = Image.open(p).convert('RGB')
    if im.width > max_w:
        im = im.resize((max_w, int(im.height * max_w / im.width)), Image.LANCZOS)
    outp = os.path.join(V2, 'assets', 'img', out)
    os.makedirs(os.path.dirname(outp), exist_ok=True)
    im.save(outp, 'WEBP', quality=q, method=6)
    print('gallery', out)

webp(r'2024\05\IMG_20211123_172615442.jpg', 'gallery/gallery-3.webp')
webp(r'2024\05\IMG-20210928-WA0042.jpg', 'gallery/gallery-4.webp')
webp(r'2024\05\Actividad-Espiral.jpg', 'gallery/gallery-5.webp')

# ---------- 2) utilidades ----------
def banner(h1, lead, img, alt, crumb):
    return """
<section class="page-banner" aria-label="%s">
  <div class="hero-bg"><img src="%s" alt="%s" loading="lazy"></div>
  <div class="container">
    <div class="hero-content">
      <h1>%s</h1>
      <p class="lead">%s</p>
      <nav class="breadcrumb" aria-label="Migues de pa"><a href="index.html">Inici</a> / %s</nav>
    </div>
  </div>
</section>""" % (h1, img, alt, h1, lead, crumb)

def extract_text(v1file):
    """Extrae los párrafos/h3 del contenido de una página v1."""
    t = open(os.path.join(CLONE, v1file), encoding='utf-8').read()
    t = re.sub(r'<head>.*?</head>', ' ', t, flags=re.S)
    t = re.sub(r'<script.*?</script>', ' ', t, flags=re.S)
    t = re.sub(r'<!--.*?-->', ' ', t, flags=re.S)
    # cortar en el footer
    t = re.sub(r'<footer.*', ' ', t, flags=re.S)
    t = re.sub(r'<(h2|h3)[^>]*>', '\n@@ ', t)
    t = re.sub(r'</(h2|h3)>', '\n', t)
    t = re.sub(r'<li[^>]*>', '\n- ', t)
    t = re.sub(r'<img[^>]*>', ' ', t)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = hm.unescape(t)
    lines = [re.sub(r'\s+', ' ', l).strip() for l in t.split('\n')]
    out = []
    for l in lines:
        if l and l not in ('-',):
            out.append(l)
    return out

def simple_page(v1file, fname, title, h1, lead, img, alt, crumb, cta_html=''):
    """Página interior simple con el contenido textual de la página v1."""
    lines = extract_text(v1file)
    parts = ['<main id="contingut">', banner(h1, lead, img, alt, crumb),
             '<section class="section"><div class="container" style="max-width:820px;">']
    for l in lines:
        if l.startswith('@@ '):
            parts.append('<h3>%s</h3>' % l[3:])
        elif l.startswith('- '):
            parts.append('<li>%s</li>' % l[2:])
        elif l.startswith('Benvinguts') or l.startswith('ubuntu@associacio'):
            continue
        else:
            parts.append('<p>%s</p>' % l)
    parts.append('<ul>')  # placeholder; los <li> sueltos los dejamos simples
    parts = '\n'.join(parts)
    parts = parts.replace('<ul>\n', '')  # limpiar
    parts += '\n%s\n</div></section>\n%s\n</main>' % (cta_html, '')
    doc = head(title, lead, active=fname) + header(fname) + parts + footer()
    with open(os.path.join(V2, fname), 'w', encoding='utf-8', newline='\n') as f:
        f.write(doc)
    print('WROTE', fname)

# ---------- 3) páginas de proyecto (contenido real v1) ----------
PROJECT_FILES = [
    ('cau.html', 'cau.html', 'CAU | Associació Ubuntu',
     'CAU', 'Espai de lleure educatiu per a infants de 6 a 12 anys, els dissabtes a la tarda.',
     'assets/img/projects/cau.webp', 'Infants participant en activitats del CAU',
     'Projectes / CAU',
     '<a class="btn btn-primary" href="dons.html">Apoya el CAU amb un donatiu</a> <a class="btn btn-secondary" href="voluntariat.html" style="margin-left:.5rem;">Fes-te voluntari/a al CAU</a>'),
    ('centre-obert.html', 'centre-obert.html', 'Centre Obert | Associació Ubuntu',
     'Centre Obert', 'Lleure educatiu i reforç escolar per a infants i adolescents de 6 a 16 anys.',
     'assets/img/projects/centre-obert.webp', 'Reforç escolar al Centre Obert',
     'Projectes / Centre Obert',
     '<a class="btn btn-primary" href="dons.html">Apoya el Centre Obert</a> <a class="btn btn-secondary" href="voluntariat.html" style="margin-left:.5rem;">Fes-te voluntari/a</a>'),
    ('trampoli.html', 'trampoli.html', 'Trampolí | Associació Ubuntu',
     'Trampolí', 'Atenció psicològica, psicopedagògica i logopèdica dins la xarxa de l\'escola pública.',
     'assets/img/projects/trampoli.webp', 'Sessió d\'atenció del projecte Trampolí',
     'Projectes / Trampolí',
     '<a class="btn btn-primary" href="dons.html">Apoya Trampolí</a>'),
    ('espiral.html', 'espiral.html', 'Espiral | Associació Ubuntu',
     'Espiral', 'Acompanyament matern-infantil (0-6 anys): el projecte Teixim Vincles.',
     'assets/img/projects/espiral.webp', 'Espai d\'acompanyament familiar Espiral',
     'Projectes / Espiral',
     '<a class="btn btn-primary" href="dons.html">Apoya Espiral</a>'),
]
for fname, v1, title, h1, lead, img, alt, crumb, cta in PROJECT_FILES:
    simple_page(v1, fname, title, h1, lead, img, alt, crumb, cta)

# ---------- 4) xarxa comunitària con logos ----------
logo_dir = os.path.join(V2, 'assets', 'img', 'xarxa')
logos = sorted(os.listdir(logo_dir)) if os.path.isdir(logo_dir) else []
def pretty(slug):
    s = slug.replace('.webp', '').replace('-', ' ')
    return s[:1].upper() + s[1:]
logo_items = '\n'.join(
    '<div class="logo-item"><img src="assets/img/xarxa/%s" alt="%s" loading="lazy"></div>'
    % (f, pretty(f)) for f in logos)
XARXA = """
<main id="contingut">
%s
  <section class="section">
    <div class="container">
      <blockquote class="quote-block reveal">“Molta gent petita, en llocs petits, fent coses petites, pot canviar el món.”<cite>Eduardo Galeano</cite></blockquote>
      <div class="mt-4 reveal">
        <p>Des d'Ubuntu creiem que és cabdal el treball comunitari: treballem de manera coordinada,
        tant entre els diferents projectes de l'associació com amb altres entitats, recursos i
        equipaments del barri i de la ciutat.</p>
      </div>
      <div class="section-head center mt-4 reveal"><h2>Entitats i equipaments de la xarxa</h2></div>
      <div class="logo-grid reveal">%s</div>
      <div class="mt-4 text-center reveal">
        <a class="btn btn-primary" href="dons.html">Apoya la xarxa comunitària</a>
      </div>
    </div>
  </section>
</main>
""" % (banner('Xarxa comunitària',
              'Teixim xarxa amb les entitats i equipaments del territori.',
              'assets/img/projects/xarxa.webp',
              'Plaça d\'Ubuntu durant una festa comunitària',
              'Xarxa comunitària'), logo_items)
doc = head('Xarxa comunitària | Associació Ubuntu',
           'La xarxa comunitària d\'Ubuntu: entitats, escoles i equipaments de la Zona Nord de Barcelona.',
           'xarxa-comunitaria.html') + header('xarxa-comunitaria.html') + XARXA + footer()
open(os.path.join(V2, 'xarxa-comunitaria.html'), 'w', encoding='utf-8', newline='\n').write(doc)
print('WROTE xarxa-comunitaria.html')

# ---------- 5) ACOL ----------
simple_page('acol-3.html', 'acol-3.html', 'ACOL | Associació Ubuntu',
            'ACOL · Treball i formació',
            'Programa d\'inserció laboral per a persones migrades en situació administrativa irregular.',
            'assets/img/projects/acol.webp', 'Cartell del programa ACOL 2022-2023',
            'ACOL',
            '<a class="btn btn-primary" href="contacte.html">Contacta\'ns per l\'ACOL</a>')

# ---------- 6) memòries / butlletí / documentació / youtube ----------
MEMORIES = """
<main id="contingut">
%s
  <section class="section">
    <div class="container">
      <div class="section-head reveal"><span class="kicker">Transparència</span><h2>Memòries i revista Ubuntu</h2>
      <p class="lead">Rendim comptes cada any: consulta les nostres memòries i la revista de la comunitat.</p></div>
      <div class="grid-3">
        <article class="card reveal"><div class="card-media"><img src="assets/img/memories/revista-1.webp" alt="Portada de la revista Ubuntu" loading="lazy"></div><div class="card-body"><h3>Revista Ubuntu</h3><p>La revista de la comunitat Ubuntu: projectes, activitats i veus del barri.</p></div></article>
        <article class="card reveal d1"><div class="card-media"><img src="assets/img/memories/memoria-2025.webp" alt="Portada de la memòria curta 2025" loading="lazy"></div><div class="card-body"><h3>Memòria 2025</h3><p>Resum d'activitats i comptes de l'exercici 2025.</p></div></article>
        <article class="card reveal d2"><div class="card-media"><img src="assets/img/memories/memoria-2024.webp" alt="Portada de la memòria curta 2024" loading="lazy"></div><div class="card-body"><h3>Memòria 2024</h3><p>Resum d'activitats i comptes de l'exercici 2024.</p></div></article>
      </div>
      <div class="mt-4 text-center reveal">
        <a class="btn btn-primary" href="dons.html">Apoya els nostres projectes</a>
      </div>
    </div>
  </section>
</main>
""" % banner('Memòries i revista', 'Transparència: la feina de cada any, explicada.',
             'assets/img/memories/memoria-2023.webp', 'Portada de la memòria 2023', 'Memòries')
doc = head('Memòries anuals | Associació Ubuntu', 'Memòries anuals i revista de l\'Associació Ubuntu.',
           'memories-anuals.html') + header('memories-anuals.html') + MEMORIES + footer()
open(os.path.join(V2, 'memories-anuals.html'), 'w', encoding='utf-8', newline='\n').write(doc)
print('WROTE memories-anuals.html')

BUTLLETI = """
<main id="contingut">
%s
  <section class="section">
    <div class="container">
      <div class="section-head reveal"><span class="kicker">Comunicació</span><h2>Butlletí Ubuntu</h2>
      <p class="lead">Cada mes expliquem què passa a la tribu. Subscriu-t'hi escrivint-nos.</p></div>
      <div class="grid-3">
        <article class="card reveal"><div class="card-media"><img src="assets/img/memories/butlleti-1.webp" alt="Portada del butlletí d'abril de 2022" loading="lazy"></div><div class="card-body"><h3>Butlletí · Abril 2022</h3></div></article>
        <article class="card reveal d1"><div class="card-media"><img src="assets/img/memories/butlleti-3.webp" alt="Portada del butlletí de febrer de 2021" loading="lazy"></div><div class="card-body"><h3>Butlletí · Febrer 2021</h3></div></article>
        <article class="card reveal d2"><div class="card-media"><img src="assets/img/memories/butlleti-2.webp" alt="Portada del butlletí de març de 2021" loading="lazy"></div><div class="card-body"><h3>Butlletí · Març 2021</h3></div></article>
      </div>
      <div class="mt-4 text-center reveal">
        <a class="btn btn-primary" href="mailto:ubuntu@associacioubuntu.org?subject=Butlletí">Vull rebre el butlletí</a>
      </div>
    </div>
  </section>
</main>
""" % banner('Butlletí Ubuntu', 'Notícies de la comunitat, cada mes.',
             'assets/img/memories/butlleti-1.webp', 'Portada d\'un butlletí d\'Ubuntu', 'Butlletí')
doc = head('Butlletí Ubuntu | Associació Ubuntu', 'Butlletí mensual de l\'Associació Ubuntu.',
           'butlleti-ubuntu.html') + header('butlleti-ubuntu.html') + BUTLLETI + footer()
open(os.path.join(V2, 'butlleti-ubuntu.html'), 'w', encoding='utf-8', newline='\n').write(doc)
print('WROTE butlleti-ubuntu.html')

YT = """
<main id="contingut">
%s
  <section class="section">
    <div class="container" style="max-width:900px;">
      <div class="section-head center reveal"><span class="kicker">Vídeo</span><h2>XIULA — el vídeo de la comunitat</h2></div>
      <div class="reveal" style="position:relative;aspect-ratio:16/9;border-radius:var(--radi-lg);overflow:hidden;box-shadow:var(--sombra);">
        <iframe src="https://www.youtube.com/embed/8K7ncoG_RMM" title="XIULA - Associació Ubuntu"
          style="position:absolute;inset:0;width:100%%;height:100%%;border:0;"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen loading="lazy"></iframe>
      </div>
      <div class="mt-4 text-center reveal">
        <a class="btn btn-primary" href="https://www.youtube.com/results?search_query=associacio+ubuntu" rel="noopener">Veure més vídeos al nostre canal</a>
      </div>
    </div>
  </section>
</main>
""" % banner('Canal de YouTube', 'Els vídeos de la comunitat Ubuntu.',
             'assets/img/gallery/gallery-1.webp', 'Imatge d\'una activitat d\'Ubuntu', 'Canal de YouTube')
doc = head('Canal de YouTube | Associació Ubuntu', 'Vídeos de l\'Associació Educació i Lleure Ubuntu.',
           'canal-de-youtube.html') + header('canal-de-youtube.html') + YT + footer()
open(os.path.join(V2, 'canal-de-youtube.html'), 'w', encoding='utf-8', newline='\n').write(doc)
print('WROTE canal-de-youtube.html')

DOC = """
<main id="contingut">
%s
  <section class="section">
    <div class="container" style="max-width:820px;">
      <div class="section-head reveal"><span class="kicker">Institucional</span><h2>Documentació</h2>
      <p class="lead">Documents oficials de l'entitat. Per a qualsevol aclariment, escriu-nos.</p></div>
      <div class="info-card reveal"><h3>Estatuts</h3><p>Estatuts de l'Associació Educació i Lleure Ubuntu — disponibles prèvia sol·licitud a <a href="mailto:ubuntu@associacioubuntu.org">ubuntu@associacioubuntu.org</a>.</p></div>
      <div class="info-card mt-2 verd reveal"><h3>Polítiques internes</h3><p>Protocol d'acollida, política d'igualtat i protocol d'assetjament: demana'ls per correu.</p></div>
      <div class="info-card mt-2 blau reveal"><h3>Memòries i butlletins</h3><p>Consulta les <a href="memories-anuals.html">memòries anuals</a> i el <a href="butlleti-ubuntu.html">butlletí Ubuntu</a>.</p></div>
      <div class="mt-4 text-center reveal"><a class="btn btn-primary" href="mailto:ubuntu@associacioubuntu.org?subject=Documentació">Sol·licitar documentació</a></div>
    </div>
  </section>
</main>
""" % banner('Documentació', 'Documents institucionals i polítics de l\'entitat.',
             'assets/img/heroes/hero-4.webp', 'Equip d\'Ubuntu en una reunió de treball', 'Documentació')
doc = head('Documentació | Associació Ubuntu', 'Documents oficials de l\'Associació Educació i Lleure Ubuntu.',
           'documentacion.html') + header('documentacion.html') + DOC + footer()
open(os.path.join(V2, 'documentacion.html'), 'w', encoding='utf-8', newline='\n').write(doc)
print('WROTE documentacion.html')

# ---------- 7) páginas legales (texto extraído de v1) ----------
LEGAL = [
    ('politica-privacitat.html', 'Política de privacitat', 'Com tractem les teves dades personals.', 'Política de privacitat'),
    ('aviso-legal.html', 'Avís legal', 'Informació legal del lloc web.', 'Avís legal'),
    ('politica-cookies.html', 'Política de cookies', 'Quines cookies usa aquest lloc i per a què.', 'Política de cookies'),
    ('accessibilitat.html', 'Accessibilitat', 'El nostre compromís amb un web accessible.', 'Accessibilitat'),
]
for fname, title, lead, crumb in LEGAL:
    simple_page(fname, fname, '%s | Associació Ubuntu' % title, title, lead,
                'assets/img/heroes/hero-3.webp',
                'Famílies i participants d\'Ubuntu', crumb)

print('DONE EXTRA')
