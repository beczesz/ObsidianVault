// ====================================================================
// DH v0.4 — Termékek oldal explorations — Renderer
// 5 approaches (A1..A5) + comparison view
// ====================================================================

// ---------- Shared building blocks ----------

function renderStatusBar() {
  return `
    <div class="phone-status">
      <span>9:41</span>
      <span style="display:flex;gap:4px;align-items:center">
        ${ICO.wifi()}
        <span style="font-size:10px;font-weight:700;margin-left:4px">100%</span>
        ${ICO.battery()}
      </span>
    </div>`;
}

function renderHeader({ title = 'Termékek', withBell = true, withCart = true, cartCount = 3 } = {}) {
  return `
    <div class="phone-header">
      <div class="ph-title">${title}</div>
      <div class="ph-right">
        ${withBell ? `<div class="ph-icon">${ICO.bell()}${cartCount ? '<span class="dot"></span>' : ''}</div>` : ''}
        ${withCart ? `<div class="ph-icon">${ICO.cart(18, 'var(--text)')}${cartCount ? '<span class="dot"></span>' : ''}</div>` : ''}
      </div>
    </div>`;
}

function renderTabBar(active = 'home') {
  const items = [
    { key: 'home',    label: 'Kezdőlap', icon: ICO.home(20, active==='home'?'var(--primary)':'var(--text2)') },
    { key: 'shop',    label: 'Termékek', icon: ICO.pkg(20, active==='shop'?'var(--primary)':'var(--text2)')  },
    { key: 'orders',  label: 'Rendeléseim', icon: `<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="${active==='orders'?'var(--primary)':'var(--text2)'}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="9" y1="13" x2="15" y2="13"/><line x1="9" y1="17" x2="15" y2="17"/></svg>` },
    { key: 'account', label: 'Fiók',     icon: ICO.user(20, active==='account'?'var(--primary)':'var(--text2)') },
  ];
  return `
    <div class="tabbar">
      ${items.map(i => `
        <div class="tabbar-item ${active===i.key?'active':''}">
          ${i.icon}
          <span>${i.label}</span>
        </div>
      `).join('')}
    </div>`;
}

function renderSearch() {
  return `
    <div class="search-bar">
      ${ICO.search(16)}
      <input placeholder="Keress terméket… (pl. kolbász, sonka)">
    </div>`;
}

function renderCatPills(active = 'osszes', withCount = false) {
  const items = [{ key: 'osszes', label: 'Összes', count: PRODUCTS.length }, ...CATEGORIES];
  return `
    <div class="cat-pills">
      ${items.map(c => `
        <span class="cat-pill ${active===c.key?'active':''}">
          ${c.label}${withCount?`<span class="cat-pill-count">${c.count}</span>`:''}
        </span>
      `).join('')}
    </div>`;
}

function renderFilterBar(count = PRODUCTS.length, sort = 'Népszerű', activeFilters = 2) {
  return `
    <div class="filter-bar">
      <button class="filter-btn">${ICO.filter()} Szűrők ${activeFilters?`<span class="filter-dot">${activeFilters}</span>`:''}</button>
      <button class="filter-btn">${ICO.sort()} ${sort}</button>
      <span class="result-count" style="margin-left:auto">${count} termék</span>
    </div>`;
}

// Product card (2-col grid)
function renderProdCard(p, { fav = false } = {}) {
  const isOos = p.stock === 'oos';
  return `
    <div class="prod-card">
      <div class="pc-img">
        ${meatImg(p.cat, p.catLabel)}
        ${p.badge === 'sale' ? '<div class="pc-badge sale">−10%</div>' : ''}
        ${p.isNew ? '<div class="pc-badge new">ÚJ</div>' : ''}
        <button class="pc-fav">${ICO.heart(16, fav?'var(--primary)':'#777', fav?'var(--primary)':'none')}</button>
        ${isOos ? '<div class="pc-oos-ov">Nincs raktáron</div>' : ''}
      </div>
      <div class="pc-body">
        <div class="pc-cat">${p.catLabel}</div>
        <div class="pc-name">${p.name}</div>
        <div class="pc-price-row">
          <div>
            ${p.oldPrice ? `<div class="pc-price-old">${p.oldPrice} RON</div>` : ''}
            <div class="pc-price">${p.price} RON</div>
            <div class="pc-price-unit">${p.unit}</div>
          </div>
          ${isOos
            ? `<button class="pc-add" style="background:#CCC" disabled>${ICO.plus(14,'white',3)}</button>`
            : `<button class="pc-add">${ICO.plus(16,'white',3)}</button>`}
        </div>
      </div>
    </div>`;
}

