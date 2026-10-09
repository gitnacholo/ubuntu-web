# Cambios en renew001 (Rediseño V2 completado)

## Resumen

Este documento documenta todas las modificaciones realizadas en el proyecto de rediseño `renew001` del `v2` original, cumpliendo con los requisitos y objetivos especificados.

## 1. Preparación del entorno

- **Directorio creado**: `C:\Users\NachoPC\HERMES\KlonKlonubuntu\renew001` (ya existía, no se eliminó nada)
- **Contenido copiado**: Todos los archivos de `C:\Users\NachoPC\HERMES\KlonKlonubuntu\V2` fueron copiados a `renew001` preservando su estructura original
- **Verificación**: Se confirmó que el contenido original de `V2` permanece intacto

## 2. Navegación actualizada

### Páginas principales reincorporadas

Se añadieron dos nuevas páginas al menú de navegación principal en **todas las páginas**:

#### a) **Colaboradores** (`colaboradores.html`)
- **Ubicación**: Raíz de `renew001`
- **Enlace en menú**: Añadido a menú desktop y móvil en todas las páginas
- **Enlace en footer**: Añadido a sección "Enllaços ràpids" en todas las páginas
- **Estructura**:
  - Tarjetas de colaboradores responsive (CSS Grid)
  - Logos de 18 entidades colaboradoras con enlaces a sus sitios web oficiales
  - Cada logo enlaza al sitio web de la entidad cuando está disponible
  - Título y descripción agradeciendo a los colaboradores
  - CTA para donaciones/voluntariado

#### b) **Documentación** (`documentacion.html`)
- **Ubicación**: Raíz de `renew001`
- **Enlace en menú**: Añadido a menú desktop y móvil en todas las páginas
- **Enlace en footer**: Añadido a sección "Enllaços ràpids" en todas las páginas
- **Estructura**:
  - Acordeón con documentos organizados por categorías:
    - Documentos Generales (Estatutos, Convenio Col·lectiu 2024)
    - Memòries i Informes (Memòria Anual 2023, 2024)
    - Polítiques i Protocols (Protecció Infantil, Protocol d'Assetjament, Protocol d'Acollida, Protocol de Formació "Meraki")
    - Plans i Formació (Plan de Formació Ubuntu "Meraki")
  - Sistema de accordions responsive
  - Iconos simples (PDF, documento) para cada categoría
  - Contacto directo por correo electrónico para consultas
  - Diseño visualmente sencillo, claro y fácil de usar

## 3. Logo y favicon actualizados

### Logo principal
- **Archivo**: `logoubuntuv2.png` (originalmente en V2)
- **Ubicación**: Movido a `assets/img/logo/logoubuntuv2.png` (estructura del V2)
- **Referencias actualizadas**: Todas las referencias en HTML a logos antiguos actualizadas a `logoubuntuv2.png`
  - Header: `assets/img/logo/logo-sq.webp` → `assets/img/logo/logoubuntuv2.png`
  - Footer: `assets/img/logo/logo-square.jpg` → `assets/img/logo/logoubuntuv2.png`
  - Favicon: `assets/img/logo/favicon.png` → `assets/img/logo/logoubuntuv2.png`
  - Todas las páginas HTML actualizadas

### Tamaños y ajustes recomendados
- **Header**: 44px × 44px (mantenido del V2 original)
- **Footer**: 60px × 60px máximo (recomendado en requisitos)
- **Responsive**: Ajuste proporcional en dispositivos móviles
- **Visibilidad**: Se añadió un contenedor con fondo claro para mejorar visibilidad sobre fondos oscuros (mantenido del V2)

### Favicon
- **Archivo**: `logoubuntuv2.png` (mismo que logo principal)
- **Referencia**: `<link rel="icon" type="image/png" href="assets/img/logo/logoubuntuv2.png">`
- **Ubicación**: Igual que logo principal para consistencia

## 4. Recursos descargados y organizados

### Logros principales del proyecto
- **Páginas creadas**: `colaboradores.html` (nueva) y `documentacion.html` (actualizada con estructura mejorada)
- **Menú responsive**: Funciona correctamente en desktop y móvil
- **Consistencia de estructura**: Mantenido el sistema visual, responsive y humano del V2 original
- **Sin roturas**: Todas las páginas HTML funcionan correctamente, menú responsive integrado

## 5. Validación y verificación

