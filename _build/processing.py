import os, json, re, html as hm
from PIL import Image

CLONE = r'C:\Users\NachoPC\HERMES\KlonKlonubuntu'
FTP   = r'g:\_borrar_\ubuntu_cdmon\web\wp-content\uploads'
DST   = os.path.join(CLONE, 'v2', 'assets', 'img')
os.makedirs(DST, exist_ok=True)

manifest = {}

def resolve(rel):
    for base in (CLONE, FTP):
        p = os.path.join(base, rel)
        if os.path.isfile(p):
            return p
    return None

def convert(rel, out, max_w=900, quality=78, square=False, src=''):
    s = resolve(rel)
    if not s:
        print('MISS', rel)
        return None
    out_path = os.path.join(DST, out)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    im = Image.open(s)
    im.load()
    if square:
        w, h = im.size
        side = min(w, h)
        left, top = (w - side) // 2, max(0, (h - side) // 2)
        im = im.crop((left, top, left + side, top + side))
        max_w = min(max_w, 420)
    if im.mode in ('RGBA', 'LA', 'P'):
        im = im.convert('RGBA')
    else:
        im = im.convert('RGB')
    if im.width > max_w:
        im = im.resize((max_w, int(im.height * max_w / im.width)), Image.LANCZOS)
    im.save(out_path, 'WEBP', quality=quality, method=6)
    manifest[out] = list(Image.open(out_path).size)
    return out_path

# ---- heroes / banners (16:9-ish, se recortan por CSS con object-fit) ----
convert('uploads/2021/02/Foto-de-Sil-2.jpg', 'heroes/hero-1.webp', 1600, 78)
convert('uploads/2024/05/IMG-20240423-WA0029.jpg', 'heroes/hero-2.webp', 1600, 78)
convert('uploads/2022/08/UBUNTU-2022-Colonies.jpeg', 'heroes/hero-3.webp', 1600, 78)
convert('uploads/2024/05/IMG_20211019_181813579_HDR-1.jpg', 'heroes/hero-4.webp', 1600, 78)
convert('uploads/2024/05/IMG-20210615-WA0024.jpg', 'heroes/hero-5.webp', 1600, 78, src='ftp')

# ---- proyectos ----
convert('uploads/2020/12/cauPetita.jpg', 'projects/cau.webp', 900)
convert('uploads/2020/12/centre_obert_petita.jpeg', 'projects/centre-obert.webp', 900)
convert('uploads/2020/12/trampoli_petita.jpg', 'projects/trampoli.webp', 900)
convert('uploads/2020/12/espiral_petita.jpg', 'projects/espiral.webp', 900)
convert('uploads/2024/05/IMG_20211022_181832-768x346.jpg', 'projects/voluntariat.webp', 900)
convert('uploads/2024/05/Acol-2022-2023.jpg', 'projects/acol.webp', 900)
convert('uploads/2024/05/Ubuntu-Plaza.png', 'projects/xarxa.webp', 900)

# ---- cuadradas para tarjetas 5:6 ----
for name, rel in [('cau', 'uploads/2020/12/cauPetita.jpg'),
                  ('centre-obert', 'uploads/2020/12/centre_obert_petita.jpeg'),
                  ('trampoli', 'uploads/2020/12/trampoli_petita.jpg'),
                  ('espiral', 'uploads/2020/12/espiral_petita.jpg')]:
    convert(rel, 'sq/%s.webp' % name, 420, 80, square=True)

# ---- galería (Actividades / actividades destacadas, vía FTP) ----
gal = ['gola-story-port.jpg', 'gola-group-ice-cream.jpg', 'gola-power-out.jpg',
       'gola-mag1-cal-gamebooks.jpg', 'gola-two-waiting-meeting.jpg',
       'gola-man-jersey.jpg', 'pestsplanya-instrument.jpg']
for i, n in enumerate(gal, 1):
    convert('2021/02/' + n, 'gallery/gallery-%d.webp' % i, 1000, 76)

