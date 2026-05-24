// ====================================================================
// DH v0.6 — Kedvenc Termékek — Renderer
// ====================================================================

// ---------- Shared phone chrome ----------

function renderStatusBar() {
  return `
    <div class="phone-status">
      <span>9:41</span>
      <span class="stat-right">
        ${ICO.wifi()}
        <span class="battery">79</span>
      </span>
    </div>`;
}

function renderTitleBar({ title = 'Termékek', showHeart = false, showBack = false } = {}) {
  const flag = `<span class="ph-flag">🇭🇺</span>`;
  const heartBtn = showHeart
    ? `<div class="ph-icon" style="color:var(--primary)">${ICO.heartOff(22)}</div>`
    : '';
  const backBtn = showBack
    ? `<div class="ph-icon" style="color:var(--primary)">${ICO.back()}</div>`
    : '';
  return `
    <div class="phone-header">
      <div style="display:flex;align-items:center;gap:6px">
        ${backBtn}
        <span class="ph-title">${title}</span>
      </div>
      <div class="ph-right">
        ${heartBtn}
        ${flag}
      </div>
    </div>
    <div class="phone-divider"></div>`;
}

function renderTabBar(active = 'shop', { cartCount = 4 } = {}) {
  const items = [
    { key: 'shop',    label: 'Termékek',   icon: ICO.home(22, active==='shop'?'var(--primary)':'var(--text3)'), badge: null },
    { key: 'cart',    label: 'Kosár',      icon: ICO.cart(22, active==='cart'?'var(--primary)':'var(--text3)'), badge: cartCount },
    { key: 'orders',  label: 'Rendelések', icon: ICO.clipboard(22, active==='orders'?'var(--primary)':'var(--text3)'), badge: null },
    { key: 'account', label: 'Fiók',       icon: ICO.user(22, active==='account'?'var(--primary)':'var(--text3)'), badge: null },
  ];
  return `
    <div class="tabbar">
      ${items.map(i => `
        <div class="tabbar-item ${active===i.key?'active':''}">
          ${i.icon}
          ${i.badge ? `<span class="tb-badge">${i.badge}</span>` : ''}
          <span>${i.label}</span>
        </div>
      `).join('')}
    </div>`;
}

function renderCatPills(active = 'osszes') {
  return `
    <div class="cat-pills">
      ${CATEGORIES.map(c => `
        <button class="cat-pill ${active===c.key?'active':''}">${c.label}</button>
      `).join('')}
    </div>`;
}

// Product card — matches real screenshot
function renderProdCard(p, { isFav = false, showHeart = true, interactive = false, onToggle = '' } = {}) {
  const heartCls = isFav ? 'on' : 'off';
  const heartSvg = isFav ? ICO.heartOn(18) : ICO.heartOff(18);
  const catCls = p.peach ? 'peach' : '';
  const clickAttr = interactive ? ` onclick="${onToggle || ''}"` : '';
  return `
    <div class="prod-card">
      <div class="pc-img">
        ${meatPhoto(p.photoTint)}
        ${showHeart ? `<button class="pc-heart ${heartCls}"${clickAttr}>${heartSvg}</button>` : ''}
      </div>
      <div class="pc-body">
        <span class="pc-cat ${catCls}">${p.catLabel}</span>
        <div class="pc-name">${p.name}</div>
        <div class="pc-price-row">
          <span class="pc-price">${p.price},00 RON</span>
          <span class="pc-price-unit"> / ${p.unit}</span>
        </div>
      </div>
    </div>`;
}

// Section header
function renderSecHead(title, count, { action = null, heartIcon = false } = {}) {
  return `
    <div class="sec-head">
      <div class="sec-head-left">
        ${heartIcon ? `<span style="color:var(--price-red);display:flex">${ICO.heartOn(16)}</span>` : ''}
        <span class="sh-title">${title}</span>
        ${count != null ? `<span class="sh-count">${count}</span>` : ''}
      </div>
      ${action ? `<span class="sh-action">${action}</span>` : ''}
    </div>`;
}

