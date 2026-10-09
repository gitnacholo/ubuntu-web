/* Ubuntu v2 — JS global: menú móvil, reveal on scroll, contadores, cookies */
(function () {
  'use strict';

  /* ---------- Menú móvil ---------- */
  var toggle = document.querySelector('.nav-toggle');
  var mobile = document.getElementById('mobile-nav');
  if (toggle && mobile) {
    toggle.addEventListener('click', function () {
      var open = mobile.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      document.body.style.overflow = open ? 'hidden' : '';
    });
    mobile.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        mobile.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && mobile.classList.contains('open')) {
        mobile.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
        toggle.focus();
      }
    });
  }

  /* ---------- Header con sombra al hacer scroll ---------- */
  var header = document.querySelector('.site-header');
  if (header) {
    var onScroll = function () {
      header.classList.toggle('scrolled', window.scrollY > 8);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ---------- Reveal on scroll ---------- */
  var revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && revealEls.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          en.target.classList.add('in');
          io.unobserve(en.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('in'); });
  }

  /* ---------- Contadores animados (data-count) ---------- */
  var counters = document.querySelectorAll('[data-count]');
  var animate = function (el) {
    var target = parseInt(el.getAttribute('data-count'), 10) || 0;
    var suffix = el.getAttribute('data-suffix') || '';
    var dur = 1400, t0 = null;
    var step = function (ts) {
      if (!t0) t0 = ts;
      var p = Math.min((ts - t0) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(target * eased).toLocaleString('ca-ES') + suffix;
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };
  if ('IntersectionObserver' in window && counters.length) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          animate(en.target);
          cio.unobserve(en.target);
        }
      });
    }, { threshold: 0.4 });
    counters.forEach(function (el) { cio.observe(el); });
  } else {
    counters.forEach(function (el) {
      el.textContent = (el.getAttribute('data-count') || '') + (el.getAttribute('data-suffix') || '');
    });
  }

  /* ---------- Aviso de cookies (sin tracking; solo aviso informativo) ---------- */
  var ck = document.getElementById('cookieNotice');
  if (ck && !localStorage.getItem('cookiesAccepted')) {
    var btn = ck.querySelector('.cookie-btn');
    if (btn) {
      btn.addEventListener('click', function () {
        ck.style.display = 'none';
        try { localStorage.setItem('cookiesAccepted', 'true'); } catch (e) {}
      });
    }
    ck.style.display = 'block';
  }
})();

/* Ubuntu — Accessibilitat persistent (contrast, mida de lletra, lletra llegible) */
(function () {
  'use strict';
  var KEY_DARK = 'ubuntu-a11y-dark';
  var KEY_FS = 'ubuntu-a11y-fs';
  var KEY_DYS = 'ubuntu-a11y-dys';
  var MIN_FS = 12, MAX_FS = 24, STEP = 2, DEF_FS = 16;

  function llegir(clau) { try { return window.localStorage.getItem(clau); } catch (e) { return null; } }
  function desar(clau, valor) { try { window.localStorage.setItem(clau, valor); } catch (e) {} }
  function esborrar(clau) { try { window.localStorage.removeItem(clau); } catch (e) {} }

  var arrel = document.documentElement;
  var btnContrast = document.getElementById('a11y-contrast');
  var btnMes = document.getElementById('a11y-font-mes');
  var btnMenys = document.getElementById('a11y-font-menys');
  var btnDislexia = document.getElementById('a11y-dislexia');
  if (!btnContrast && !btnMes && !btnMenys && !btnDislexia) return;

  function aplicaEstat() {
    if (btnContrast) btnContrast.setAttribute('aria-pressed', arrel.classList.contains('modo-oscuro') ? 'true' : 'false');
    if (btnDislexia) btnDislexia.setAttribute('aria-pressed', arrel.classList.contains('font-dislexia') ? 'true' : 'false');
  }
  function midaActual() {
    var v = parseInt(arrel.style.fontSize, 10);
    return isNaN(v) ? DEF_FS : v;
  }
  function canviaMida(dir) {
    var v = Math.max(MIN_FS, Math.min(MAX_FS, midaActual() + dir * STEP));
    if (v === DEF_FS) { arrel.style.fontSize = ''; esborrar(KEY_FS); }
    else { arrel.style.fontSize = v + 'px'; desar(KEY_FS, String(v)); }
  }

  if (btnContrast) btnContrast.addEventListener('click', function () {
    var actiu = arrel.classList.toggle('modo-oscuro');
    if (actiu) desar(KEY_DARK, '1'); else esborrar(KEY_DARK);
    aplicaEstat();
  });
  if (btnMes) btnMes.addEventListener('click', function () { canviaMida(1); });
  if (btnMenys) btnMenys.addEventListener('click', function () { canviaMida(-1); });
  if (btnDislexia) btnDislexia.addEventListener('click', function () {
    var actiu = arrel.classList.toggle('font-dislexia');
    if (actiu) desar(KEY_DYS, '1'); else esborrar(KEY_DYS);
    aplicaEstat();
  });
  aplicaEstat();
})();
