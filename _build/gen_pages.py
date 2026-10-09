# -*- coding: utf-8 -*-
"""Genera les pàgines interiors v2: qui-som, projectes, voluntariat, dons, contacte."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from layout import render

def banner(h1, lead, img, alt, crumb, crumb_href='index.html'):
    return """
<section class="page-banner" aria-label="%s">
  <div class="hero-bg"><img src="%s" alt="%s" loading="lazy"></div>
  <div class="container">
    <div class="hero-content">
      <h1>%s</h1>
      <p class="lead">%s</p>
      <nav class="breadcrumb" aria-label="Migues de pa"><a href="%s">Inici</a> / %s</nav>
    </div>
  </div>
</section>""" % (h1, img, alt, h1, lead, crumb_href, crumb)

# ============================================================ QUI SOM
QUI_SOM = """
<main id="contingut">
%s
  <section class="section">
    <div class="container">
      <div class="grid-2" style="align-items:center;">
        <div class="reveal">
          <span class="kicker" style="display:inline-block;font-size:.8rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--vermell);background:var(--vermell-suau);padding:.35em .9em;border-radius:999px;margin-bottom:var(--sp-2);">La filosofia</span>
          <h2>“Jo sóc perquè tu ets”</h2>
          <p>Ubuntu és una expressió africana que significa <em>“Jo sóc el que sóc per allò que tots som”</em>.
          Tots i totes som importants, som part de la tribu, i ens acceptem tal com som, des de la
          convivència amb respecte i esperit crític. Compartir i crear vincle afavoreix la transformació
          individual i col·lectiva.</p>
          <p>L'any 2008 vam començar com un espai de lleure els dissabtes a la tarda a la Zona Nord de
          Ciutat Meridiana: el <strong>Cau de la Ubuntu</strong>. El 2012, coneixent de prop les necessitats
          del barri (un gran nombre de famílies en situació de vulnerabilitat), vam construir
          l'<strong>Associació Educació i Lleure Ubuntu</strong> per portar a terme diferents projectes
          amb aquesta filosofia.</p>
        </div>
        <div class="reveal d1"><img src="assets/img/heroes/hero-4.webp" alt="Voluntariat i infants d'Ubuntu compartint una activitat al barri" loading="lazy" style="border-radius:var(--radi-lg);box-shadow:var(--sombra);"></div>
      </div>
    </div>
  </section>

  <section class="section bg-verd" aria-label="Missió, visió i valors">
    <div class="container">
      <div class="section-head center reveal">
        <span class="kicker verd">Ideari</span>
        <h2>Missió, visió i valors</h2>
      </div>
      <div class="grid-3">
        <div class="info-card reveal">
          <h3>Missió</h3>
          <p>L'educació com a eix: acompanyament als aprenentatges de la quotidianitat i dels processos
          de vida. Promovem, a través de l'educació i el lleure, el desenvolupament integral de les
          persones de la comunitat Ubuntu i de les famílies de la Zona Nord de Barcelona, generant
          noves oportunitats.</p>
        </div>
        <div class="info-card verd reveal d1">
          <h3>Visió</h3>
          <p>Ser reconeguda com una entitat responsable i compromesa amb la justícia social i el
          desenvolupament humà, prioritzant la defensa dels drets de la infància i la joventut.
          Una associació dinàmica i participativa, amb actuació local i capacitat d'adaptació.</p>
        </div>
        <div class="info-card blau reveal d2">
          <h3>Valors</h3>
          <p><strong>Unitat · Diversitat · Compromís · Qualitat · Confiança · Transparència ·
          Voluntariat · Justícia · Participació</strong>. Nou valors que guien cada projecte i cada
          relació dins la comunitat.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section" aria-label="Valors en detall">
    <div class="container" style="max-width:860px;">
      <div class="section-head reveal">
        <span class="kicker">Transparència</span>
        <h2>Els nou valors, un a un</h2>
      </div>
      <details class="accordion reveal"><summary>Unitat</summary><div class="acc-body">Creiem en el treball en equip de manera interna i en la col·laboració externa amb altres organitzacions i institucions, per potenciar sinergies i millorar tots els aspectes de la nostra feina.</div></details>
      <details class="accordion reveal"><summary>Diversitat</summary><div class="acc-body">Fomentem una cultura on totes les persones són tractades de manera justa i respectuosa, amb el mateix accés a oportunitats i recursos.</div></details>
      <details class="accordion reveal"><summary>Compromís</summary><div class="acc-body">Ens comprometem íntegrament amb la nostra missió i visió, recolzant-nos en la integritat com a principi essencial de les nostres accions per contribuir a la transformació social.</div></details>
      <details class="accordion reveal"><summary>Qualitat</summary><div class="acc-body">Definim criteris de qualitat a través de l'anàlisi de cada projecte educatiu i de lleure, amb indicadors i objectius clarament avaluables.</div></details>
      <details class="accordion reveal"><summary>Confiança</summary><div class="acc-body">Facilitem la seguretat, naturalitat i familiaritat amb què tractem els integrants de la comunitat Ubuntu, perquè es puguin recolzar en el nostre equip.</div></details>
      <details class="accordion reveal"><summary>Transparència</summary><div class="acc-body">Basem la nostra tasca en l'honestedat, la mútua responsabilitat i el màxim accés a la informació: rendició de comptes social i econòmica davant socis, col·laboradors, donants i la societat.</div></details>
      <details class="accordion reveal"><summary>Voluntariat</summary><div class="acc-body">Proporcionem els mitjans necessaris per a la implicació de persones que contribueixin personal, professional i socialment a l'enriquiment educatiu dels projectes.</div></details>
      <details class="accordion reveal"><summary>Justícia</summary><div class="acc-body">Considerem la llibertat individual, la interdependència i la igualtat entre les persones i institucions perquè cada individu obtingui el que li correspon.</div></details>
      <details class="accordion reveal"><summary>Participació</summary><div class="acc-body">Fomentem els principis democràtics i participatius com a mitjans necessaris per a la transformació social.</div></details>
      <div class="mt-4 info-card reveal">
        <h3>Dades d'interès públic</h3>
        <p>Entitat sense ànim de lucre inscrita al registre amb el <strong>nº 49677</strong>, declarada
        d'utilitat pública i acollida als beneficis fiscals de la <strong>Llei 49/2002</strong>.
        Consulta les <a href="memories-anuals.html">memòries anuals</a> i la documentació institucional.</p>
      </div>
      <div class="mt-4 reveal">
        <a class="btn btn-primary" href="dons.html">Apoya l'equip amb un donatiu</a>
        <a class="btn btn-secondary" href="voluntariat.html" style="margin-left:.5rem;">Fes-te voluntari/a</a>
      </div>
    </div>
  </section>
