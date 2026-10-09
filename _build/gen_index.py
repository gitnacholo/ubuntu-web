# -*- coding: utf-8 -*-
"""Genera la homepage v2."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from layout import render

CONTENT = """
<main id="contingut">

  <!-- HERO -->
  <section class="hero" aria-label="Presentació">
    <div class="hero-bg"><img src="assets/img/heroes/hero-1.webp" alt="Infants i famílies de la Zona Nord durant una activitat d'oci educatiu d'Ubuntu" fetchpriority="high"></div>
    <div class="container">
      <div class="hero-content">
        <span class="kicker">Ciutat Meridiana · Zona Nord · Barcelona</span>
        <h1>Oci educatiu que transforma vides</h1>
        <p class="lead">Acompanyem infants, joves i famílies perquè ningú es quedi enrere.
        “Jo sóc perquè tu ets”: amb el teu suport, la tribu creix.</p>
        <div class="hero-ctas">
          <a class="btn btn-primary btn-lg" href="dons.html">Dona ara</a>
          <a class="btn btn-ghost btn-lg" href="voluntariat.html">Fes-te voluntari/a</a>
        </div>
        <p class="hero-note">Entitat sense ànim de lucre nº 49677 · Més de 15 anys al barri · <a href="projectes.html">Coneix els projectes</a></p>
      </div>
    </div>
  </section>

  <!-- CITA -->
  <section class="section" aria-label="Cita">
    <div class="container">
      <blockquote class="quote-block reveal">
        “Per educar un infant, cal tota una tribu.”
        <cite>Proverbi africà — el principi que ens inspira cada dia</cite>
      </blockquote>
    </div>
  </section>

  <!-- IMPACTE -->
  <section class="stats-band section" aria-label="El nostre impacte">
    <div class="container">
      <div class="section-head center reveal" style="color:#fff;">
        <span class="kicker">El nostre impacte</span>
        <h2 style="color:#fff;">Xifres que expliquen la tribu</h2>
      </div>
      <div class="stats-grid">
        <div class="stat reveal"><div class="num" data-count="50" data-suffix="+">0</div><div class="lbl">places d'oci educatiu i reforç escolar al Centre Obert</div></div>
        <div class="stat reveal d1"><div class="num" data-count="300" data-suffix="+">0</div><div class="lbl">famílies ateses pel projecte Trampolí</div></div>
        <div class="stat reveal d2"><div class="num" data-count="4" data-suffix="">0</div><div class="lbl">projectes oberts al barri: CAU, Centre Obert, Trampolí i Espiral</div></div>
        <div class="stat reveal d3"><div class="num" data-count="15" data-suffix="+">0</div><div class="lbl">anys creant vincles a Ciutat Meridiana</div></div>
      </div>
    </div>
  </section>

  <!-- QUE FEM: PROGRAMMES -->
  <section class="section" aria-label="Els nostres projectes">
    <div class="container">
      <div class="section-head center reveal">
        <span class="kicker">Què fem</span>
        <h2>Quatre projectes, una mateixa tribu</h2>
        <p class="lead">Educació en el temps lliure, acompanyament familiar, suport psicològic i xarxa comunitària a la Zona Nord de Nou Barris.</p>
      </div>
      <div class="grid-2">
        <article class="card reveal">
          <div class="card-media"><img src="assets/img/projects/cau.webp" alt="Infants participant en una activitats del CAU, espai de lleure educatiu dels dissabtes" loading="lazy"></div>
          <div class="card-body">
            <span class="card-tag">Dissabtes · 6 a 12 anys</span>
            <h3>CAU</h3>
            <p>Espai de lleure educatiu on infants i famílies participen d'activitats a través de la convivència, l'estima i l'acompanyament.</p>
            <a class="btn btn-secondary" href="cau.html">Descobreix el CAU</a>
          </div>
        </article>
        <article class="card reveal d1">
          <div class="card-media"><img src="assets/img/projects/centre-obert.webp" alt="Nens i adolescents fent reforç escolar al Centre Obert d'Ubuntu" loading="lazy"></div>
          <div class="card-body">
            <span class="card-tag">Cada tarda · 6 a 16 anys</span>
            <h3>Centre Obert</h3>
            <p>Lleure educatiu i reforç escolar: 50 places perquè infants i adolescents de la Zona Nord tinguin un espai pensat per a ells.</p>
            <a class="btn btn-secondary" href="centre-obert.html">Descobreix el Centre Obert</a>
          </div>
        </article>
        <article class="card reveal">
          <div class="card-media"><img src="assets/img/projects/trampoli.webp" alt="Sessió d'atenció psicològica i logopèdica del projecte Trampolí" loading="lazy"></div>
          <div class="card-body">
            <span class="card-tag">A l'escola pública · 3 a 16 anys</span>
            <h3>Trampolí</h3>
            <p>Atenció psicològica, psicopedagògica i logopèdica a l'abast de tothom, amb més de 300 famílies ateses en una dècada.</p>
            <a class="btn btn-secondary" href="trampoli.html">Descobreix Trampolí</a>
          </div>
        </article>
        <article class="card reveal d1">
          <div class="card-media"><img src="assets/img/projects/espiral.webp" alt="Grup de mares i bebès en un espai d'acompanyament familiar del projecte Espiral" loading="lazy"></div>
          <div class="card-body">
            <span class="card-tag">Famílies · 0 a 6 anys</span>
            <h3>Espiral</h3>
            <p>Projecte Teixim Vincles: espais d'acompanyament matern-infantil per potenciar el benestar de les famílies des de l'inici de la criança.</p>
            <a class="btn btn-secondary" href="espiral.html">Descobreix Espiral</a>
          </div>
        </article>
      </div>
      <p class="text-center mt-4 reveal"><a class="btn btn-green" href="projectes.html">Veure tots els projectes i la xarxa comunitària</a></p>
    </div>
  </section>

  <!-- QUI SOM teaser -->
  <section class="section bg-crema" aria-label="Qui som">
    <div class="container grid-2" style="align-items:center;">
      <div class="reveal">
        <span class="kicker" style="display:inline-block;font-size:.8rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--vermell);background:var(--vermell-suau);padding:.35em .9em;border-radius:999px;margin-bottom:var(--sp-2);">Qui som</span>
        <h2>Una associació nascuda del barri</h2>
        <p>L'any 2008 començàvem com un espai de lleure els dissabtes a la tarda a la Zona Nord de
        Ciutat Meridiana. Vuit anys més tard, veient les necessitats de les famílies del barri,
        naixia l'Associació Educació i Lleure Ubuntu: “Jo sóc perquè tu ets”.</p>
        <p>Som un equip de professionals i voluntàries amb vocació. És gràcies a la comunitat que
        Ubuntu creix any rere any i arriba a més infants i famílies.</p>
        <a class="btn btn-primary" href="qui-som.html">Coneix la nostra història</a>
      </div>
      <div class="reveal d1"><img src="assets/img/heroes/hero-2.webp" alt="Equip i voluntariat d'Ubuntu durant una sortida comunitària" loading="lazy" style="border-radius:var(--radi-lg);box-shadow:var(--sombra);"></div>
    </div>
  </section>

  <!-- GALERIA -->
  <section class="section" aria-label="Activitats destacades">
    <div class="container">
      <div class="section-head center reveal">
        <span class="kicker">Així som</span>
        <h2> Moments que expliquen qui som</h2>
      </div>
      <div class="masonry reveal">
        <div class="tall"><img src="assets/img/gallery/gallery-1.webp" alt="Activitat d'oci educatiu d'Ubuntu a la Zona Nord" loading="lazy"></div>
        <div><img src="assets/img/gallery/gallery-3.webp" alt="Infants gaudint d'una sortida d'entitat del barri" loading="lazy"></div>
        <div class="tall"><img src="assets/img/gallery/gallery-2.webp" alt="Moment de convivència entre participants i voluntariat" loading="lazy"></div>
        <div><img src="assets/img/gallery/gallery-4.webp" alt="Taller d'oci educatiu amb infants del barri" loading="lazy"></div>
        <div><img src="assets/img/gallery/gallery-5.webp" alt="Famílies participants en les activitats comunitàries" loading="lazy"></div>
      </div>
    </div>
  </section>

  <!-- CTA FINAL -->
  <section class="cta-final section" aria-label="Com ajudar">
    <div class="container">
      <div class="reveal">
        <span class="kicker" style="display:inline-block;font-size:.8rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#3A2400;background:var(--groc);padding:.35em .9em;border-radius:999px;margin-bottom:var(--sp-2);">Fes-la possible</span>
        <h2>La teva ajuda fa possible que seguim</h2>
        <p>Cada donatiu es converteix en oci educatiu, reforç escolar, atenció psicològica i acompanyament
        familiar. I cada voluntària que s'uneix fa la tribu més gran.</p>
        <div class="hero-ctas">
          <a class="btn btn-white btn-lg" href="dons.html">Dona ara</a>
          <a class="btn btn-ghost btn-lg" href="voluntariat.html">Uneix-te a l'equip</a>
        </div>
      </div>
    </div>
  </section>

</main>
"""

if __name__ == '__main__':
    render('index.html',
           'Ubuntu | Associació Educació i Lleure — Ciutat Meridiana',
           'Associació Educació i Lleure Ubuntu: oci educatiu, acompanyament familiar i comunitat a Ciutat Meridiana des de 2008. Dona o fes-te voluntari/ària.',
           CONTENT, active='index.html')
