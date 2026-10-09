"""Ronda 2: completa imágenes faltantes (galería, donativos, portadas extras)."""
import os, json
from PIL import Image

CLONE = r'C:\Users\NachoPC\HERMES\KlonKlonubuntu'
FTP   = r'g:\_borrar_\ubuntu_cdmon\web\wp-content\uploads'
DST   = os.path.join(CLONE, 'v2', 'assets', 'img')
manifest = json.load(open(os.path.join(CLONE, 'v2', '_build', 'img_manifest.json'), encoding='utf-8'))

def resolve(rel):
    for base in (CLONE, FTP):
        p = os.path.join(base, rel)
        if os.path.isfile(p):
            return p
    return None

def convert(rel, out, max_w=900, quality=78, base_dir=None):
    if base_dir:
        p = os.path.normpath(os.path.join(base_dir, rel))
    else:
        p = resolve(rel)
    if not p or not os.path.isfile(p):
        print('MISS2', rel)
        return
    out_path = os.path.join(DST, out)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    im = Image.open(p)
    im.load()
    if im.mode in ('RGBA', 'LA', 'P'):
        im = im.convert('RGBA')
    else:
        im = im.convert('RGB')
    if im.width > max_w:
        im = im.resize((max_w, int(im.height * max_w / im.width)), Image.LANCZOS)
    im.save(out_path, 'WEBP', quality=quality, method=6)
    manifest[out] = list(Image.open(out_path).size)
    print('OK2', out, manifest[out])

g = os.path.join(FTP, '2021', '02')
# galería: filtrar solo las originales (sin sufijo -WxH)
real = [f for f in sorted(os.listdir(g)) if f.lower().endswith(('.jpg', '.jpeg', '.png'))
        and not (f.rsplit('.', 1)[0].split('-')[-1].replace('x', '').isdigit()
                 and 'x' in f.rsplit('.', 1)[0])]
i = 1
for f in real:
    if i > 10:
        break
    convert('2021/02/' + f, 'gallery/gallery-%d.webp' % i, 1000, 76, base_dir=FTP)
    i += 1

# donativos / ayudate: por si hay pantallas de bizum o imágenes en ajudes.html
import re
ah = open(os.path.join(CLONE, 'ajudes.html'), encoding='utf-8').read()
for m in sorted(set(re.findall(r'(?:uploads/[0-9]{4}/[0-9]{2}/[^"\s]+\.(?:jpg|jpeg|png|webp))', ah))):
    if 'logo' not in m.lower():
        f = os.path.basename(m)
        slug = 'help/' + re.sub(r'[^a-z0-9]+', '-', f.rsplit('.', 1)[0].lower()).strip('-')
        convert(m, slug + '.webp', 1200, 78)

# portada revista y memoria curta extras
convert('uploads/2026/03/Portada-Revista-Dic25.png', 'memories/revista-5.webp', 900, 78)
convert('uploads/2024/05/MEMORIA-2023-1024x767.png', 'memories/memoria-2023.webp', 900, 78)

# 2 imágenes más de actividad para donaciones / voluntariado
convert('uploads/2024/05/IMG-20210928-WA0042.jpg', 'projects/activitat-web.webp', 1200, 76, base_dir=FTP)
convert('uploads/2026/03/2IMGe_20211020_164711_446-1024x768.jpg', 'projects/activitat-2.webp', 1000, 76)

json.dump(manifest, open(os.path.join(CLONE, 'v2', '_build', 'img_manifest.json'), 'w', encoding='utf-8'),
          indent=1, ensure_ascii=False)
print('TOTAL', len(manifest))