# ---- xarxa comunitaria: logos ----
for f in os.listdir(os.path.join(CLONE, 'uploads', '2024', '05')):
    if f.lower().endswith('.png') and 'Ubuntu-Plaza' not in f and 'Acol' not in f:
        slug = re.sub(r'[^a-z0-9]+', '-', f.rsplit('.', 1)[0].lower()).strip('-')
        convert('uploads/2024/05/' + f, 'xarxa/%s.webp' % slug, 240)

# ---- patrocinadores ----
sponsors = ['uploads/2020/12/ajuntament.png', 'uploads/2025/06/CaixaNew2.png',
            'uploads/2020/12/generalitat.png', 'uploads/2025/06/LGO-FundacionLaCaixaNew.png',
            'uploads/2021/01/Xiula-logo-invertit.png', 'uploads/2020/12/mafars.png',
            'uploads/2021/03/LOGO-FPM.png', 'uploads/2021/01/martiBonet.png',
            'uploads/2022/01/logo_ICMversio3claim.jpg', 'uploads/2022/03/RMC-Sport.png',
            'uploads/2023/05/LOGO-EspaiAuditiu2.png', 'uploads/2023/05/eTNIA-LOGO.png',
            'uploads/2023/05/Logo-AccionPlanetaria.png',
            'uploads/2023/05/Logo-Xamfra-Centre-de-Musica-i-Escena-del-Raval.png',
            'uploads/2023/05/alfasoni-logo-web.webp', 'uploads/2023/05/CapiBOla1.jpg',
            'uploads/2023/12/LOGOS-Harmonitzacio_SOC_GENE_FSE_HALG.png']
for rel in sponsors:
    f = os.path.basename(rel)
    slug = re.sub(r'[^a-z0-9]+', '-', f.rsplit('.', 1)[0].lower()).strip('-')
    convert(rel, 'sponsors/%s.webp' % slug, 280)

# ---- logo / favicon ----
convert('uploads/2024/06/logo_grande.webp', 'logo/logo-mono.webp', 320)
convert('uploads/2020/12/logo-300x300.jpg', 'logo/logo-square.jpg', 192)
convert('uploads/2020/12/logo-300x300.jpg', 'logo/logo-sq.webp', 200, square=True)
im = Image.open(os.path.join(CLONE, 'uploads', '2020', '12', 'logo-300x300.jpg'))
im.convert('RGB').resize((64, 64), Image.LANCZOS).save(os.path.join(DST, 'logo', 'favicon.png'))

# ---- portadas ( revista / memòries / butlletí ) ----
convert('uploads/2025/10/RevistaUbuntu1.png', 'memories/revista-1.webp', 900)
convert('uploads/2025/10/RevistaUbuntu2.png', 'memories/revista-2.webp', 900)
convert('uploads/2025/10/RevistaUbuntu3.png', 'memories/revista-3.webp', 900)
convert('uploads/2025/10/RevistaUbuntu4.png', 'memories/revista-4.webp', 900)
convert('uploads/2025/11/Portada-Memoria-Curta-2024-1024x768.png', 'memories/memoria-2024.webp', 900)
convert('uploads/2026/02/Memoria-Curta-2025-IMG-1024x768.png', 'memories/memoria-2025.webp', 900)
convert('uploads/2022/04/Boletin-Abril-2022.png', 'memories/butlleti-1.webp', 900)
convert('uploads/2022/03/Boletin-Marzo-2022.png', 'memories/butlleti-2.webp', 900)
convert('uploads/2021/09/Boletin-Febrero-2021.png', 'memories/butlleti-3.webp', 900)

# ---- ayuda / donativos ----
convert('uploads/2025/10/pay-screens.jpg', 'help/pay-screens.webp', 1200, 80, src='ftp')
convert('uploads/2022/10/WhatsApp-task-oct22-lg.jpg', 'help/whatsapp-lg.webp', 900, 80, src='ftp')

# ---- manifiesto de dimensiones ----
with open(os.path.join(CLONE, 'v2', '_build', 'img_manifest.json'), 'w', encoding='utf-8') as f:
    json.dump(manifest, f, indent=1, ensure_ascii=False)
print('OK', len(manifest), 'images')