// ====================================================================
// SCENARIO RENDERERS
// ====================================================================

// 1. Empty state (no favs yet)
function renderScenarioEmpty() {
  return `
    ${renderStatusBar()}
    ${renderTitleBar({ title: 'Termékek' })}
    <div class="phone-body">
      ${renderCatPills('osszes')}
      <div class="prod-grid">
        ${PRODUCTS.slice(0, 6).map(p => renderProdCard(p, { isFav: false })).join('')}
      </div>
    </div>
    ${renderTabBar('shop')}`;
}

// 2. One favorite
function renderScenarioOneFav() {
  const favId = 'p3'; // Deák háziKolbász
  const favs = PRODUCTS.filter(p => p.id === favId);
  const rest = PRODUCTS.filter(p => p.id !== favId).slice(0, 5);
  return `
    ${renderStatusBar()}
    ${renderTitleBar({ title: 'Termékek', showHeart: true })}
    <div class="phone-body">
      ${renderCatPills('osszes')}

      ${renderSecHead('Kedvenceim', favs.length, { heartIcon: true })}
      <div class="prod-grid">
        ${favs.map(p => renderProdCard(p, { isFav: true })).join('')}
      </div>

      <div class="sec-divider"></div>

      ${renderSecHead('Összes termék', rest.length)}
      <div class="prod-grid">
        ${rest.map(p => renderProdCard(p, { isFav: false })).join('')}
      </div>
    </div>
    ${renderTabBar('shop')}`;
}

// 3. Multi-fav — with "Csak kedvencek" filter pill
function renderScenarioMultiFav() {
  const favIds = new Set(['p1', 'p3', 'p4']);
  const favs = PRODUCTS.filter(p => favIds.has(p.id));
  const rest = PRODUCTS.filter(p => !favIds.has(p.id)).slice(0, 4);
  return `
    ${renderStatusBar()}
    ${renderTitleBar({ title: 'Termékek', showHeart: true })}
    <div class="phone-body">
      <div class="cat-pills">
        <button class="fav-filter-pill">
          <span style="display:flex;align-items:center;color:var(--price-red)">${ICO.heartOn(14)}</span>
          Kedvencek
        </button>
        <button class="cat-pill active">Összes</button>
        <button class="cat-pill">Felvágott & Egyéb</button>
        <button class="cat-pill">Füstölt Áruk</button>
        <button class="cat-pill">Friss Növendékhús</button>
      </div>

      ${renderSecHead('Kedvenceim', favs.length, { heartIcon: true, action: 'Mind kosárba' })}
      <div class="prod-grid">
        ${favs.map(p => renderProdCard(p, { isFav: true })).join('')}
      </div>

      <div class="sec-divider"></div>

      ${renderSecHead('Összes termék', rest.length)}
      <div class="prod-grid">
        ${rest.map(p => renderProdCard(p, { isFav: false })).join('')}
      </div>
    </div>
    ${renderTabBar('shop')}`;
}

// 3b. Multi-fav with "Csak kedvencek" filter active
function renderScenarioMultiFavFilter() {
  const favIds = new Set(['p1', 'p3', 'p4']);
  const favs = PRODUCTS.filter(p => favIds.has(p.id));
  return `
    ${renderStatusBar()}
    ${renderTitleBar({ title: 'Termékek', showHeart: true })}
    <div class="phone-body">
      <div class="cat-pills">
        <button class="fav-filter-pill active">
          <span style="display:flex;align-items:center">${ICO.heartOn(14)}</span>
          Kedvencek
        </button>
        <button class="cat-pill">Összes</button>
        <button class="cat-pill">Felvágott & Egyéb</button>
        <button class="cat-pill">Füstölt Áruk</button>
      </div>

      <div style="padding:4px 2px 10px">
        <div style="font-size:12px;color:var(--text2)">
          ${favs.length} kedvenc termék megjelenítve
        </div>
      </div>

      <div class="prod-grid">
        ${favs.map(p => renderProdCard(p, { isFav: true })).join('')}
      </div>

      <div class="bulk-bar">
        <div class="bb-icon">${ICO.cart(20, 'white')}</div>
        <div class="bb-body">
          <div class="bb-title">Mind kosárba</div>
          <div class="bb-sub">${favs.length} termék · ~${favs.reduce((s,p)=>s+p.price,0)} RON</div>
        </div>
        <button class="bb-cta">Hozzáadás</button>
      </div>
    </div>
    ${renderTabBar('shop')}`;
}