// Product list-item (1-col horizontal)
function renderProdListItem(p, { qty = 0 } = {}) {
  return `
    <div class="prod-list-item">
      <div class="pli-img">${meatImg(p.cat, p.catLabel, { small: true })}</div>
      <div class="pli-body">
        <div class="pli-cat">${p.catLabel}</div>
        <div class="pli-name">${p.name}</div>
        <div class="pli-meta">${p.unit.replace('RON','').trim()}</div>
        <div class="pli-price-row">
          <div>
            <span class="pli-price">${p.price} RON</span>
            <span class="pli-price-unit"> ${p.unit}</span>
          </div>
          ${qty > 0
            ? `<div class="qty-step">
                 <button>−</button>
                 <span class="qval">${qty.toFixed(1).replace('.',',')} kg</span>
                 <button>+</button>
               </div>`
            : `<button class="pc-add">${ICO.plus(16,'white',3)}</button>`}
        </div>
      </div>
    </div>`;
}

// Savings nudge (mini progress)
function renderSavingsNudge() {
  const cartTotal = 98;
  const target = 150;
  const pct = Math.min((cartTotal / target) * 100, 100);
  return `
    <div class="savings-nudge">
      <div class="sn-icon">${ICO.piggy(22, '#2D7A4F')}</div>
      <div class="sn-body">
        <div class="sn-title">Még ${target - cartTotal} RON → ingyenes szállítás</div>
        <div class="sn-sub">${cartTotal}/${target} RON</div>
        <div class="sn-bar"><div style="width:${pct}%"></div></div>
      </div>
    </div>`;
}

function renderBundleStrip() {
  return `
    <div class="bundle-strip">
      ${BUNDLES.map(b => `
        <div class="bundle-chip">
          <div class="bc-dot">${ICO.flame(16, 'white', 2)}</div>
          <div class="bc-txt">
            <div class="bc-t1">${b.name}</div>
            <div class="bc-t2">${b.items} term. · ~${b.price} RON</div>
          </div>
        </div>
      `).join('')}
    </div>`;
}

// ====================================================================
// A1 — CLASSIC 2-COL GRID
// ====================================================================
function renderA1() {
  const shown = PRODUCTS.slice(0, 8); // first 8 products
  const body = `
    ${renderStatusBar()}
    ${renderHeader({ title: 'Termékek' })}
    <div class="phone-body">
      ${renderSavingsNudge()}
      ${renderSearch()}

      <div class="sec-head" style="margin-top:0">
        <div class="sh-title">${ICO.pkg(16, 'var(--text)')} Csomagok</div>
        <div class="sh-link">Összes ›</div>
      </div>
      ${renderBundleStrip()}

      ${renderCatPills('osszes', true)}
      ${renderFilterBar(shown.length, 'Népszerű', 2)}

      <div class="prod-grid">
        ${shown.map((p, i) => renderProdCard(p, { fav: i === 1 })).join('')}
      </div>

      <div style="text-align:center;margin:12px 0">
        <button class="filter-btn" style="padding:10px 24px;font-size:13px">További 14 termék mutatása</button>
      </div>
    </div>
    ${renderTabBar('shop')}`;
  return body;
}

// ====================================================================
// A2 — CATEGORY CAROUSEL + VERTICAL LIST
// ====================================================================
function renderA2() {
  const filtered = PRODUCTS.filter(p => p.cat === 'friss').slice(0, 5);

  const catCarousel = `
    <div class="cat-carousel">
      ${CATEGORIES.map((c, i) => `
        <div class="cat-hero meat-img ${c.tint} ${i===0?'active':''}">
          <div class="ch-name">${c.label}</div>
          <div class="ch-count">${c.count} termék</div>
        </div>
      `).join('')}
    </div>`;

  const body = `
    ${renderStatusBar()}
    ${renderHeader({ title: 'Termékek' })}
    <div class="phone-body">
      ${renderSearch()}

      <div class="sec-head" style="margin-top:0">
        <div class="sh-title">Kategóriák</div>
      </div>
      ${catCarousel}

      <div class="sec-head">
        <div class="sh-title">Friss húsok</div>
        <div class="sh-link">${filtered.length} termék</div>
      </div>
      ${renderFilterBar(filtered.length, 'Ár szerint', 1)}

      <div class="prod-list">
        ${filtered.map((p, i) => renderProdListItem(p, { qty: i === 0 ? 0.5 : 0 })).join('')}
      </div>
    </div>
    ${renderTabBar('shop')}`;
  return body;
}