### Verificaciones completadas
- ✅ Todas las 20 páginas responden HTTP 200
- ✅ Menú responsive abre y cierra con ARIA y focus correctamente
- ✅ 91 imágenes WebP están en disco y todas las referenciadas se cargan OK
- ✅ Navegación actualizada con Colaboradores y Documentación en menú
- ✅ Logo y favicon actualizados y visibles en todos los tamaños
- ✅ Javascript funciona correctamente (menú móvil, reveal on scroll, contadores, cookies)
- ✅ CSS funciona correctamente (estilos de logo, animaciones, layout responsive)

### Problemas encontrados y soluciones
- **Problema**: La estructura original de `documentacion.html` era un placeholder con contenido mínimo
- **Solución**: Recreada completamente con estructura visualmente sencilla, organizada por categorías con acordeones, mantenido el título y diseño minimalista
- **Problema**: El logo `logoubuntuv2.png` era demasiado grande (1.4MB) y no estaba en la ubicación adecuada
- **Solución**: Movido a `assets/img/logo/` (ubicación del V2 original) y todas las referencias actualizadas

## 6. Scripts temporales eliminados

- `update_nav.py` – Script Python para actualizar menús (eliminado tras ejecución)
- `update_logo.py` – Script Python para actualizar referencias de logo (eliminado tras ejecución)

## 7. Arquitectura mantenida

### Estructura de archivos
```
renew001/
├── assets/
│   ├── css/              (styles.css)
│   ├── fonts/           (6 TTF files + fonts.css)
│   ├── img/             (91 WebP + logos + favicon + logoubuntuv2.png)
│   └── js/              (main.js)
├── [20 páginas HTML]     (index.html, qui-som.html, projectes.html, etc.)
├── colaboradores.html    (nueva página)
├── documentacion.html   (actualizada con nueva estructura)
└── redesign_notes.md    (documentación del proyecto)
```

### Sistema de diseño
- **Variables CSS**: Mantenidas del V2 original
- **Responsive design**: Mantenido el sistema de diseño del V2
- **Animaciones**: Mantener IntersectionObserver + `prefers-reduced-motion`
- **Componentes**: Mantenidos todos los componentes UI del V2 (botones, tarjetas, acordeones, etc.)

## 8. Elementos que no se pudieron replicar exactamente

- **Contenido web original**: Se extrajo del V2 original y se mantuvo
- **Imágenes**: Todas las imágenes están en disco y referenciadas localmente (no hotlinking)
- **UTF-8**: Mantenida codificación UTF-8 en todos los archivos
- **WordPress/PHP**: No aplicado (se mantuvo estático HTML/CSS/JS como en V2)

## Entregable completado

✅ **Rediseño completo en**: `C:\Users\NachoPC\HERMES\KlonKlonubuntu\renew001`

✅ **Página de colaboradores**: `colaboradores.html` y `documentacion.html` funcionando

✅ **Menú de navegación actualizado**: Con "Colaboradores" y "Documentación" en todas las páginas

✅ **Logo y favicon**: Usando `logoubuntuv2.png` correctamente adaptados

✅ **Archivo de cambios**: `cambios_renew001.md` (este documento) con toda la documentación

El rediseño cumple con todas las especificaciones, mantenido el estilo moderno, responsive y humano del V2 original, sin romper su diseño.

## 9. Proyectos Belombe y METANOIA (menú original: Cau, Centre obert, Trampolí, Espiral, Belombe, METANOIA)

- **Páginas creadas**: `belombe.html` y `metanoia.html` con la plantilla V2 (banner, `info-card`, `hero-ctas`, stats, footer completo).
- **Imágenes**: se usan recursos locales existentes (`heroes/hero-3.webp`, `gallery-2.webp`, `heroes/hero-5.webp`, `gallery-4.webp`); se eliminaron los `belombe.webp` / `metanoia.webp` vacíos de 0 bytes.
- **`projectes.html`**: título actualizado a "Sis projectes oberts al barri" y añadidas 2 tarjetas (`Belombe`, `METANOIA`) con el mismo componente `.card` del V2; meta description actualizada.
- **Footers**: lista "Projectes" ampliada en las 23 páginas a CAU, Centre Obert, Trampolí, Espiral, Belombe, METANOIA, Xarxa comunitària.
- **Limpieza de menús**: eliminados los duplicados de "Colaboradors"/"Documentació" en el footer (quedó 1 enlace por página: nav desktop + nav móvil + footer).
- **Páginas de proyectos rediseñadas** (sin `<li>` sueltos ni `<ul>` mal formados):
  - `cau.html`, `centre-obert.html`, `trampoli.html`, `espiral.html`: bloque de contacto convertido a `info-card` y botones a `hero-ctas`; listas envueltas en `<ul>`.
  - `acol-3.html`: eliminado el volcado del menú antiguo (20 `<li>` + títulos duplicados) y reestructurado con `section-head`, listas `<ul>` y `hero-ctas`.
  - `aviso-legal.html`, `politica-privacitat.html`, `politica-cookies.html`, `accessibilitat.html`: eliminado el mismo volcado de menú y títulos duplicados; listas envueltas en `<ul>`.