</main>
""" % banner('Qui som',
             'Més de 15 anys acompanyant la infància i les famílies de la Zona Nord de Barcelona.',
             'assets/img/heroes/hero-2.webp',
             'Voluntariat i famílies d\'Ubuntu en una activitat comunitària',
             'Qui som')

# ============================================================ PROJECTES
PROJECTES = """
<main id="contingut">
%s
  <section class="section">
    <div class="container">
      <div class="section-head reveal">
        <span class="kicker">Projectes</span>
        <h2>Quatre projectes oberts al barri</h2>
        <p class="lead">Del temps lliure al suport psicològic i acompanyament de les famílies: una xarxa d'actuacions per a infants, joves i famílies de 0 a 99 anys.</p>
      </div>
      <div class="grid-2">
        <article class="card reveal">
          <div class="card-media"><img src="assets/img/projects/cau.webp" alt="Activitats del CAU, espai de lleure educatiu dels dissabtes" loading="lazy"></div>
          <div class="card-body">
            <span class="card-tag">Dissabtes 16h–18:30h · 6 a 12 anys</span>
            <h3>CAU</h3>
            <p>Espai de lleure educatiu a l'Escola Ferrer i Guàrdia on infants i famílies participen
            d'activitats a través de la convivència, l'estima i l'acompanyament.</p>
            <a class="btn btn-secondary" href="cau.html">Llegir més</a>
          </div>
        </article>
        <article class="card reveal d1">
          <div class="card-media"><img src="assets/img/projects/centre-obert.webp" alt="Reforç escolar al Centre Obert" loading="lazy"></div>
          <div class="card-body">
            <span class="card-tag">Cada tarda · 6 a 16 anys</span>
            <h3>Centre Obert</h3>
            <p>Lleure educatiu i reforç escolar a la Zona Nord: 50 places en cinc grups d'edat amb
            educadora-referent, suport de voluntariat i treball intergeneracional.</p>
            <a class="btn btn-secondary" href="centre-obert.html">Llegir més</a>
          </div>
        </article>
        <article class="card reveal">
          <div class="card-media"><img src="assets/img/projects/trampoli.webp" alt="Atenció psicològica i logopèdica del projecte Trampolí" loading="lazy"></div>
          <div class="card-body">
            <span class="card-tag">A l'escola pública · 3 a 16 anys</span>
            <h3>Trampolí</h3>
            <p>Intervenció psicològica, psicopedagògica i logopèdica a escoles de Ciutat Meridiana,
            Torre Baró i Vallbona. Més de 300 famílies ateses en més d'una dècada.</p>
            <a class="btn btn-secondary" href="trampoli.html">Llegir més</a>
          </div>
        </article>
        <article class="card reveal d1">
          <div class="card-media"><img src="assets/img/projects/espiral.webp" alt="Espai d'acompanyament matern-infantil del projecte Espiral" loading="lazy"></div>
          <div class="card-body">
            <span class="card-tag">Famílies · 0 a 6 anys</span>
            <h3>Espiral</h3>
            <p>Projecte Teixim Vincles: espais d'acompanyament matern-infantil, grups de parla,
            tallers i suport en el postpart, amb el suport de Pla de Barris.</p>
            <a class="btn btn-secondary" href="espiral.html">Llegir més</a>
          </div>
        </article>
      </div>
    </div>
  </section>

  <section class="section bg-blau" aria-label="Altres programes">
    <div class="container">
      <div class="section-head reveal">
        <span class="kicker blau">Més programes</span>
        <h2>Xarxa comunitària i inserció laboral</h2>
      </div>
      <div class="grid-2">
        <div class="info-card reveal">
          <h3>Xarxa comunitària</h3>
          <p>Treballem de manera coordinada amb entitats, recursos i equipaments del barri i de la
          ciutat: escoles, casals, biblioteca, centres cívics i serveis socials.
          <a href="xarxa-comunitaria.html">Descobreix la xarxa</a></p>
        </div>
        <div class="info-card blau reveal d1">
          <h3>ACOL · Treball i formació</h3>
          <p>Programa d'inserció laboral per a persones migrades en situació administrativa
          irregular: assessorament jurídic, formació i mediació amb empreses.
          <a href="acol-3.html">Saber-ne més</a></p>
        </div>
      </div>
      <div class="mt-4 reveal">
        <a class="btn btn-primary" href="dons.html">Apoya aquests projectes amb una donació</a>
        <a class="btn btn-secondary" href="voluntariat.html" style="margin-left:.5rem;">Col·labora com a voluntari/a</a>
      </div>
    </div>
  </section>