// ====================================================================
// A3 — MAGAZINE MIX
// ====================================================================
function renderA3() {
  const recommended = PRODUCTS.filter(p => p.badge === 'sale' || p.isNew).slice(0, 4);
  const newItems = PRODUCTS.filter(p => p.isNew).slice(0, 4);
  const browsing = PRODUCTS.slice(0, 4);

  const editorial = `
    <div class="edit-card">
      <div class="ec-tag">Szezon · április</div>
      <div class="ec-title">Grillszezon — 5 tipp<br>a tökéletes sertéstarjához</div>
      <div class="ec-sub">A mesterszakács ajánlja · 3 perc olvasás</div>
    </div>`;

  const body = `
    ${renderStatusBar()}
    ${renderHeader({ title: 'Termékek' })}
    <div class="phone-body">
      ${renderSearch()}
      ${editorial}
      ${renderSavingsNudge()}

      <div class="sec-head" style="margin-top:0">
        <div class="sh-title">${ICO.pkg(16)} Csomagok</div>
        <div class="sh-link">Mind ›</div>
      </div>
      ${renderBundleStrip()}

      <div class="sec-head">
        <div class="sh-title">Ajánljuk</div>
        <div class="sh-link">Mind ›</div>
      </div>
      <div class="h-scroll">
        ${recommended.map(p => renderProdCard(p)).join('')}
      </div>

      <div class="sec-head">
        <div class="sh-title">Újdonságok</div>
        <div class="sh-link">Mind ›</div>
      </div>
      <div class="h-scroll">
        ${newItems.map(p => renderProdCard(p)).join('')}
      </div>

      <div class="sec-head">
        <div class="sh-title">Böngéssz kategóriák szerint</div>
      </div>
      ${renderCatPills('osszes')}
      <div class="prod-grid">
        ${browsing.map(p => renderProdCard(p)).join('')}
      </div>
    </div>
    ${renderTabBar('shop')}`;
  return body;
}

// ====================================================================
// A4 — DENSITY-VARIED
// ====================================================================
function renderA4() {
  const featured = PRODUCTS.find(p => p.id === 'P004'); // Sertéskaraj on sale
  const popular = PRODUCTS.slice(0, 4);
  const rest = PRODUCTS.slice(4, 8);

  const featureCard = `
    <div class="feat-card">
      <div class="fc-img meat-img friss">
        <div class="fc-tag">A hét kiemelt terméke</div>
      </div>
      <div class="fc-body">
        <div class="pc-cat" style="font-size:10px;color:var(--text2);text-transform:uppercase;letter-spacing:0.4px;font-weight:600">${featured.catLabel}</div>
        <div class="fc-name">${featured.name}</div>
        <div class="fc-meta">Sertés · 1 kg vagy 500 g kiszerelésben · Ma frissen vágott</div>
        <div class="fc-row">
          <div>
            <span style="font-size:11px;color:var(--text2);text-decoration:line-through">${featured.oldPrice} RON</span>
            <div><span class="fc-price">${featured.price}</span> <span class="fc-price-unit" style="display:inline;font-size:12px">RON / kg</span></div>
          </div>
          <button class="fc-btn">${ICO.plus(14)} Kosárba</button>
        </div>
      </div>
    </div>`;

  const quickTiles = `
    <div class="quick-grid">
      ${CATEGORIES.slice(0, 4).map(c => `
        <div class="quick-tile">
          <div class="qt-img">${meatImg(c.tint, c.label, { small: true })}</div>
          <div class="qt-name">${c.label}</div>
        </div>
      `).join('')}
    </div>`;

  const body = `
    ${renderStatusBar()}
    ${renderHeader({ title: 'Termékek' })}
    <div class="phone-body">
      ${renderSearch()}
      ${featureCard}

      <div class="sec-head" style="margin-top:0">
        <div class="sh-title">Kategóriák</div>
      </div>
      ${quickTiles}

      <div class="sec-head">
        <div class="sh-title">${ICO.pkg(16)} Csomagok</div>
        <div class="sh-link">Mind ›</div>
      </div>
      ${renderBundleStrip()}

      <div class="sec-head">
        <div class="sh-title">Népszerű most</div>
        <div class="sh-link">Mind ›</div>
      </div>
      <div class="h-scroll">
        ${popular.map(p => renderProdCard(p)).join('')}
      </div>

      <div class="sec-head">
        <div class="sh-title">Összes termék</div>
      </div>
      <div class="prod-grid">
        ${rest.map(p => renderProdCard(p)).join('')}
      </div>
    </div>
    ${renderTabBar('shop')}`;
  return body;
}