// 4. Dedicated Favorites page (accessed via heart icon in header or Account menu)
function renderScenarioFavPage() {
  const favIds = new Set(['p1', 'p3', 'p4']);
  const favs = PRODUCTS.filter(p => favIds.has(p.id));
  const total = favs.reduce((s, p) => s + p.price, 0);
  return `
    ${renderStatusBar()}
    ${renderTitleBar({ title: 'Kedvenceim', showBack: true })}
    <div class="phone-body">
      <div class="bulk-bar">
        <div class="bb-icon">${ICO.cart(22, 'white')}</div>
        <div class="bb-body">
          <div class="bb-title">Mind kosárba (${favs.length})</div>
          <div class="bb-sub">~${total} RON · 1 koppintás</div>
        </div>
        <button class="bb-cta">Hozzáadás</button>
      </div>

      <div style="font-size:12px;color:var(--text2);margin:0 2px 10px">
        A leggyorsabb rendelés — a kedvenceid egyben.
      </div>

      <div class="prod-grid">
        ${favs.map(p => renderProdCard(p, { isFav: true })).join('')}
      </div>

      <div style="text-align:center;margin-top:20px;padding:12px;background:white;border-radius:14px;border:1px solid var(--border)">
        <div style="font-size:12px;color:var(--text2);margin-bottom:8px">Még több kedvenc terméket?</div>
        <button style="padding:10px 20px;border-radius:12px;background:transparent;color:var(--primary);border:2px solid var(--primary);font-size:13px;font-weight:700;cursor:pointer">Böngéssz termékeket →</button>
      </div>
    </div>
    ${renderTabBar('account')}`;
}

// 5. Fav page empty state
function renderScenarioFavEmpty() {
  return `
    ${renderStatusBar()}
    ${renderTitleBar({ title: 'Kedvenceim', showBack: true })}
    <div class="phone-body">
      <div class="empty-state">
        <div class="es-illust">
          <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.29 1.51 4.04 3 5.5l7 7Z"/></svg>
        </div>
        <h3>Még nincs kedvenced</h3>
        <p>A kedvenc termékeid itt gyűlnek — így gyorsabb lesz a rendelés.</p>

        <div class="es-steps">
          <div class="es-step">
            <div class="es-step-num">1</div>
            <div class="es-step-body">
              <strong>Böngéssz termékeket</strong>
              <span>A Termékek oldalon minden húsod megtalálod.</span>
            </div>
          </div>
          <div class="es-step">
            <div class="es-step-num">2</div>
            <div class="es-step-body">
              <strong>Koppints a szív ikonra</strong>
              <span>Ami tetszik, legyen a kedvenced — egy koppintás.</span>
            </div>
          </div>
          <div class="es-step">
            <div class="es-step-num">3</div>
            <div class="es-step-body">
              <strong>Rendelj egy koppintással</strong>
              <span>"Mind kosárba" → kész a vásárlás 5 mp alatt.</span>
            </div>
          </div>
        </div>

        <button class="es-cta">${ICO.pkg(18, 'white')} Böngéssz termékeket</button>
      </div>
    </div>
    ${renderTabBar('account')}`;
}