</main>
""" % banner('Projectes',
             'Oci educatiu, acompanyament familiar, salut comunitària i xarxa al barri.',
             'assets/img/projects/activitat-2.webp',
             'Activitat educativa d\'Ubuntu amb infants del barri',
             'Projectes', crumb_href='index.html')

# ============================================================ VOLUNTARIAT
VOLUNTARIAT = """
<main id="contingut">
%s
  <section class="section">
    <div class="container grid-2" style="align-items:center;">
      <div class="reveal">
        <span class="kicker" style="display:inline-block;font-size:.8rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--vermell);background:var(--vermell-suau);padding:.35em .9em;border-radius:999px;margin-bottom:var(--sp-2);">Voluntariat</span>
        <h2>Fes créixer la tribu</h2>
        <p>El voluntariat és el <strong>motor de l'Associació</strong>. Necessitem persones compromeses
        per acompanyar els projectes: CAU, Centre Obert, Trampolí i Espiral. Si tens ganes d'aportar
        el teu temps i les teves habilitats, ens encantaria conèixer-te.</p>
        <p>També oferim <strong>places de pràctiques</strong> per a estudiants de treball social,
        educació social, psicologia, logopèdia, magisteri i altres graus relacionats.</p>
      </div>
      <div class="reveal d1"><img src="assets/img/projects/voluntariat.webp" alt="Voluntariat d'Ubuntu durant una sessió amb infants" loading="lazy" style="border-radius:var(--radi-lg);box-shadow:var(--sombra);"></div>
    </div>
  </section>

  <section class="section bg-crema" aria-label="Què oferim">
    <div class="container">
      <div class="section-head center reveal">
        <span class="kicker">Què oferim</span>
        <h2>Un entorn per aprendre i contribuir</h2>
      </div>
      <div class="grid-3">
        <div class="info-card reveal"><h3>Acompanyament</h3><p>Acompanyament i supervisió professional contínua durant tota la teva col·laboració.</p></div>
        <div class="info-card verd reveal d1"><h3>Formació</h3><p>Formació específica en els àmbits d'actuació dels projectes, amb experts de cada disciplina.</p></div>
        <div class="info-card blau reveal d2"><h3>Certificat</h3><p>Certificat de pràctiques o voluntariat i experiència real en entorns educatius i socials.</p></div>
      </div>
      <div class="grid-3 mt-3">
        <div class="info-card reveal"><h3>Equip</h3><p>Participació en un equip multidisciplinari amb vocació i implicació.</p></div>
        <div class="info-card verd reveal d1"><h3>Perfil buscat</h3><p>Sensibilitat cap a la injustícia social, compromís, treball en equip i disponibilitat de 3–4 hores setmanals.</p></div>
        <div class="info-card blau reveal d2"><h3>Pràctiques</h3><p>Convenis amb universitats per a estudiants de graus socials i educatius.</p></div>
      </div>
    </div>
  </section>

  <section class="section" aria-label="Formulari de voluntariat">
    <div class="container" style="max-width:760px;">
      <div class="section-head center reveal">
        <span class="kicker">Uneix-t'hi</span>
        <h2>Escriu-nos i ens coneixem</h2>
      </div>
      <!-- MAQUETA ESTÀTICA: aquest formulari no envia dades. Contacte real: ubuntu@associacioubuntu.org -->
      <form class="form-grid reveal" onsubmit="return false;" aria-describedby="vol-note">
        <div class="field"><label for="v-nom">Nom i cognoms</label><input id="v-nom" name="nom" type="text" autocomplete="name" required></div>
        <div class="field"><label for="v-mail">Correu electrònic</label><input id="v-mail" name="email" type="email" autocomplete="email" required></div>
        <div class="field"><label for="v-tel">Telèfon</label><input id="v-tel" name="telefon" type="tel" autocomplete="tel"></div>
        <div class="field">
          <label for="v-projecte">Projecte on vols col·laborar</label>
          <select id="v-projecte" name="projecte">
            <option>CAU (dissabtes)</option>
            <option>Centre Obert (tardes)</option>
            <option>Trampolí (escoles)</option>
            <option>Espiral (famílies 0-6)</option>
            <option>Pràctiques acadèmiques</option>
            <option>Encara no ho sé</option>
          </select>
        </div>
        <div class="field full"><label for="v-msg">Presenta't breument</label><textarea id="v-msg" name="missatge" placeholder="Qui ets, què t'interessa i quina disponibilitat tens…"></textarea></div>
        <div class="full">
          <button class="btn btn-primary btn-lg" type="submit">Enviar sol·licitud</button>
          <p class="mock-note mt-2" id="vol-note">Maqueta visual: aquest formulari no envia dades en la versió estàtica.
          Escriu-nos a <a href="mailto:ubuntu@associacioubuntu.org">ubuntu@associacioubuntu.org</a> o truca'ns al
          <a href="tel:+34620015846">+34 620 01 58 46</a>.</p>
        </div>
      </form>
    </div>
  </section>