// ====================================================================
// A5 — HERO SWIPE + CATEGORY TILES
// ====================================================================
function renderA5() {
  const popular = PRODUCTS.slice(0, 4);

  const heroSwipe = `
    <div class="hero-swipe">
      ${HEROES.map(h => `
        <div class="hero-slide ${h.tint}">
          <div>
            <div class="hs-eyebrow">${h.eyebrow}</div>
            <div class="hs-title">${h.title}</div>
            <div class="hs-sub">${h.sub}</div>
          </div>
          <div class="hs-cta">${h.cta} ${ICO.chevR(13)}</div>
        </div>
      `).join('')}
    </div>
    <div class="hero-dots">
      <div class="hero-dot active"></div>
      <div class="hero-dot"></div>
      <div class="hero-dot"></div>
    </div>`;

  const catTiles = `
    <div class="cat-tile-grid">
      <div class="cat-tile large meat-img friss">
        <div class="ct-name">Friss húsok</div>
        <div class="ct-count">6 termék · napi szállítás</div>
      </div>
      <div class="cat-tile meat-img fustolt">
        <div class="ct-name">Füstölt</div>
        <div class="ct-count">5 termék</div>
      </div>
      <div class="cat-tile meat-img kolbasz">
        <div class="ct-name">Kolbász</div>
        <div class="ct-count">5 termék</div>
      </div>
      <div class="cat-tile meat-img felvagott">
        <div class="ct-name">Felvágott</div>
        <div class="ct-count">4 termék</div>
      </div>
      <div class="cat-tile meat-img fuszer">
        <div class="ct-name">Fűszer</div>
        <div class="ct-count">4 termék</div>
      </div>
    </div>`;

  const body = `
    ${renderStatusBar()}
    ${renderHeader({ title: 'Termékek' })}
    <div class="phone-body">
      ${renderSearch()}
      ${heroSwipe}

      <div class="sec-head" style="margin-top:0">
        <div class="sh-title">Kategóriák</div>
      </div>
      ${catTiles}

      <div class="sec-head">
        <div class="sh-title">${ICO.pkg(16)} Csomagok</div>
        <div class="sh-link">Mind ›</div>
      </div>
      ${renderBundleStrip()}

      <div class="sec-head">
        <div class="sh-title">Népszerűek most</div>
        <div class="sh-link">Mind ›</div>
      </div>
      <div class="h-scroll">
        ${popular.map(p => renderProdCard(p)).join('')}
      </div>
    </div>
    ${renderTabBar('shop')}`;
  return body;
}

// ====================================================================
// Comparison view — all 5 phones side-by-side (scrollable horizontally)
// ====================================================================
function renderCompare() {
  const container = document.getElementById('compare-phones');
  const labels = [
    { key: 'a1', label: '1 · Klasszikus grid' },
    { key: 'a2', label: '2 · Carousel + lista' },
    { key: 'a3', label: '3 · Magazine' },
    { key: 'a4', label: '4 · Density-varied' },
    { key: 'a5', label: '5 · Hero swipe' },
  ];
  const renderers = { a1: renderA1, a2: renderA2, a3: renderA3, a4: renderA4, a5: renderA5 };
  container.innerHTML = labels.map(l => `
    <div style="display:flex;flex-direction:column;align-items:center;gap:8px;">
      <div style="font-size:11px;font-weight:700;color:var(--text2);text-transform:uppercase;letter-spacing:0.8px">${l.label}</div>
      <div class="phone" style="transform:scale(0.75);transform-origin:top center;margin-bottom:-180px">${renderers[l.key]()}</div>
    </div>
  `).join('');
}

// ====================================================================
// Boot
// ====================================================================
function mountAll() {
  document.getElementById('phone-a1').innerHTML = renderA1();
  document.getElementById('phone-a2').innerHTML = renderA2();
  document.getElementById('phone-a3').innerHTML = renderA3();
  document.getElementById('phone-a4').innerHTML = renderA4();
  document.getElementById('phone-a5').innerHTML = renderA5();
}

document.querySelectorAll('.tab').forEach(t => {
  t.addEventListener('click', () => {
    document.querySelectorAll('.tab').forEach(x => x.classList.remove('active'));
    document.querySelectorAll('.feature').forEach(f => f.classList.remove('active'));
    t.classList.add('active');
    const id = t.dataset.tab;
    document.getElementById(id).classList.add('active');
    if (id === 'compare') renderCompare();
    // persist tab
    try { localStorage.setItem('dh_prod_listing_tab', id); } catch (e) {}
  });
});

// Restore last tab
try {
  const saved = localStorage.getItem('dh_prod_listing_tab');
  if (saved && document.querySelector(`.tab[data-tab="${saved}"]`)) {
    document.querySelector(`.tab[data-tab="${saved}"]`).click();
  }
} catch (e) {}

mountAll();