// 6. Guest flow with bottom sheet
function renderScenarioGuest() {
  return `
    ${renderStatusBar()}
    ${renderTitleBar({ title: 'Termékek' })}
    <div class="phone-body" style="position:relative;overflow:hidden">
      ${renderCatPills('osszes')}
      <div class="prod-grid" style="filter:brightness(0.92)">
        ${PRODUCTS.slice(0, 4).map(p => renderProdCard(p, { isFav: false })).join('')}
      </div>
    </div>

    <div class="bottom-sheet">
      <div class="bs-handle"></div>
      <div style="text-align:center;margin-bottom:14px">
        <div style="width:64px;height:64px;margin:0 auto 12px;background:var(--primary-lighter);border-radius:20px;display:flex;align-items:center;justify-content:center;color:var(--primary)">
          ${ICO.heartOn(32)}
        </div>
        <h3>Menthetjük ezt neked?</h3>
        <p>Jelentkezz be, hogy elmentsük a kedvenc termékeidet és bárhonnan elérd őket.</p>
      </div>
      <button class="bs-btn primary">Bejelentkezés</button>
      <button class="bs-btn secondary">Regisztráció</button>
      <button class="bs-btn ghost">Most nem</button>
    </div>

    ${renderTabBar('shop')}`;
}

// 7. Heart icon spec — close-up cards
function renderHeartSpec() {
  const container = document.getElementById('heart-spec-phones');
  const p = PRODUCTS[2]; // Deák háziKolbász
  container.innerHTML = `
    <div class="phone" style="height:auto;min-height:auto">
      <div style="padding:30px 20px 20px">
        <div style="font-size:11px;color:var(--text2);margin-bottom:10px;font-weight:600;text-transform:uppercase;letter-spacing:0.5px">Off állapot (nem kedvenc)</div>
        <div style="width:180px;margin-bottom:24px">
          ${renderProdCard(p, { isFav: false })}
        </div>

        <div style="font-size:11px;color:var(--text2);margin-bottom:10px;font-weight:600;text-transform:uppercase;letter-spacing:0.5px">On állapot (kedvenc)</div>
        <div style="width:180px;margin-bottom:24px">
          ${renderProdCard(p, { isFav: true })}
        </div>

        <div style="font-size:11px;color:var(--text2);margin-bottom:10px;font-weight:600;text-transform:uppercase;letter-spacing:0.5px">Átmeneti állapot (animáció közben)</div>
        <div style="width:180px">
          <div class="prod-card">
            <div class="pc-img">
              ${meatPhoto(p.photoTint)}
              <button class="pc-heart on" style="transform:scale(1.25);transition:none">
                ${ICO.heartOn(18)}
              </button>
            </div>
            <div class="pc-body">
              <span class="pc-cat peach">${p.catLabel}</span>
              <div class="pc-name">${p.name}</div>
              <div class="pc-price-row">
                <span class="pc-price">${p.price},00 RON</span>
                <span class="pc-price-unit"> / ${p.unit}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="phone" style="height:auto;min-height:auto;width:340px">
      <div style="padding:30px 20px 20px">
        <div style="font-size:13px;font-weight:800;margin-bottom:14px;color:var(--primary)">Design tokens</div>
        <table style="width:100%;font-size:12px;border-collapse:collapse">
          <tr style="border-bottom:1px solid var(--border)">
            <td style="padding:8px 0;color:var(--text2)">Off stroke</td>
            <td style="padding:8px 0;text-align:right;font-family:monospace">#5C544C</td>
          </tr>
          <tr style="border-bottom:1px solid var(--border)">
            <td style="padding:8px 0;color:var(--text2)">Off fill</td>
            <td style="padding:8px 0;text-align:right;font-family:monospace">none</td>
          </tr>
          <tr style="border-bottom:1px solid var(--border)">
            <td style="padding:8px 0;color:var(--text2)">On fill & stroke</td>
            <td style="padding:8px 0;text-align:right;font-family:monospace">#C8102E</td>
          </tr>
          <tr style="border-bottom:1px solid var(--border)">
            <td style="padding:8px 0;color:var(--text2)">Bubble bg</td>
            <td style="padding:8px 0;text-align:right;font-family:monospace">rgba(255,255,255,0.92)</td>
          </tr>
          <tr style="border-bottom:1px solid var(--border)">
            <td style="padding:8px 0;color:var(--text2)">Bubble méret</td>
            <td style="padding:8px 0;text-align:right;font-family:monospace">36×36px</td>
          </tr>
          <tr style="border-bottom:1px solid var(--border)">
            <td style="padding:8px 0;color:var(--text2)">Pozíció</td>
            <td style="padding:8px 0;text-align:right;font-family:monospace">top:10 right:10</td>
          </tr>
          <tr style="border-bottom:1px solid var(--border)">
            <td style="padding:8px 0;color:var(--text2)">Anim. scale</td>
            <td style="padding:8px 0;text-align:right;font-family:monospace">1 → 1.2 → 1</td>
          </tr>
          <tr style="border-bottom:1px solid var(--border)">
            <td style="padding:8px 0;color:var(--text2)">Anim. duration</td>
            <td style="padding:8px 0;text-align:right;font-family:monospace">140ms ease-out</td>
          </tr>
          <tr>
            <td style="padding:8px 0;color:var(--text2)">Touch target</td>
            <td style="padding:8px 0;text-align:right;font-family:monospace">44×44px (padding)</td>
          </tr>
        </table>

        <div style="height:20px"></div>

        <div style="font-size:13px;font-weight:800;margin-bottom:10px;color:var(--primary)">Frappe integráció</div>
        <div style="font-size:11px;color:var(--text2);line-height:1.6;background:var(--bg);padding:12px;border-radius:10px;font-family:monospace">
          <div><strong>Doctype:</strong> User</div>
          <div><strong>Field:</strong> favorite_items (JSON)</div>
          <div style="margin-top:8px"><strong>Endpoint:</strong></div>
          <div>POST /api/favorites/toggle</div>
          <div style="margin-top:4px"><strong>Body:</strong> { item_id }</div>
          <div><strong>Response:</strong> { is_fav }</div>
          <div style="margin-top:8px;color:var(--text3);font-family:system-ui;font-style:italic;line-height:1.4">Optimistic UI: a csillag azonnal változik, szerver hibánál visszaáll + toast.</div>
        </div>
      </div>
    </div>
  `;
}