</main>
""" % banner('Voluntariat i pràctiques',
             'Aporta el teu temps i les teves habilitats: la tribu t\'està esperant.',
             'assets/img/projects/voluntariat.webp',
             'Voluntariat d\'Ubuntu acompanyant infants en una activitat',
             'Voluntariat')

# ============================================================ DONACIONS
DONS = """
<main id="contingut">
%s
  <section class="section">
    <div class="container">
      <div class="section-head center reveal">
        <span class="kicker">Donacions</span>
        <h2>Cada euro es transforma en oportunitats</h2>
        <p class="lead">Amb el teu donatiu fem possible l'oci educatiu dels dissabtes, el reforç escolar de cada tarda,
        l'atenció psicològica a les escoles i l'acompanyament de les famílies amb nadons.</p>
      </div>
      <div class="grid-2" style="align-items:center;">
        <div class="reveal">
          <div class="info-card" style="border-left-color:var(--groc);">
            <h3>Per transferència bancària</h3>
            <p style="font-size:1.15rem;"><strong>ES37 2100 3307 4921 0089 2027</strong><br>
            <span style="color:var(--tinta-2);">CaixaBank · Associació Educació i Lleure Ubuntu</span></p>
          </div>
          <div class="info-card mt-2" style="border-left-color:var(--groc);">
            <h3>Amb Bizum</h3>
            <p>Obre Bizum → «Fer donatiu» → escriu el codi <strong>02962</strong> → indica l'import → confirma.
            El codi identifica l'Associació Ubuntu com a destinatària.</p>
          </div>
          <div class="info-card mt-2 verd">
            <h3>Fes-te soci o sòcia</h3>
            <p>Amb la teva quota (la decides tu; referència: <strong>50 € anuals</strong>) col·labores amb
            els projectes, reps el butlletí i participes de l'Assemblea General.
            Escriu-nos per donar-te d'alta.</p>
          </div>
        </div>
        <div class="reveal d1">
          <img src="assets/img/help/2024-11-18-10-22-48-donaciones-y-desgrave.webp" alt="Infografia de donacions i desgravacions fiscals d'Ubuntu" loading="lazy" style="border-radius:var(--radi-lg);box-shadow:var(--sombra);">
          <p class="form-note text-center mt-2">Les donacions es desgraven: fins al 80%% de l'IRPF en els primers 150 €
          i deduccions de fins al 45%% amb donacions recurrents (Llei 49/2002, entitat d'utilitat pública).</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section bg-terrat" aria-label="Altres maneres d'ajudar">
    <div class="container">
      <div class="section-head center reveal">
        <span class="kicker">Més maneres d'ajudar</span>
        <h2>No tot és diners</h2>
      </div>
      <div class="grid-3">
        <div class="info-card reveal"><h3>Donacions en espècie</h3><p>Recollim joguines, roba, menjar i productes de la llar per a les famílies. Posa't en contacte i et passem a buscar.</p></div>
        <div class="info-card verd reveal d1"><h3>Voluntariat</h3><p>El teu temps setmanal val or als projectes. <a href="voluntariat.html">Fes-te voluntari/a</a>.</p></div>
        <div class="info-card blau reveal d2"><h3>Difusió</h3><p>Comparteix els nostres projectes a les xarxes i al teu entorn. Fer-nos conèixer també és ajudar.</p></div>
      </div>
      <div class="mt-4 text-center reveal">
        <a class="btn btn-primary btn-lg" href="mailto:ubuntu@associacioubuntu.org?subject=Donatiu">Vull fer un donatiu</a>
      </div>
    </div>
  </section>

  <section class="section" aria-label="Transparència">
    <div class="container" style="max-width:860px;">
      <div class="section-head reveal">
        <span class="kicker">Transparència</span>
        <h2>On van els teus diners</h2>
        <p>Entitat sense ànim de lucre <strong>nº 49677</strong>, declarada d'utilitat pública (Llei 49/2002).
        Rendim comptes cada any: consulta les <a href="memories-anuals.html">memòries anuals</a>,
        el <a href="butlleti-ubuntu.html">butlletí</a> i la <a href="documentacion.html">documentació</a>.</p>
      </div>
    </div>
  </section>
</main>
""" % banner('Dona a Ubuntu',
             'La teva aportació fa possible el treball amb infants, joves i famílies de la Zona Nord.',
             'assets/img/heroes/hero-5.webp',
             'Infants d\'Ubuntu durant una colònia d\'estiu',
             'Donacions')

# ============================================================ CONTACTE
CONTACTE = """
<main id="contingut">
%s
  <section class="section">
    <div class="container">
      <div class="grid-2" style="align-items:start;">
        <div class="reveal">
          <span class="kicker" style="display:inline-block;font-size:.8rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--vermell);background:var(--vermell-suau);padding:.35em .9em;border-radius:999px;margin-bottom:var(--sp-2);">Contacte</span>
          <h2>Parlem?</h2>
          <!-- MAQUETA ESTÀTICA: aquest formulari no envia dades. -->
          <form class="form-grid" onsubmit="return false;" aria-describedby="ct-note">
            <div class="field"><label for="c-nom">Nom</label><input id="c-nom" name="nom" type="text" autocomplete="name" required></div>
            <div class="field"><label for="c-mail">Correu electrònic</label><input id="c-mail" name="email" type="email" autocomplete="email" required></div>
            <div class="field full"><label for="c-assumpte">Assumpte</label>
              <select id="c-assumpte" name="assumpte">
                <option>Informació general</option>
                <option>Vull fer un donatiu</option>
                <option>Vull fer de voluntari/ària</option>
                <option>Pràctiques acadèmiques</option>
                <option>Famílies: inscripcions</option>
              </select>
            </div>
            <div class="field full"><label for="c-msg">Missatge</label><textarea id="c-msg" name="missatge" required></textarea></div>
            <div class="full">
              <button class="btn btn-primary btn-lg" type="submit">Enviar missatge</button>
              <p class="mock-note mt-2" id="ct-note">Maqueta visual: el formulari no envia dades en la versió estàtica.
              Escriviu a <a href="mailto:ubuntu@associacioubuntu.org">ubuntu@associacioubuntu.org</a>.</p>
            </div>
          </form>
        </div>
        <div class="reveal d1">
          <div class="info-card">
            <h3>Associació Educació i Lleure Ubuntu</h3>
            <p>C/ Vallcivera, 24-26 · 08033 Barcelona<br>
            <a href="mailto:ubuntu@associacioubuntu.org">ubuntu@associacioubuntu.org</a><br>
            <a href="tel:+34931465255">93 146 52 55</a> · <a href="tel:+34620015846">620 01 58 46</a></p>
          </div>
          <div class="info-card mt-2 verd">
            <h3>CAU · Centre Obert · Trampolí</h3>
            <p>Escola Ferrer i Guàrdia · C/ Pedraforca, 3, 08033<br>
            CAU: cauubuntuzonanord@gmail.com<br>
            Centre Obert: centreobertubuntu@gmail.com · 681 68 86 61 / 722 23 27 80<br>
            Trampolí: projecte.trampoli@gmail.com</p>
          </div>
          <div class="info-card mt-2 blau">
            <h3>Espiral</h3>
            <p>Local Ubuntu (C/ Vallcivera, 24) i EBM Aqüeducte · EBM La Muntanya (C/ Sant Feliu de Codines, 4)<br>
            espaieducatiu.espiral@gmail.com</p>
          </div>
          <iframe class="map-embed mt-3" title="Mapa: C/ Vallcivera 24-26, Barcelona" loading="lazy"
            src="https://www.openstreetmap.org/export/embed.html?bbox=2.166%%2C41.435%%2C2.196%%2C41.455&amp;layer=mapnik&amp;marker=41.445%%2C2.181"></iframe>
        </div>
      </div>
    </div>
  </section>
</main>
""" % banner('Contacte',
             'Vine al local, escriu-nos o truca\'ns: la porta de la tribu sempre és oberta.',
             'assets/img/heroes/hero-3.webp',
             'Participants d\'Ubuntu en una sortida comunitària',
             'Contacte')

if __name__ == '__main__':
    render('qui-som.html', 'Qui som | Associació Ubuntu',
           'Història, missió, visió i valors de l\'Associació Educació i Lleure Ubuntu (reg. nº 49677), a Ciutat Meridiana des de 2008.',
           QUI_SOM, active='qui-som.html')
    render('projectes.html', 'Projectes | Associació Ubuntu',
           'CAU, Centre Obert, Trampolí i Espiral: els projectes educatius i comunitaris d\'Ubuntu a la Zona Nord de Barcelona.',
           PROJECTES, active='projectes.html')
    render('voluntariat.html', 'Voluntariat i pràctiques | Associació Ubuntu',
           'Fes-te voluntari o fes les pràctiques amb Ubuntu: acompanyament, formació i experiència real en educació social.',
           VOLUNTARIAT, active='voluntariat.html')
    render('dons.html', 'Donacions | Associació Ubuntu',
           'Dona a l\'Associació Ubuntu: transferència, Bizum 02962 o fes-te soci. Desgravacions fiscals segons la Llei 49/2002.',
           DONS, active='dons.html')
    render('contacte.html', 'Contacte | Associació Ubuntu',
           'Contacta amb l\'Associació Educació i Lleure Ubuntu: adreces, correus, telèfons i formulari.',
           CONTACTE, active='contacte.html')