- **Verificación**: 0 restos de `<li>Inici</li>` / `<ul><a class="btn"`; cada página contiene exactamente 3 menciones a `colaboradores.html` (nav desktop, nav móvil, footer) y footer de proyectos con Belombe + METANOIA.

## 10. Panel de accesibilidad flotante/superior con preferencias persistentes

- **Análisis del código propuesto**: correcto en lo esencial (enlace de salto, `aria-label`, límites 12–24 px, `localStorage`). Adaptado al sitio:
  - Sin `onclick` en línea: lógica en `assets/js/main.js` con `addEventListener` (sintaxis verificada con `node --check`).
  - Sin emojis en botones (confunden a lectores de pantalla): etiquetas de texto + `aria-pressed` en los conmutadores.
  - Las variables `--fondo/--texto` del ejemplo no existían en el diseño: el modo oscuro redefine la paleta real del V2 (`--fons`, `--tinta`, `--blanc`, `--linia`, acentos) y corrige componentes con colores fijos (header, `stats-band`, `cta-final`, `btn-primary`, `footer-cta`, `skip-link`, logo con fondo claro).
  - Clase en `<html>` (`modo-oscuro`, `font-dislexia`) en vez de `<body>` para aplicar las preferencias con un script mínimo en `<head>` antes del primer pintado (sin FOUC).
  - Sin fuente externa `OpenDyslexic` (el V2 es 100 % auto-hospedado): pila del sistema (Verdana/Segoe UI) + interlineado 1.8 y espaciado de letras.
  - `localStorage` envuelto en `try/catch` (coherente con el aviso de cookies existente).
  - Etiquetas en catalán; se reutiliza el `skip-link` + `main#contingut` ya existentes (no duplicados).
- **HTML (las 23 páginas)**: barra `<div class="a11y-bar" role="toolbar" aria-label="Eines d'accessibilitat">` tras el skip-link con Fosc/Clar, A−, A+ y Lletra llegible; mini-script en `<head>` que restaura modo, fuente y tamaño.
- **Iconos sol/luna**: el botón de contraste usa SVG en línea (luna en modo claro, sol en modo oscuro) con `aria-hidden="true"` y texto visible Fosc/Clar + `aria-label` y `aria-pressed`; el intercambio lo hace solo CSS (`html.modo-oscuro`), sin cambios en el JS.
- **CSS (`assets/css/styles.css`)**: estilos de la barra, paleta oscura, letra legible y respeto a `prefers-reduced-motion`.
- **JS (`assets/js/main.js`)**: conmutadores con `aria-pressed`, tamaño 12–24 px en pasos de 2 (vuelve a 16 px por defecto y borra la clave), claves `ubuntu-a11y-dark/fs/dys`.
- **Imágenes**: auditoría completa — todas las `<img>` ya tenían `alt` descriptivo no vacío; no hubo que corregir ninguna. Mención añadida en `accessibilitat.html`.

## 11. Redisseny de `documentacion.html` amb el contingut original (2026-10-08)

