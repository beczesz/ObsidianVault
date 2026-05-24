#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dashboard v2 generálás: önálló offline HTML, drill-down, szűrők, kereső, téma."""
import os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda n: os.path.join(BASE, n)
DATA = open(P('_build/data_v2.json'), encoding='utf-8').read()
CHARTJS = open(P('_build/chart.umd.min.js'), encoding='utf-8').read()

HTML = r'''<!DOCTYPE html>
<html lang="hu">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Gergely István — üzleti dashboard</title>
<style>
:root[data-theme="dark"]{
  --bg:#0d1117;--bg2:#0a0e14;--panel:#161b22;--panel2:#1c2330;--line:#283041;
  --txt:#e6edf3;--muted:#8b98a9;--accent:#4f8cff;--accent2:#36c5a0;--warn:#f0a020;--bad:#f0506e;--good:#36c5a0;
  --shadow:0 6px 24px rgba(0,0,0,.35);
}
:root[data-theme="light"]{
  --bg:#f4f6fb;--bg2:#eef1f7;--panel:#ffffff;--panel2:#f1f4fa;--line:#e2e7f0;
  --txt:#1a2230;--muted:#697586;--accent:#2f6fed;--accent2:#1aa884;--warn:#c9821a;--bad:#d83a5a;--good:#1aa884;
  --shadow:0 4px 18px rgba(40,60,100,.10);
}
*{box-sizing:border-box}
body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  background:var(--bg);color:var(--txt);font-size:14px;line-height:1.45;transition:background .2s,color .2s}
header{padding:16px 24px 0;border-bottom:1px solid var(--line);position:sticky;top:0;z-index:30;
  background:color-mix(in srgb,var(--bg) 92%,transparent);backdrop-filter:blur(8px)}
.topbar{display:flex;align-items:center;gap:14px;flex-wrap:wrap}
.brand{font-size:18px;font-weight:700;margin-right:auto}
.brand .sub{display:block;font-size:12px;color:var(--muted);font-weight:400;margin-top:2px}
.controls{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
input,select,button{font:inherit;color:var(--txt);background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:7px 10px}
input::placeholder{color:var(--muted)}
button{cursor:pointer;transition:.15s}
button:hover{border-color:var(--accent)}
#search{min-width:210px}
nav{display:flex;gap:6px;flex-wrap:wrap;margin:14px 0 0;padding-bottom:0}
nav button{background:transparent;border:none;border-bottom:2px solid transparent;border-radius:0;padding:9px 12px;color:var(--muted)}
nav button:hover{color:var(--txt)}
nav button.active{color:var(--accent);border-bottom-color:var(--accent);font-weight:600}
#filterbar{padding:8px 0 12px;min-height:0}
.chip{display:inline-flex;align-items:center;gap:8px;background:var(--accent);color:#fff;border-radius:20px;padding:5px 8px 5px 14px;font-size:13px;font-weight:600}
.chip b{font-weight:700}
.chip button{background:rgba(255,255,255,.25);border:none;color:#fff;border-radius:50%;width:20px;height:20px;padding:0;line-height:1;font-size:14px}
main{padding:18px 24px 70px;max-width:1320px;margin:0 auto}
.tab{display:none} .tab.active{display:block;animation:fade .22s}
@keyframes fade{from{opacity:0;transform:translateY(4px)}to{opacity:1}}
.grid{display:grid;gap:16px}
.k4{grid-template-columns:repeat(4,1fr)}.k3{grid-template-columns:repeat(3,1fr)}.k2{grid-template-columns:repeat(2,1fr)}
@media(max-width:920px){.k4,.k3{grid-template-columns:1fr 1fr}}
@media(max-width:600px){.k4,.k3,.k2{grid-template-columns:1fr}}
.card{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:18px;box-shadow:var(--shadow)}
.card.full{margin-top:16px}
.card h3{margin:0 0 12px;font-size:15px;display:flex;justify-content:space-between;align-items:center;gap:8px}
.kpi{cursor:default}.kpi.click{cursor:pointer}.kpi.click:hover{border-color:var(--accent)}
.kpi .l{color:var(--muted);font-size:11px;text-transform:uppercase;letter-spacing:.5px}
.kpi .v{font-size:25px;font-weight:700;margin:6px 0 2px}
.kpi .d{font-size:12px;color:var(--accent2)}
canvas{max-height:330px}
table{width:100%;border-collapse:collapse;font-size:13px}
th,td{text-align:right;padding:8px 10px;border-bottom:1px solid var(--line)}
th:first-child,td:first-child{text-align:left}
th{color:var(--muted);font-weight:600;font-size:11px;text-transform:uppercase;letter-spacing:.3px;position:sticky;top:0;background:var(--panel)}
tr.clk{cursor:pointer}tr.clk:hover td{background:var(--panel2)}
.tablewrap{max-height:460px;overflow:auto;border-radius:8px}
.pill{display:inline-block;padding:2px 8px;border-radius:20px;font-size:11px;font-weight:600}
.pill.bad{background:color-mix(in srgb,var(--bad) 18%,transparent);color:var(--bad)}
.pill.warn{background:color-mix(in srgb,var(--warn) 18%,transparent);color:var(--warn)}
.pill.good{background:color-mix(in srgb,var(--good) 18%,transparent);color:var(--good)}
.note{color:var(--muted);font-size:12px;margin-top:8px;line-height:1.5}
.callout{border-left:3px solid var(--accent2);background:var(--panel2);padding:11px 14px;border-radius:0 8px 8px 0;margin:14px 0;font-size:13px}
.callout.warn{border-left-color:var(--warn)}
.tag{font-size:11px;color:var(--muted)}
.bc{display:flex;gap:6px;align-items:center;font-size:13px;color:var(--muted);margin-bottom:12px;flex-wrap:wrap}
.bc a{color:var(--accent);cursor:pointer;text-decoration:none}
.linklike{color:var(--accent);cursor:pointer}
.modal{position:fixed;inset:0;background:rgba(0,0,0,.5);display:flex;align-items:flex-start;justify-content:center;
  padding:5vh 16px;z-index:50;overflow:auto}
.modal[hidden]{display:none}
.modal .box{background:var(--panel);border:1px solid var(--line);border-radius:16px;max-width:840px;width:100%;
  padding:22px;box-shadow:var(--shadow)}
.modal h2{margin:0 0 6px;font-size:18px}
.modal .x{float:right;border-radius:50%;width:30px;height:30px;padding:0}
.flex{display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.filters{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px}
.bigstat{font-size:30px;font-weight:700}
.muted{color:var(--muted)}
.result{padding:10px 12px;border:1px solid var(--line);border-radius:10px;margin-bottom:8px;cursor:pointer;background:var(--panel2)}
.result:hover{border-color:var(--accent)}
.result .n{font-weight:600}
.swatch{display:inline-block;width:10px;height:10px;border-radius:2px;margin-right:5px;vertical-align:middle}
.legend{display:flex;gap:14px;flex-wrap:wrap;font-size:12px;color:var(--muted);margin-bottom:8px}
</style>
</head>
<body>
<header>
  <div class="topbar">
    <div class="brand">Gergely István — üzleti dashboard<span class="sub" id="brandsub"></span></div>
    <div class="controls">
      <input id="search" placeholder="🔎 Termék keresése…" autocomplete="off"/>
      <select id="yearSel" title="Év"></select>
      <select id="storeSel" title="Telephely szűrő"></select>
      <button id="themeBtn" title="Téma">🌙</button>
    </div>
  </div>
  <nav id="nav"></nav>
  <div id="filterbar"></div>
</header>
<main id="view"></main>
<div class="modal" id="modal" hidden><div class="box" id="modalbox"></div></div>

<script>__CHARTJS__</script>
<script>
const DB = __DATA__;
const STATE = { year: DB.meta.aktiv_ev, store: null, theme: 'dark', sub: {} };
const Y = () => DB.years[STATE.year];
const STORES = () => Y().gestiune.map(g=>g.nev);
const fmt = n => (n==null?'–':Number(n).toLocaleString('hu-HU',{maximumFractionDigits:0}));
const fmtM = n => (n/1e6).toLocaleString('hu-HU',{maximumFractionDigits:2})+' M';
const pct = n => (n==null?'–':Number(n).toLocaleString('hu-HU',{maximumFractionDigits:1})+'%');
const lei = n => fmt(n)+' lej';
const MONTHS=['Jan','Feb','Már','Ápr','Máj','Jún','Júl','Aug','Szep','Okt','Nov','Dec'];
const C=['#4f8cff','#36c5a0','#f0a020','#f0506e','#a06bff','#ff8a5c','#3fb6d3','#d39a3f'];
const META_COLOR={};DB.meta.meta_kategoriak.forEach((m,i)=>META_COLOR[m]=C[i%C.length]);
let CHARTS=[];
function newChart(canvas,cfg){const c=new Chart(canvas,cfg);CHARTS.push(c);return c;}
function killCharts(){CHARTS.forEach(c=>{try{c.destroy()}catch(e){}});CHARTS=[];}
function themeColors(){const s=getComputedStyle(document.documentElement);
  Chart.defaults.color=s.getPropertyValue('--muted').trim();
  Chart.defaults.borderColor=s.getPropertyValue('--line').trim();
  Chart.defaults.font.family='-apple-system,Segoe UI,Roboto,sans-serif';}

/* ---------- TABS ---------- */
const TABS=[['attekintes','Áttekintés'],['telephely','Telephely'],['mire','Mire költenek'],
  ['termekek','Termékek'],['b2b','B2B & partnerek'],['ido','Idő & ritmus'],['keszlet','Készlet']];
const STORE_AWARE={telephely:1,termekek:1,keszlet:1};
let CURRENT='attekintes';
const nav=document.getElementById('nav');
TABS.forEach(([id,label])=>{const b=document.createElement('button');b.textContent=label;b.dataset.t=id;
  b.onclick=()=>go(id);nav.appendChild(b);});
function go(id){CURRENT=id;document.querySelectorAll('nav button').forEach(x=>x.classList.toggle('active',x.dataset.t===id));render();}

/* ---------- HELPERS ---------- */
function el(html){const d=document.createElement('div');d.innerHTML=html.trim();return d.firstChild;}
function kpi(l,v,d,onClick){const c=el(`<div class="card kpi${onClick?' click':''}"><div class="l">${l}</div><div class="v">${v}</div>${d?`<div class="d">${d}</div>`:''}</div>`);
  if(onClick)c.onclick=onClick;return c;}
function panel(title,extra){const c=el(`<div class="card"><h3><span>${title}</span><span class="hx"></span></h3></div>`);
  if(extra)c.querySelector('.hx').innerHTML=extra;return c;}
function netNote(){return STATE.store?`<div class="callout warn">⚠️ <b>Hálózati adat</b> — ez a nézet a teljes cégre vonatkozik, telephelyre nem bontható a jelenlegi exportból (lásd adatkérő lista). A „${STATE.store}" szűrő itt nincs hatással.</div>`:'';}
function appendNote(g){const n=netNote();if(n)g.append(el(n));}
const view=document.getElementById('view');
function clear(){killCharts();view.innerHTML='';}

/* ---------- MODAL ---------- */
const modal=document.getElementById('modal'),modalbox=document.getElementById('modalbox');
modal.onclick=e=>{if(e.target===modal)closeModal();};
function openModal(title,node){modalbox.innerHTML=`<button class="x" onclick="closeModal()">✕</button><h2>${title}</h2>`;
  if(typeof node==='string')modalbox.insertAdjacentHTML('beforeend',node);else modalbox.appendChild(node);modal.hidden=false;}
function closeModal(){modal.hidden=true;modalbox.innerHTML='';}
window.closeModal=closeModal;

/* ---------- CONTROLS ---------- */
const yearSel=document.getElementById('yearSel');
DB.meta.elerheto_evek.forEach(y=>{const o=document.createElement('option');o.value=y;o.textContent=y;yearSel.appendChild(o);});
yearSel.value=STATE.year;yearSel.onchange=()=>{STATE.year=yearSel.value;buildStoreSel();render();};
const storeSel=document.getElementById('storeSel');
function buildStoreSel(){storeSel.innerHTML='<option value="">Összes telephely</option>'+STORES().map(s=>`<option>${s}</option>`).join('');storeSel.value=STATE.store||'';}
storeSel.onchange=()=>{STATE.store=storeSel.value||null;syncFilterbar();render();};
function setStore(s){STATE.store=s;storeSel.value=s||'';syncFilterbar();}
const themeBtn=document.getElementById('themeBtn');
themeBtn.onclick=()=>{STATE.theme=STATE.theme==='dark'?'light':'dark';applyTheme();render();};
function applyTheme(){document.documentElement.dataset.theme=STATE.theme;themeBtn.textContent=STATE.theme==='dark'?'🌙':'☀️';themeColors();}
function syncFilterbar(){const fb=document.getElementById('filterbar');
  fb.innerHTML=STATE.store?`<span class="chip">Telephely: <b>${STATE.store}</b><button onclick="clearStore()">✕</button></span>`:'';}
window.clearStore=()=>{setStore(null);render();};
document.getElementById('brandsub').textContent=`${DB.meta.penznem} · ${STATE.year} (jan–dec) · forrás: PTOT, ZGY, Adaos, P2025, GERDIT · csak tényadat`;

/* ---------- SEARCH ---------- */
const search=document.getElementById('search');
search.addEventListener('keydown',e=>{if(e.key==='Enter'){go('termekek');renderSearch(search.value);}});
search.addEventListener('input',()=>{if(CURRENT==='termekek')renderSearch(search.value);});

/* ============ RENDER ROUTER ============ */
function render(){clear();({attekintes:vOverview,telephely:vStore,mire:vSpending,termekek:vProducts,
  b2b:vB2B,ido:vTime,keszlet:vStock}[CURRENT])();}

/* ---- ÁTTEKINTÉS ---- */
function vOverview(){const k=Y().kpi;const g=el('<div></div>');
  const row=el('<div class="grid k4"></div>');
  row.append(
    kpi('Teljes árbevétel (áfa n.)',fmtM(k.teljes_arbevetel)+' lej',`${k.egyseg_db} telephely · ${STATE.year}`),
    kpi('Kasszás kiskeresk.',fmtM(k.kassza_arbevetel)+' lej',`${pct(k.kassza_pct)} · árrés ${pct(k.kassza_arres_pct)}`,()=>go('mire')),
    kpi('B2B számlás',fmtM(k.b2b_arbevetel)+' lej',`${pct(k.b2b_pct)} · profit ${pct(k.b2b_profit_pct)}`,()=>go('b2b')),
    kpi('Árréstömeg (kassza)',fmtM(k.kassza_arres)+' lej',`+ B2B profit ${lei(k.b2b_profit)}`));
  g.append(row);
  g.append(el(`<div class="callout">✅ <b>Adat-rekonciliáció:</b> a teljes árbevétel (${fmt(k.teljes_arbevetel)}) = kasszás (${fmt(k.kassza_arbevetel)}) + B2B (${fmt(k.b2b_arbevetel)}); eltérés ${fmt(k.rekonciliacio_elteres)} lej. <b>Becslés sehol nincs</b> — minden szám közvetlen az exportokból.</div>`));
  const g2=el('<div class="grid k2" style="margin-top:16px"></div>');
  const p1=panel('Árbevétel csatorna szerint');p1.querySelector('h3 .hx').innerHTML='<span class="tag">kattintható</span>';
  const cv1=el('<canvas></canvas>');p1.append(cv1);
  newChart(cv1,{type:'doughnut',data:{labels:['Kasszás kiskeresk.','B2B számlás'],
    datasets:[{data:[k.kassza_arbevetel,k.b2b_arbevetel],backgroundColor:[C[0],C[1]],borderWidth:0}]},
    options:{onClick:(e,els)=>{if(els.length)go(els[0].index===0?'mire':'b2b');},
      plugins:{legend:{position:'bottom'},tooltip:{callbacks:{label:c=>c.label+': '+lei(c.parsed)+' ('+pct(c.parsed/k.teljes_arbevetel*100)+')'}}}}});
  const p2=panel('Árbevétel telephelyenként');p2.querySelector('h3 .hx').innerHTML='<span class="tag">kattints egy telephelyre →</span>';
  const cv2=el('<canvas></canvas>');p2.append(cv2);const gs=Y().gestiune;
  newChart(cv2,{type:'bar',data:{labels:gs.map(x=>x.nev),datasets:[{data:gs.map(x=>x.arbevetel),backgroundColor:C[0],borderRadius:5}]},
    options:{indexAxis:'y',onClick:(e,els)=>{if(els.length){setStore(gs[els[0].index].nev);go('telephely');}},
      plugins:{legend:{display:false},tooltip:{callbacks:{label:c=>lei(c.parsed.x)+' ('+pct(gs[c.dataIndex].reszesedes_pct)+')'}}},
      scales:{x:{ticks:{callback:v=>fmtM(v)}}}}});
  g2.append(p2,p1);g.append(g2);
  // mire költenek mini
  const p3=panel('Mire költenek a vásárlók (kasszás, érték)');p3.classList.add('full');
  p3.querySelector('h3 .hx').innerHTML='<span class="tag">kattints egy csoportra →</span>';
  const cv3=el('<canvas></canvas>');p3.append(cv3);const meta=Y().adaos.meta;
  newChart(cv3,{type:'bar',data:{labels:meta.map(m=>m.meta),datasets:[{data:meta.map(m=>m.forgalom),
    backgroundColor:meta.map(m=>META_COLOR[m.meta]),borderRadius:5}]},
    options:{indexAxis:'y',onClick:(e,els)=>{if(els.length){STATE.sub.meta=meta[els[0].index].meta;go('mire');}},
      plugins:{legend:{display:false},tooltip:{callbacks:{label:c=>lei(c.parsed.x)+' ('+pct(meta[c.dataIndex].forgalom_pct)+') · árrés '+pct(meta[c.dataIndex].arres_pct)}}},
      scales:{x:{ticks:{callback:v=>fmtM(v)}}}}});
  p3.append(el('<div class="note">Az érték a kasszás eladási forgalom (áfa nélkül). A buborék/oszlop melletti % a teljes kasszás forgalomhoz viszonyított arány.</div>'));
  g.append(p3);view.append(g);}

/* ---- TELEPHELY ---- */
function vStore(){const g=el('<div></div>');
  if(!STATE.store){
    g.append(el('<div class="callout">Válassz telephelyet a fenti szűrővel vagy kattints egy oszlopra — al-dashboard nyílik az adott telephely adataival. Szűrő nélkül az összevetést látod.</div>'));
    const p=panel('Telephelyek összevetése');p.classList.add('full');
    const gs=Y().gestiune,ks=Y().keszlet_egeszseg.gestiune_keszlet;
    const tw=el('<div class="tablewrap"></div>');
    tw.innerHTML=`<table><thead><tr><th>Telephely</th><th>Árbevétel</th><th>Részesedés</th><th>Számlák</th><th>Átl. számla</th><th>Cikkszám</th><th>Forgás×</th></tr></thead><tbody>${
      gs.map(x=>{const s=ks[x.nev]||{};return `<tr class="clk" data-s="${x.nev}"><td>${x.nev}</td><td>${fmt(x.arbevetel)}</td><td>${pct(x.reszesedes_pct)}</td><td>${fmt(x.szamlak)}</td><td>${fmt(x.atlag_szamla)}</td><td>${s.cikk?fmt(s.cikk):'–'}</td><td>${s.forgas!=null?s.forgas:'–'}</td></tr>`;}).join('')}</tbody></table>`;
    p.append(tw);p.append(el('<div class="note">Forgás× = éves kiadás / átlagkészlet (mennyiségi, nagyságrendi jelzés). Kattints egy sorra a telephely al-dashboardjáért.</div>'));
    g.append(p);
    const p2=panel('Havi árbevétel telephelyenként · '+STATE.year);p2.classList.add('full');
    const cv=el('<canvas></canvas>');p2.append(cv);
    newChart(cv,{type:'line',data:{labels:MONTHS,datasets:gs.map((x,i)=>({label:x.nev,
      data:MONTHS.map((_,m)=>Y().gestiune_havi[x.nev][String(m+1).padStart(2,'0')]||0),
      borderColor:C[i%C.length],backgroundColor:'transparent',tension:.3,pointRadius:2}))},
      options:{plugins:{legend:{position:'bottom'}},scales:{y:{ticks:{callback:v=>fmt(v)}}}}});
    g.append(p2);view.append(g);
    tw.querySelectorAll('tr.clk').forEach(tr=>tr.onclick=()=>{setStore(tr.dataset.s);render();});
    return;
  }
  // store sub-dashboard
  const s=STATE.store,gobj=Y().gestiune.find(x=>x.nev===s),ks=Y().keszlet_egeszseg.gestiune_keszlet[s]||{};
  g.append(el(`<div class="bc"><a onclick="clearStore();render()">← Összes telephely</a> / <b>${s}</b></div>`));
  const row=el('<div class="grid k4"></div>');
  row.append(kpi('Árbevétel (áfa n.)',lei(gobj.arbevetel),`${pct(gobj.reszesedes_pct)} a cég forgalmából`),
    kpi('Számlák',fmt(gobj.szamlak),`átlag ${lei(gobj.atlag_szamla)}`),
    kpi('Cikkszám',fmt(ks.cikk),`forgás ${ks.forgas}×`),
    kpi('Készletprobléma',fmt((negCount(s))+ (deadCount(s))),`${negCount(s)} negatív · ${deadCount(s)} holt`,()=>{STATE.sub.stockStore=s;go('keszlet');}));
  g.append(row);
  const g2=el('<div class="grid k2" style="margin-top:16px"></div>');
  const p1=panel('Havi árbevétel · '+STATE.year);const cv1=el('<canvas></canvas>');p1.append(cv1);
  newChart(cv1,{type:'bar',data:{labels:MONTHS,datasets:[{data:MONTHS.map((_,m)=>Y().gestiune_havi[s][String(m+1).padStart(2,'0')]||0),
    backgroundColor:C[0],borderRadius:4}]},options:{plugins:{legend:{display:false},tooltip:{callbacks:{label:c=>lei(c.parsed.y)}}},scales:{y:{ticks:{callback:v=>fmt(v)}}}}});
  const p2=panel('Top 12 termék (mennyiség) — '+s);const cv2=el('<canvas></canvas>');p2.append(cv2);
  const tp=Y().termekek.filter(p=>p.st[s]).map(p=>({n:p.n,q:p.st[s].out,P:p})).filter(x=>x.q>0).sort((a,b)=>b.q-a.q).slice(0,12);
  newChart(cv2,{type:'bar',data:{labels:tp.map(x=>x.n.length>24?x.n.slice(0,22)+'…':x.n),datasets:[{data:tp.map(x=>x.q),backgroundColor:C[1],borderRadius:4}]},
    options:{indexAxis:'y',onClick:(e,els)=>{if(els.length)productDetail(tp[els[0].index].P);},plugins:{legend:{display:false}},scales:{x:{ticks:{callback:v=>fmt(v)}}}}});
  p2.append(el('<div class="note">Kattints egy termékre a részletekért. (Mennyiség db/UM — termékszintű érték nincs az exportban.)</div>'));
  g2.append(p1,p2);g.append(g2);
  g.append(el('<div class="callout">A kategória-, partner- és B2B-bontás telephelyre nem érhető el a jelenlegi exportból. A pontos telephelyi árréshez/profithoz az adatkérő lista #1 pontja kell.</div>'));
  view.append(g);}
function negCount(s){return Y().keszlet_negativ.filter(x=>x.g===s).length;}
function deadCount(s){return Y().keszlet_holt.filter(x=>x.g===s).length;}

/* ---- MIRE KÖLTENEK ---- */
function vSpending(){const g=el('<div></div>');appendNote(g);
  const meta=Y().adaos.meta,cats=Y().adaos.kategoriak,tot=Y().adaos.osszesen;
  // category filter dropdown
  const fbar=el('<div class="filters"></div>');
  const csel=el(`<select><option value="">— Ugrás kategóriához —</option>${cats.map(c=>`<option>${c.kategoria}</option>`).join('')}</select>`);
  csel.onchange=()=>{if(csel.value)categoryDetail(csel.value);};
  fbar.append(csel);g.append(fbar);
  if(!STATE.sub.meta){
    const row=el('<div class="grid k3"></div>');
    row.append(kpi('Kasszás forgalom',fmtM(tot.forgalom)+' lej','áfa nélkül'),
      kpi('Árréstömeg',fmtM(tot.adaos)+' lej',pct(tot.arres_pct)+' a forgalomra'),
      kpi('Költési csoportok',meta.length+' db'));
    g.append(row);
    const p=panel('Mire költenek — költési csoportok (érték + %)');p.classList.add('full');
    p.querySelector('.hx').innerHTML='<span class="tag">kattints egy csoportra →</span>';
    const cv=el('<canvas></canvas>');p.append(cv);
    newChart(cv,{type:'bar',data:{labels:meta.map(m=>m.meta),datasets:[{data:meta.map(m=>m.forgalom),backgroundColor:meta.map(m=>META_COLOR[m.meta]),borderRadius:5}]},
      options:{indexAxis:'y',onClick:(e,els)=>{if(els.length){STATE.sub.meta=meta[els[0].index].meta;render();}},
        plugins:{legend:{display:false},tooltip:{callbacks:{label:c=>lei(c.parsed.x)+' ('+pct(meta[c.dataIndex].forgalom_pct)+') · árrés '+pct(meta[c.dataIndex].arres_pct)}}},scales:{x:{ticks:{callback:v=>fmtM(v)}}}}});
    const tw=el('<div class="tablewrap" style="margin-top:8px"></div>');
    tw.innerHTML=`<table><thead><tr><th>Költési csoport</th><th>Forgalom</th><th>% forgalom</th><th>Árrés</th><th>Árrés%</th></tr></thead><tbody>${
      meta.map(m=>`<tr class="clk" data-m="${m.meta}"><td><span class="swatch" style="background:${META_COLOR[m.meta]}"></span>${m.meta}</td><td>${fmt(m.forgalom)}</td><td>${pct(m.forgalom_pct)}</td><td>${fmt(m.adaos)}</td><td>${pct(m.arres_pct)}</td></tr>`).join('')}</tbody></table>`;
    p.append(tw);g.append(p);view.append(g);
    tw.querySelectorAll('tr.clk').forEach(tr=>tr.onclick=()=>{STATE.sub.meta=tr.dataset.m;render();});
    return;
  }
  // drilled into a meta
  const m=meta.find(x=>x.meta===STATE.sub.meta);const inCats=cats.filter(c=>c.meta===STATE.sub.meta).sort((a,b)=>b.forgalom-a.forgalom);
  g.append(el(`<div class="bc"><a id="back">← Költési csoportok</a> / <b>${m.meta}</b></div>`));
  const row=el('<div class="grid k3"></div>');
  row.append(kpi(m.meta+' — forgalom',lei(m.forgalom),pct(m.forgalom_pct)+' a kasszás forgalomból'),
    kpi('Árréstömeg',lei(m.adaos),pct(m.arres_pct)+' árrés'),kpi('Kategóriák',inCats.length+' db'));
  g.append(row);
  const p=panel(m.meta+' — kategóriák');p.classList.add('full');p.querySelector('.hx').innerHTML='<span class="tag">kattints egy kategóriára →</span>';
  const cv=el('<canvas></canvas>');p.append(cv);
  newChart(cv,{type:'bar',data:{labels:inCats.map(c=>c.kategoria),datasets:[{data:inCats.map(c=>c.forgalom),backgroundColor:META_COLOR[m.meta],borderRadius:4}]},
    options:{indexAxis:'y',onClick:(e,els)=>{if(els.length)categoryDetail(inCats[els[0].index].kategoria);},
      plugins:{legend:{display:false},tooltip:{callbacks:{label:c=>lei(c.parsed.x)+' ('+pct(inCats[c.dataIndex].forgalom_pct)+')'}}},scales:{x:{ticks:{callback:v=>fmt(v)}}}}});
  const tw=el('<div class="tablewrap" style="margin-top:8px"></div>');
  tw.innerHTML=`<table><thead><tr><th>Kategória</th><th>Forgalom</th><th>% forgalom</th><th>Árrés%</th><th>Áfa%</th></tr></thead><tbody>${
    inCats.map(c=>`<tr class="clk" data-c="${c.kategoria}"><td>${c.kategoria}</td><td>${fmt(c.forgalom)}</td><td>${pct(c.forgalom_pct)}</td><td><span class="pill ${c.arres_pct>=26?'good':c.arres_pct<15?'bad':'warn'}">${pct(c.arres_pct)}</span></td><td>${pct(c.tva_pct)}</td></tr>`).join('')}</tbody></table>`;
  p.append(tw);g.append(p);view.append(g);
  document.getElementById('back').onclick=()=>{STATE.sub.meta=null;render();};
  tw.querySelectorAll('tr.clk').forEach(tr=>tr.onclick=()=>categoryDetail(tr.dataset.c));}

function categoryDetail(catName){const c=Y().adaos.kategoriak.find(x=>x.kategoria===catName);
  const prods=Y().termekek.filter(p=>p.cat===catName).sort((a,b)=>b.ie-a.ie);
  const totQ=prods.reduce((s,p)=>s+p.ie,0)||1;
  const box=el('<div></div>');
  box.append(el(`<div class="grid k3">
    <div class="card kpi"><div class="l">Forgalom</div><div class="v">${fmt(c?c.forgalom:0)}</div><div class="d">${pct(c?c.forgalom_pct:0)} a kasszás forgalomból</div></div>
    <div class="card kpi"><div class="l">Árrés</div><div class="v">${fmt(c?c.adaos:0)}</div><div class="d">${pct(c?c.arres_pct:0)} · áfa ${pct(c?c.tva_pct:0)}</div></div>
    <div class="card kpi"><div class="l">Termékek (besorolt)</div><div class="v">${prods.length}</div><div class="d">mennyiség alapú</div></div></div>`));
  box.append(el(`<div class="note" style="margin:12px 0">Csoport: <b>${c?c.meta:'—'}</b>. A termékek <b>mennyiség</b> szerint (db/UM) — a termékszintű forgalom (érték) nem szerepel az exportban, ezért itt a kategórián belüli <b>mennyiségi részesedést</b> mutatjuk.</div>`));
  const tw=el('<div class="tablewrap"></div>');
  tw.innerHTML=`<table><thead><tr><th>Termék</th><th>Mennyiség</th><th>% (menny.)</th><th>Egységek</th></tr></thead><tbody>${
    prods.slice(0,80).map(p=>`<tr class="clk" data-n="${encodeURIComponent(p.n)}"><td>${p.n}</td><td>${fmt(p.ie)}</td><td>${pct(p.ie/totQ*100)}</td><td>${p.eg}</td></tr>`).join('')}</tbody></table>`;
  box.append(tw);openModal('Kategória: '+catName,box);
  tw.querySelectorAll('tr.clk').forEach(tr=>tr.onclick=()=>{const p=Y().termekek.find(x=>x.n===decodeURIComponent(tr.dataset.n));productDetail(p);});}

/* ---- TERMÉKEK (kereső) ---- */
function vProducts(){const g=el('<div></div>');
  g.append(el('<div class="card"><h3>Termékkereső</h3><div class="note">Írj a fenti keresőbe, vagy ide. Egy termékre kattintva minden elérhető információt látsz (kategória, költési csoport, telephelyenkénti készletmozgás).</div><input id="psearch" placeholder="🔎 pl. bere, cafea, paine…" style="width:100%;margin-top:10px"/><div id="presults" style="margin-top:14px"></div></div>'));
  view.append(g);const ps=document.getElementById('psearch');ps.value=search.value;
  ps.addEventListener('input',()=>{search.value=ps.value;renderSearch(ps.value);});
  renderSearch(search.value);}
function renderSearch(q){const box=document.getElementById('presults');if(!box)return;q=(q||'').trim().toLowerCase();
  if(q.length<2){box.innerHTML='<div class="muted">Írj legalább 2 karaktert…</div>';return;}
  const res=Y().termekek.filter(p=>p.n.toLowerCase().includes(q)).slice(0,60);
  box.innerHTML=res.length?'':'<div class="muted">Nincs találat.</div>';
  res.forEach(p=>{const r=el(`<div class="result"><div class="n">${p.n}</div><div class="tag"><span class="swatch" style="background:${META_COLOR[p.meta]}"></span>${p.meta} · ${p.cat} · ${fmt(p.ie)} ${p.um} · ${p.eg} telephely</div></div>`);
    r.onclick=()=>productDetail(p);box.append(r);});
  if(Y().termekek.filter(p=>p.n.toLowerCase().includes(q)).length>60)box.append(el('<div class="note">Csak az első 60 találat látszik — finomítsd a keresést.</div>'));}
function productDetail(p){if(!p)return;const box=el('<div></div>');
  const totQ=p.ie||1;
  box.append(el(`<div class="grid k3">
    <div class="card kpi"><div class="l">Összes kiadás (eladás)</div><div class="v">${fmt(p.ie)}</div><div class="d">${p.um}</div></div>
    <div class="card kpi"><div class="l">Költési csoport</div><div class="v" style="font-size:18px">${p.meta}</div><div class="d">kategória: ${p.cat}</div></div>
    <div class="card kpi"><div class="l">Telephelyek</div><div class="v">${p.eg}</div><div class="d">ahol forgalmazzák</div></div></div>`));
  box.append(el('<div class="note" style="margin:12px 0">Telephelyenkénti készletmozgás (mennyiség, UM='+p.um+'). Kattints a kategóriára a csoport többi termékéért.</div>'));
  const rows=Object.entries(p.st).map(([s,v])=>`<tr><td>${s}</td><td>${fmt(v.si)}</td><td>${fmt(v.in)}</td><td>${fmt(v.out)}</td><td>${fmt(v.sf)}</td><td>${pct(v.out/totQ*100)}</td></tr>`).join('');
  const tw=el('<div class="tablewrap"></div>');
  tw.innerHTML=`<table><thead><tr><th>Telephely</th><th>Nyitó</th><th>Be</th><th>Ki (eladás)</th><th>Záró</th><th>% kiadásból</th></tr></thead><tbody>${rows}</tbody></table>`;
  box.append(tw);
  const link=el(`<div style="margin-top:12px"><span class="linklike">→ ${p.cat} kategória részletei</span></div>`);
  link.querySelector('.linklike').onclick=()=>{closeModal();categoryDetail(p.cat);};box.append(link);
  openModal('Termék: '+p.n,box);}

/* ---- B2B & PARTNEREK ---- */
function vB2B(){const g=el('<div></div>');appendNote(g);const p=Y().partnerek,s=Y().szamlas_ossz;
  const row=el('<div class="grid k4"></div>');
  row.append(kpi('B2B forgalom',fmtM(p.osszesen)+' lej','áfa nélkül'),kpi('Profit',lei(s.profit),pct(s.profit_pct)),
    kpi('Partnerek',p.darab+' db',`top5 ${pct(p.top5_pct)} · top10 ${pct(p.top10_pct)}`),
    kpi('HHI koncentráció',fmt(p.hhi),p.hhi>2500?'magas':p.hhi>1500?'közepes':'alacsony'));
  g.append(row);
  const pp=panel('Pareto — vevők és kumulált részesedés');pp.classList.add('full');const cv=el('<canvas></canvas>');pp.append(cv);
  const top=p.lista.slice(0,15);
  newChart(cv,{data:{labels:top.map(x=>x.partner.length>20?x.partner.slice(0,18)+'…':x.partner),
    datasets:[{type:'bar',data:top.map(x=>x.ertek),backgroundColor:C[0],borderRadius:4,yAxisID:'y'},
      {type:'line',data:top.map(x=>x.kumulativ_pct),borderColor:C[3],tension:.2,pointRadius:3,yAxisID:'y1'}]},
    options:{onClick:(e,els)=>{if(els.length)partnerDetail(top[els[0].index]);},plugins:{legend:{display:false}},
      scales:{y:{ticks:{callback:v=>fmt(v)}},y1:{position:'right',min:0,max:100,ticks:{callback:v=>v+'%'},grid:{drawOnChartArea:false}}}}});
  g.append(pp);
  const lp=panel('Partnerlista');lp.classList.add('full');const tw=el('<div class="tablewrap"></div>');
  tw.innerHTML=`<table><thead><tr><th>#</th><th>Partner</th><th>Település</th><th>Érték</th><th>% forgalom</th><th>Kumul.</th></tr></thead><tbody>${
    p.lista.map((x,i)=>`<tr class="clk" data-i="${i}"><td>${i+1}</td><td>${x.partner}</td><td class="tag">${x.telepules}</td><td>${fmt(x.ertek)}</td><td>${pct(x.reszesedes_pct)}</td><td>${pct(x.kumulativ_pct)}</td></tr>`).join('')}</tbody></table>`;
  lp.append(tw);g.append(lp);view.append(g);
  tw.querySelectorAll('tr.clk').forEach(tr=>tr.onclick=()=>partnerDetail(p.lista[+tr.dataset.i]));}
function partnerDetail(x){openModal('Partner: '+x.partner,
  `<div class="grid k3"><div class="card kpi"><div class="l">Éves érték (áfa n.)</div><div class="v">${fmt(x.ertek)}</div></div>
   <div class="card kpi"><div class="l">% a B2B forgalomból</div><div class="v">${pct(x.reszesedes_pct)}</div></div>
   <div class="card kpi"><div class="l">Település</div><div class="v" style="font-size:18px">${x.telepules||'–'}</div></div></div>
   <div class="note" style="margin-top:12px">A partnerenkénti idő-/profitbontás a jelenlegi exportból nem érhető el (lásd adatkérő #2: számlaszintű lista vevővel és önköltséggel).</div>`);}

/* ---- IDŐ & RITMUS ---- */
function vTime(){const g=el('<div></div>');appendNote(g);
  const gm=Y().gerdit_havi,sm=Y().szamlas_havi,hr=Y().heti_ritmus;
  const p1=panel('Teljes árbevétel vs. B2B számlás — havonta · '+STATE.year);p1.classList.add('full');const cv1=el('<canvas></canvas>');p1.append(cv1);
  newChart(cv1,{data:{labels:MONTHS,datasets:[
    {type:'bar',label:'Teljes árbevétel',data:gm.map(x=>x.arbevetel),backgroundColor:'rgba(79,140,255,.4)'},
    {type:'line',label:'B2B számlás',data:sm.map(x=>x.ertek),borderColor:C[1],tension:.3}]},
    options:{plugins:{legend:{position:'bottom'}},scales:{y:{ticks:{callback:v=>fmt(v)}}}}});
  p1.append(el('<div class="note">A teljes árbevételnek nyári csúcsa van, de nincs novemberi gödre — a novemberi visszaesés kizárólag a B2B csatorna jelensége.</div>'));
  g.append(p1);
  const g2=el('<div class="grid k2" style="margin-top:16px"></div>');
  const p2=panel('Heti ritmus — B2B értékesítés napok szerint');const cv2=el('<canvas></canvas>');p2.append(cv2);
  newChart(cv2,{type:'bar',data:{labels:hr.map(d=>d.nap),datasets:[{data:hr.map(d=>d.ertek),
    backgroundColor:hr.map(d=>d.ertek>100000?C[3]:C[0]),borderRadius:4}]},
    options:{plugins:{legend:{display:false},tooltip:{callbacks:{label:c=>lei(c.parsed.y)+' ('+pct(hr[c.dataIndex].ertek_pct)+') · '+hr[c.dataIndex].napok+' nap'}}},scales:{y:{ticks:{callback:v=>fmt(v)}}}}});
  p2.append(el('<div class="note">A B2B forgalom <b>kedd + péntek</b> köré tömörül — ez a kiszállítási/körjárat-rend. A piros oszlopok a fő szállítási napok.</div>'));
  const p3=panel('B2B profit% havonta · '+STATE.year);const cv3=el('<canvas></canvas>');p3.append(cv3);
  newChart(cv3,{type:'line',data:{labels:MONTHS,datasets:[{data:sm.map(x=>x.profit_pct),borderColor:C[2],
    backgroundColor:'rgba(240,160,32,.15)',fill:true,tension:.3}]},options:{plugins:{legend:{display:false}},scales:{y:{ticks:{callback:v=>v+'%'}}}}});
  g2.append(p2,p3);g.append(g2);
  const tw=el('<div class="card full"><h3>Heti ritmus — részletes</h3></div>');
  const t=el('<div class="tablewrap"></div>');
  t.innerHTML=`<table><thead><tr><th>Nap</th><th>Aktív napok</th><th>Forgalom</th><th>% forgalom</th><th>Átlag/nap</th><th>Profit%</th></tr></thead><tbody>${
    hr.map(d=>`<tr><td>${d.nap}</td><td>${d.napok}</td><td>${fmt(d.ertek)}</td><td>${pct(d.ertek_pct)}</td><td>${fmt(d.atlag_nap)}</td><td>${pct(d.profit_pct)}</td></tr>`).join('')}</tbody></table>`;
  tw.append(t);g.append(tw);view.append(g);}

/* ---- KÉSZLET ---- */
function vStock(){const g=el('<div></div>');const ke=Y().keszlet_egeszseg;
  const storeFilter=STATE.store;
  const neg=Y().keszlet_negativ.filter(x=>!storeFilter||x.g===storeFilter);
  const dead=Y().keszlet_holt.filter(x=>!storeFilter||x.g===storeFilter);
  if(storeFilter)g.append(el(`<div class="bc"><a onclick="clearStore();render()">← Összes telephely</a> / <b>${storeFilter}</b> készlete</div>`));
  const row=el('<div class="grid k4"></div>');
  row.append(kpi('Vizsgált cikksor',fmt(storeFilter?(Y().keszlet_egeszseg.gestiune_keszlet[storeFilter]||{}).cikk:ke.osszes_cikksor)),
    kpi('⚠️ Negatív készlet',fmt(neg.length),'kattints a listáért',()=>stockList('Negatív készlet',neg,'neg')),
    kpi('🟡 Holt készlet',fmt(dead.length),'kattints a listáért',()=>stockList('Holt készlet (0 éves eladás)',dead,'dead')),
    kpi('Kategorizálás',pct(ke.kategorizalas_lefedettseg_pct),'automatikus besorolás'));
  g.append(row);
  g.append(el('<div class="callout">📄 Tételes Excel: <b>Keszlet_problemak_2025.xlsx</b>. A KPI-kártyákra kattintva a szűrhető lista is megnyílik itt.</div>'));
  const g2=el('<div class="grid k2" style="margin-top:4px"></div>');
  // negatív/holt telephelyenként
  const gs=STORES();
  const p1=panel('Készletproblémák telephelyenként');const cv1=el('<canvas></canvas>');p1.append(cv1);
  newChart(cv1,{type:'bar',data:{labels:gs,datasets:[
    {label:'Negatív',data:gs.map(s=>Y().keszlet_negativ.filter(x=>x.g===s).length),backgroundColor:C[3],borderRadius:4},
    {label:'Holt',data:gs.map(s=>Y().keszlet_holt.filter(x=>x.g===s).length),backgroundColor:C[2],borderRadius:4}]},
    options:{onClick:(e,els)=>{if(els.length){setStore(gs[els[0].index]);render();}},plugins:{legend:{position:'bottom'}}}});
  p1.append(el('<div class="note">Kattints egy telephelyre a szűréshez. A ZETEKINCSE (új bolt) kiugró holt készlete a túl széles nyitó szortimentből ered.</div>'));
  const p2=panel('Szortiment-átfedés (hány telephelyen van egy cikk)');const cv2=el('<canvas></canvas>');p2.append(cv2);const ov=Y().szortiment_atfedes;
  newChart(cv2,{type:'bar',data:{labels:Object.keys(ov).map(k=>k+' telephely'),datasets:[{data:Object.values(ov),backgroundColor:C[0],borderRadius:4}]},
    options:{plugins:{legend:{display:false}}}});
  g2.append(p1,p2);g.append(g2);view.append(g);
  if(STATE.sub.stockStore){STATE.sub.stockStore=null;} // consumed
}
function stockList(title,arr,kind){const box=el('<div></div>');
  const cats=[...new Set(arr.map(x=>x.cat))].sort();
  box.append(el(`<div class="filters"><input id="sf" placeholder="🔎 szűrés névre…" style="flex:1"/><select id="sc"><option value="">Minden kategória</option>${cats.map(c=>`<option>${c}</option>`).join('')}</select></div>`));
  const tw=el('<div class="tablewrap"></div>');box.append(tw);
  const head=kind==='neg'?'<tr><th>Telephely</th><th>Termék</th><th>Kategória</th><th>Nyitó</th><th>Be</th><th>Ki</th><th>Záró</th></tr>'
                         :'<tr><th>Telephely</th><th>Termék</th><th>Kategória</th><th>Bevét</th><th>Zárókészlet</th></tr>';
  function draw(){const q=(box.querySelector('#sf').value||'').toLowerCase(),c=box.querySelector('#sc').value;
    const rows=arr.filter(x=>(!q||x.n.toLowerCase().includes(q))&&(!c||x.cat===c)).slice(0,400);
    tw.innerHTML=`<table><thead>${head}</thead><tbody>${rows.map(x=>kind==='neg'
      ?`<tr><td>${x.g}</td><td>${x.n}</td><td class="tag">${x.cat}</td><td>${fmt(x.si)}</td><td>${fmt(x.in)}</td><td>${fmt(x.out)}</td><td><span class="pill bad">${fmt(x.sf)}</span></td></tr>`
      :`<tr><td>${x.g}</td><td>${x.n}</td><td class="tag">${x.cat}</td><td>${fmt(x.in)}</td><td>${fmt(x.sf)}</td></tr>`).join('')}</tbody></table>
      <div class="note">${arr.length} tétel${arr.length>400?' (első 400 látszik — szűkíts)':''}.</div>`;}
  box.querySelector('#sf').addEventListener('input',draw);box.querySelector('#sc').addEventListener('change',draw);draw();
  openModal(title+(STATE.store?(' — '+STATE.store):''),box);}

/* ---------- INIT ---------- */
buildStoreSel();applyTheme();syncFilterbar();go('attekintes');
</script>
</body>
</html>'''

out = HTML.replace('__CHARTJS__', CHARTJS).replace('__DATA__', DATA)
with open(P('Dashboard_2025.html'),'w',encoding='utf-8') as f: f.write(out)
print('Dashboard v2 mentve:', P('Dashboard_2025.html'), '(', len(out)//1024, 'KB )')
