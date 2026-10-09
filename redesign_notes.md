# Rediseño v2 — Associació Educació i Lleure Ubuntu

## Resum
Web estàtica, HTML / CSS / JS, **20 pàgines**, ràpida i sense dependències externes de Google Fonts (les tipografies són auto-hostades a `assets/fonts`). Tot el contingut textual i les imatges procedeixen del clon original i del FTP; no s'ha inventat text ni imatges.

**Arrel del projecte:** `C:\Users\NachoPC\HERMES\KlonKlonubuntu\v2`

## Pàgines (20)
- `index.html` — portada: hero, impacte (xifres amb comptador), programes en targetes, galeria, CTA final
- `qui-som.html` — història (2008 / 2012), missió, visió, 9 valors en acordeó, registre 49677
- `projectes.html` — presentació dels 4 projectes + xarxa i ACOL; CTAs a donacions / voluntariat
- `cau.html`, `centre-obert.html`, `trampoli.html`, `espiral.html` — contingut oficial de cada programa + CTA a dons i voluntariat
- `xarxa-comunitaria.html` — intro + quadrícula de 24 logos de la xarxa
- `acol-3.html` — ACOL / inserció laboral
- `voluntariat.html` — avantatges, perfil, formulari estàtic (maqueta)
- `dons.html` — comptes, Bizum 02962, beneficis fiscals, transparència
- `contacte.html` — fitxa, corbes, mapa OpenStreetMap + formulari estàtic
- `memories-anuals.html`, `butlleti-ubuntu.html`, `canal-de-youtube.html`, `documentacion.html`
- `politica-privacitat.html`, `politica-cookies.html`, `aviso-legal.html`, `accessibilitat.html`

## Sistema de disseny (`assets/`)
- `assets/css/styles.css` (~18 KB): variables CSS, reset base, botons (primary / secondary / green / ghost / lg), targetes, xifres, acordions, formularis, footer, animacions al fer scroll (IntersectionObserver + `prefers-reduced-motion`) i header fixe amb CTA.
- `assets/js/main.js` (~3,6 KB): menú mòbil accessible (aria-expanded, tancament per Escape / focus), revelead amb IO, comptadors animats, avís de cookies.
- `assets/fonts/fonts.css` + 6 TTF auto-hostades: Fraunces 600 / 700 + Inter 400 / 500 / 600 / 700. S'hi lliga en el `<head>` de totes les pàgines; el CSS apunta a `../assets/fonts/fonts.css` i les fonts apunten a carpeta local correcta.
- Imatges: `assets/img/` (91 WebP + logos / favicon / JPEG), tot el tractament defensat.

## CTA
- **“Dona ara”**: header fixe, hero, CTA final, footer. Enllaça a `dons.html`. Es podria connectar una passarel·la real (PayPal / Stripe) en l'implementació.
- **“Fes-te voluntari/a”**: header + hero + seccions + voluntariat; enllaça a `voluntariat.html`.
- CTAs contextuals: cada projecte acaba amb “Apoya …”.

## Validació local
- Totes les **20 pàgines responen HTTP 200**.
- Hi ha **91 imatges WebP** al disc i totes les referenciades es carreguen OK.
- El menú mòbil s'obre i tanca amb ARIA i el focus es manté correctament.

## Equip
- S'ha fet còpia de seguretat a `KlonKlonubuntu_backup_YYYYMMDD` abans de tocar les dades.

## Punts de visió en el futur
- Integració real dels formularis (back-end o mitjançant `mailto`) — actualment són maquetes estàtiques amb comentari visible.
- Mapa de Google (actualment s'utilitzen embeds externs d'OpenStreetMap).

## Nota
Web sense contes ni CTA de donació integrada fins a la integració d'una passarel·la real.

=======
## Documents del projecte

- `v2/redesign_notes.md` — aquest fitxer.
- `v2/index.html` … `v2/accessibilitat.html` — 20 pàgines.
- `v2/assets/fonts/` — 6 fonts TrueType auto-hostades (Fraunces 600/700, Inter 400/500/600/700).
- `v2/assets/css/styles.css` — sistema global de disseny.
- `v2/assets/js/main.js` — comportament del client.
- `v2/assets/img/` — 91 WebP + logos / favicon / JPEG.