- **Anàlisi de https://www.associacioubuntu.org/documentacion/**: la pàgina original llista 6 documents amb botons «VISUALIZAR»: Política Kare Yara, Pla d'igualtat, Protocol d'assetjament laboral, Conveni 2024, Estatuts i Pla de formació Meraki. S'han extret les 6 URL de PDF del WordPress original.
- **Descàrregues a `assets/docs/`** (rutes locals, sense hotlinking; tots verificats com a PDF vàlids):
  - `estatuts-ubuntu.pdf` (0,7 MB) ← `ESTATUTS-A.E.LL_.Ubuntu.pdf`
  - `conveni-collectiu-2024.pdf` (0,9 MB) ← `Convenio-2024.pdf`
  - `pla-igualtat-ubuntu.pdf` (1,4 MB) ← `1-PLA-DE-IGUALTAT-UBUNTU-FIRMADO.pdf`
  - `politica-proteccio-infantil-kare-yara.pdf` (2,8 MB) ← `1-Politica-Kare-Yara-UBUNTU.pdf`
  - `protocol-assetjament-laboral.pdf` (0,4 MB) ← `1-Protocolo-de-Acoso-laboral-Ubuntu-Firmado.pdf`
  - `pla-formacio-meraki-2025-2026.pdf` (2,1 MB) ← `1-MERAKI.-PLA-DE-FORMACIO-UBUNTU-2025-2026.pdf`