// ====================================================================
// MOUNT
// ====================================================================
function mountAll() {
  document.getElementById('phone-empty').innerHTML = renderScenarioEmpty();
  document.getElementById('phone-one-fav').innerHTML = renderScenarioOneFav();
  document.getElementById('phone-multi-fav').innerHTML = renderScenarioMultiFav();
  document.getElementById('phone-multi-fav-filter').innerHTML = renderScenarioMultiFavFilter();
  document.getElementById('phone-fav-page').innerHTML = renderScenarioFavPage();
  document.getElementById('phone-fav-empty').innerHTML = renderScenarioFavEmpty();
  document.getElementById('phone-guest').innerHTML = renderScenarioGuest();
  renderHeartSpec();
}

document.querySelectorAll('.tab').forEach(t => {
  t.addEventListener('click', () => {
    document.querySelectorAll('.tab').forEach(x => x.classList.remove('active'));
    document.querySelectorAll('.feature').forEach(f => f.classList.remove('active'));
    t.classList.add('active');
    document.getElementById(t.dataset.tab).classList.add('active');
    try { localStorage.setItem('dh_favs_tab', t.dataset.tab); } catch (e) {}
  });
});

try {
  const saved = localStorage.getItem('dh_favs_tab');
  if (saved && document.querySelector(`.tab[data-tab="${saved}"]`)) {
    document.querySelector(`.tab[data-tab="${saved}"]`).click();
  }
} catch (e) {}

mountAll();