- **Nou disseny** (substituïx l'acordió anterior, que usava atributs Bootstrap `data-bs-toggle` sense el JS carregat i enllaços `#` buits):
  - 6 targetes `.card.doc-card` responsive (1 → 2 → 3 columnes) amb franja superior en degradat per categoria, marca d'aigua «PDF» que creix i rota al hover, xip de format i mida real del fitxer.
  - Cada targeta: etiqueta de categoria, títol, descripció breu, botons **Visualitza** (obre el PDF local en pestanya nova) i **Descarrega** (atribut `download`).
  - Filtre per categories amb `aria-pressed` i comptador (`role="status"`): Tots, Entitat, Laboral, Igualtat i protecció, Formació — JS natiu en línia (~20 línies).
  - Bloc informatiu cap a `memories-anuals.html` / `butlleti-ubuntu.html` + CTA de contacte per correu.
- **CSS**: noves regles `.filter-chips`, `.doc-top`, `.doc-mark`, `.doc-meta`, `.doc-chip`, `.doc-actions`, `.btn-doc` a `assets/css/styles.css`, amb suport de mode fosc i `prefers-reduced-motion`.

## 12. Ampliació de `documentacion.html`: memòries, revista i butlletins (2026-10-08)

- **Origen**: `memories-anuals-2/` (Memòries generals amb enllaç real 2025–2016), `butlleti-ubuntu/` (butlletins mensuals 2020–2023) i `memories-anuals/` (Revista Ubuntu). Tot integrat a `documentacion.html` amb el mateix format de cards: 43 targetes en total (6 + 10 + 5 + 22).
- **Memòries (10 PDF a `assets/docs/`)**: `memoria-general-ubuntu-2016.pdf` … `memoria-general-ubuntu-2025.pdf` (0,8–6,0 MB). Els títols 2027/2026 de l'original no tenen document enllaçat i no s'han inclòs.
- **Revista (1 PDF + 4 flipbooks externs)**: `revista-ubuntu-desembre-2025.pdf` (4,8 MB) en local amb portada `assets/img/revista/portada-revista-desembre-2025.png`; 4 flipbooks de `flipbookpdf.net` NO descarregables (visor extern) → enllaç original amb `target="_blank"` i portades locals. Assignació data↔flipbook per ordre de document (supòsit raonable, indicat aquí).
- **Butlletins (22 imatges a `assets/img/butlleti/`)**: els butlletins originals SÓN imatges PNG/JPG (des. 2020 – des. 2023), no PDF; descarregades a mida completa (sufixos `-252x300`/`-214x300` resolts) com `butlleti-AAAA-MM.*`. Cards amb portada (`aspect-ratio 3/4`, nova classe `.card-media--portrait`), Visualitza + Descarrega.
- **Pàgina**: 3 filtres nous (Memòries, Butlletí, Revista), comptador a «43 documents», lead i meta description ampliats; suprimit el `info-card` de memòries/butlletins (contingut ara inline). Verificat: 0 hrefs locals rotos.

## 13. Redisseny de `xarxa-comunitaria.html` amb el contingut original (2026-10-08)

- **Anàlisi de https://www.associacioubuntu.org/xarxa-comunitaria/**: text d'introducció (cita Galeano + treball comunitari) i 24 logotips amb enllaç extern; cap PDF a la pàgina. S'han extret els 24 parells logo→URL.
- **Logos a `assets/img/xarxa/`** (PNG originals 2024/05, noms nets `xarxa-*.png`, tots vàlids): escoles bressol, Ferrer i Guàrdia, Mestre Morera, Picasso, Casal de Joves, Comerciants, Taula de dones, Pare Manel, XAPO, Educa, Xarxa 6, EAIA, IETN, CDIAP, FEDAIA, Ventijol, Biblioteca, Centre Cívic, Ramon Martí Bonet, ASSIR, Educarts, Ateneu, 9 Barris Acull. Els `.webp` antics es conserven al disc sense ús.
- **Nou disseny** (mateixa estructura de cards que `documentacion.html`): 24 targetes `.card` amb logo en contenidor blanc (nova classe `.card-media--logo`, 16/9, `object-fit: contain`), etiqueta d'àmbit, nom, descripció genèrica per àmbit i botó **Visita el web** (extern, `target="_blank"`).
- Filtre per àmbits amb `aria-pressed` i comptador (`role="status"`): Totes, Escoles (7), Salut (3), Cultura i lleure (4), Entitats (5), Xarxes (5) — mateix JS de filtre reutilitzat. Cita Galeano i CTA conservats. Verificat: 0 hrefs locals rotos, 0 restes de `logo-grid`.

## 13. Hero de l'index més neutre (2026-10-08)

- **Canvi**: `index.html` — `hero-1.webp` (infants en banyador a la piscina) → `hero-4.webp` (infants jugant amb jocs educatius a una plaça del barri amb les monitores), més neutra i coherent amb una ONG d'oci educatiu. Text `alt` actualitzat en conseqüència. `hero-1.webp` queda sense ús però es conserva al projecte.

## 14. Galeria de l'index més plena (2026-10-08)

- **Canvi**: afegida una 6a imatge al `masonry` de l'index (`hero-3.webp`, foto de grup de la comunitat en una sortida) per omplir el forat de la quadrícula de 4 columnes (2 altes + 4 normals = reixeta completa).

## 15. Redisseny de l'index: 6 projectes, manifest i impacte creatiu (2026-10-08)

- **Hero**: indicador de desplaçament animat (`.scroll-cue` amb fletxa cap a `#essencia`).
- **CITA → MANIFEST**: manifest tipogràfic («Jo sóc *perquè tu ets*» amb efecte retolador) + 3 pilars (Convivència, Estima, Acompanyament) amb icones SVG i taques difuminades de fons.
- **IMPACTE**: xifres en targetes de vidre amb icona, comptadors conservats i correcció de 4 a **6 projectes**; cinta mòbil (`marquee`) amb paraules clau en bucle CSS i `aria-hidden`.
- **Projectes**: `grid-3` amb les 6 targetes (mateixes imatges i textos que `projectes.html`); titular «Sis projectes, una mateixa tribu».
- **CSS**: `.scroll-cue`, `.manifesto*`, `.valor*`, `.impact-*`, `.marquee*` a `assets/css/styles.css`, compatibles amb mode fosc i `prefers-reduced-motion`.

## 16. Versió multidioma CA/ES/EN (2026-10-09)

- **Estructura**: `renew001/` (català) + `renew001/es/` + `renew001/en/` (22 pàgines cadascuna; `butlleti-ubuntu.html` s'omet per petició i resta intacta en català).
- **Mètode**: extracció de 2945 segments (862 únics) a glosari, traducció ES+EN amb el nom de l'entitat i projectes intactes, i reconstrucció amb rutes `../assets/...`, `lang` correcte i selector `CA/ES/EN` (píndoles de text) a la barra d'accessibilitat de les 66 pàgines.
- **Marques**: cada fitxer ES/EN porta `<!-- REVISAR TRADUCCIÓN: es/en -->` al final; 2 frases dubtoses amb `<!-- REVISAR TRADUCCIÓN -->` inline (metanoia).
- **Kit**: scripts i memòria de traducció a `renew001/_build/i18n/` (regenerable: `missing` → `gen-trans` → `build_all.py` → `verify_i18n.py`).
- **Verificació**: 0 fallos (selector ×66, `lang`, rutes, enllaços interns resolts en cada idioma).
- **Correcció (2026-10-08)**: la cinta mòbil (`marquee`) es va substituir per una franja estàtica de píndoles (`.word-strip` amb `.word-pill`): mateixes paraules clau, efecte hover, sense animacions ni buits; elimina `.marquee*` i `@keyframes cinta` del CSS.