#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Önálló, offline interaktív dashboard generálása a dashboard_data.json-ból."""
import json, os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def P(n): return os.path.join(BASE,n)
DATA = open(P('_build/dashboard_data.json'),encoding='utf-8').read()
CHARTJS = open(P('_build/chart.umd.min.js'),encoding='utf-8').read()

HTML = r'''<!DOCTYPE html>
<html lang="hu">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Gergely István — 2025 üzleti dashboard</title>
<style>
:root{
  --bg:#0d1117; --panel:#161b22; --panel2:#1c2330; --line:#283041;
  --txt:#e6edf3; --muted:#8b98a9; --accent:#4f8cff; --accent2:#36c5a0;
  --warn:#f0a020; --bad:#f0506e; --good:#36c5a0;
  --c1:#4f8cff;--c2:#36c5a0;--c3:#f0a020;--c4:#f0506e;--c5:#a06bff;--c6:#ff8a5c;
}
*{box-sizing:border-box}
body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  background:var(--bg);color:var(--txt);font-size:14px;line-height:1.45}
header{padding:22px 28px 14px;border-bottom:1px solid var(--line);position:sticky;top:0;background:rgba(13,17,23,.92);
  backdrop-filter:blur(8px);z-index:20}
h1{margin:0;font-size:20px;letter-spacing:.2px}
.sub{color:var(--muted);font-size:13px;margin-top:3px}
nav{display:flex;gap:6px;flex-wrap:wrap;margin-top:14px}
nav button{background:var(--panel);color:var(--muted);border:1px solid var(--line);padding:7px 14px;border-radius:8px;
  cursor:pointer;font-size:13px;transition:.15s}
nav button:hover{color:var(--txt);border-color:var(--accent)}
nav button.active{background:var(--accent);color:#fff;border-color:var(--accent)}
main{padding:22px 28px 60px;max-width:1280px;margin:0 auto}
.tab{display:none;animation:fade .25s} .tab.active{display:block}
@keyframes fade{from{opacity:0;transform:translateY(4px)}to{opacity:1;transform:none}}
.grid{display:grid;gap:16px}
.k4{grid-template-columns:repeat(4,1fr)} .k3{grid-template-columns:repeat(3,1fr)} .k2{grid-template-columns:repeat(2,1fr)}
@media(max-width:900px){.k4,.k3,.k2{grid-template-columns:1fr 1fr}}
@media(max-width:600px){.k4,.k3,.k2{grid-template-columns:1fr}}
.card{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:18px}
.kpi .v{font-size:26px;font-weight:700;margin:6px 0 2px}
.kpi .l{color:var(--muted);font-size:12px;text-transform:uppercase;letter-spacing:.5px}
.kpi .d{font-size:12px;color:var(--accent2)}
.card h3{margin:0 0 14px;font-size:15px}
.card.full{margin-top:16px}
canvas{max-height:340px}
table{width:100%;border-collapse:collapse;font-size:13px}
th,td{text-align:right;padding:8px 10px;border-bottom:1px solid var(--line)}
th:first-child,td:first-child{text-align:left}
th{color:var(--muted);font-weight:600;font-size:11px;text-transform:uppercase;letter-spacing:.4px;position:sticky;top:0;background:var(--panel)}
tr:hover td{background:var(--panel2)}
.tablewrap{max-height:480px;overflow:auto;border-radius:8px}
.pill{display:inline-block;padding:2px 8px;border-radius:20px;font-size:11px;font-weight:600}
.pill.bad{background:rgba(240,80,110,.15);color:var(--bad)} .pill.warn{background:rgba(240,160,32,.15);color:var(--warn)}
.pill.good{background:rgba(54,197,160,.15);color:var(--good)}
.note{color:var(--muted);font-size:12px;margin-top:8px;line-height:1.5}
.bar-mini{height:6px;background:var(--line);border-radius:3px;overflow:hidden;margin-top:4px}
.bar-mini>i{display:block;height:100%;background:var(--accent)}
.flex{display:flex;justify-content:space-between;align-items:center;gap:10px}
.tag{font-size:11px;color:var(--muted)}
select{background:var(--panel2);color:var(--txt);border:1px solid var(--line);border-radius:6px;padding:5px 8px}
.legend-inline{display:flex;gap:14px;flex-wrap:wrap;font-size:12px;color:var(--muted);margin-bottom:8px}
.legend-inline i{display:inline-block;width:10px;height:10px;border-radius:2px;margin-right:5px;vertical-align:middle}
.callout{border-left:3px solid var(--accent2);background:var(--panel2);padding:12px 14px;border-radius:0 8px 8px 0;margin-top:14px;font-size:13px}
</style>
</head>
<body>
<header>
  <h1>Gergely István — 2025 üzleti dashboard</h1>
  <div class="sub">Romániai kis- &amp; nagykereskedés · 6 telephely · forrás: PTOT, ZGY, Adaos, P2025 SZAMLA, GERDIT · érték: RON (lej), áfa nélkül ahol jelölve</div>
  <nav id="nav"></nav>
</header>
<main id="main"></main>

<script>__CHARTJS__</script>
<script>
const D = __DATA__;
const fmt = n => (n==null?'–':Number(n).toLocaleString('hu-HU',{maximumFractionDigits:0}));
const fmtM = n => (n/1e6).toLocaleString('hu-HU',{maximumFractionDigits:2})+' M';
const pct = n => (n==null?'–':Number(n).toLocaleString('hu-HU',{maximumFractionDigits:1})+'%');
const C=['#4f8cff','#36c5a0','#f0a020','#f0506e','#a06bff','#ff8a5c'];
Chart.defaults.color='#8b98a9'; Chart.defaults.borderColor='#283041'; Chart.defaults.font.family='-apple-system,Segoe UI,Roboto,sans-serif';
const HU={'01':'Jan','02':'Feb','03':'Már','04':'Ápr','05':'Máj','06':'Jún','07':'Júl','08':'Aug','09':'Szep','10':'Okt','11':'Nov','12':'Dec'};

const TABS=[
 ['attekintes','Áttekintés'],['gestiune','Telephelyek'],['kategoria','Árrés / kategória'],
 ['partnerek','B2B partnerek'],['ido','Időbeli trend'],['keszlet','Készlet-egészség'],['afa','Áfa & mix']
];
const nav=document.getElementById('nav'), main=document.getElementById('main');
TABS.forEach(([id,label],i)=>{
  const b=document.createElement('button'); b.textContent=label; b.dataset.t=id; if(i===0)b.classList.add('active');
  b.onclick=()=>{document.querySelectorAll('nav button').forEach(x=>x.classList.remove('active'));b.classList.add('active');
    document.querySelectorAll('.tab').forEach(x=>x.classList.remove('active'));document.getElementById('tab-'+id).classList.add('active');};
  nav.appendChild(b);
  const d=document.createElement('section'); d.className='tab'+(i===0?' active':''); d.id='tab-'+id; main.appendChild(d);
});
const kpiCard=(l,v,d)=>`<div class="card kpi"><div class="l">${l}</div><div class="v">${v}</div>${d?`<div class="d">${d}</div>`:''}</div>`;
function chart(parent,title,cfg,note){const c=document.createElement('div');c.className='card';
  c.innerHTML=`<h3>${title}</h3><canvas></canvas>${note?`<div class="note">${note}</div>`:''}`;parent.appendChild(c);
  new Chart(c.querySelector('canvas'),cfg);}

/* ---- ÁTTEKINTÉS ---- */
(()=>{const t=document.getElementById('tab-attekintes');const k=D.kpi;
 t.innerHTML=`<div class="grid k4">
   ${kpiCard('Teljes árbevétel (áfa n.)',fmtM(k.teljes_arbevetel)+' lej','6 telephely összesen')}
   ${kpiCard('Kasszás kiskeresk.',fmtM(k.kassza_arbevetel)+' lej',k.kassza_pct+'% · árrés '+pct(k.kassza_arres_pct))}
   ${kpiCard('B2B számlás',fmtM(k.b2b_arbevetel)+' lej',k.b2b_pct+'% · profit '+pct(k.b2b_profit_pct))}
   ${kpiCard('Árréstömeg (kassza)',fmtM(k.kassza_arres)+' lej','+ B2B profit '+fmt(k.b2b_profit)+' lej')}
 </div>
 <div class="callout">✅ <b>Adat-rekonciliáció:</b> GERDIT (${fmt(k.teljes_arbevetel)}) = kasszás (${fmt(k.kassza_arbevetel)}) + B2B (${fmt(k.b2b_arbevetel)}). Eltérés mindössze ${fmt(k.rekonciliacio_elteres)} lej (0,02%) → a három fájl ugyanazt a teljes árbevételt írja le.</div>`;
 const g1=document.createElement('div');g1.className='grid k2 card-wrap';g1.style.marginTop='16px';t.appendChild(g1);
 chart(g1,'Árbevétel csatorna szerint',{type:'doughnut',data:{labels:['Kasszás kiskeresk.','B2B számlás'],
   datasets:[{data:[k.kassza_arbevetel,k.b2b_arbevetel],backgroundColor:[C[0],C[1]],borderWidth:0}]},
   options:{plugins:{legend:{position:'bottom'}}}});
 chart(g1,'Árbevétel telephelyenként',{type:'bar',data:{labels:D.gestiune.map(x=>x.nev),
   datasets:[{data:D.gestiune.map(x=>x.arbevetel),backgroundColor:C[0],borderRadius:5}]},
   options:{indexAxis:'y',plugins:{legend:{display:false}},scales:{x:{ticks:{callback:v=>fmtM(v)}}}}});
})();

/* ---- TELEPHELYEK ---- */
(()=>{const t=document.getElementById('tab-gestiune');
 let rows=D.gestiune.map(g=>{const ks=D.keszlet_egeszseg.gestiune_keszlet[g.nev]||{};return `<tr>
   <td>${g.nev}</td><td>${fmt(g.arbevetel)}</td><td>${pct(g.reszesedes_pct)}</td><td>${fmt(g.szamlak)}</td>
   <td>${fmt(g.atlag_szamla)}</td><td>${ks.cikk?fmt(ks.cikk):'–'}</td><td>${ks.forgas!=null?ks.forgas+'×':'–'}</td></tr>`;}).join('');
 t.innerHTML=`<div class="card"><h3>Telephelyek összevetése</h3><div class="tablewrap"><table>
   <thead><tr><th>Telephely</th><th>Árbevétel</th><th>Részesedés</th><th>Számlák</th><th>Átl. számla</th><th>Cikkszám</th><th>Forgás*</th></tr></thead>
   <tbody>${rows}</tbody></table></div><div class="note">*Forgás = éves kiadás / átlagkészlet (mennyiségi, vegyes UM — nagyságrendi jelzés). Magasabb = gyorsabb áruforgás.</div></div>
   <div class="grid k2" style="margin-top:16px"><div class="card"><h3>Havi árbevétel telephelyenként <select id="gsel"></select></h3><canvas id="gmon"></canvas><div class="note">A ZETEKINCSE év közben nyílt → felfutó pálya.</div></div>
   <div class="card"><h3>Átlagos számlaérték</h3><canvas id="gavg"></canvas><div class="note">A nagykereskedés sok kis tételt számláz; a boltok kevesebb, nagyobb bizonylatot.</div></div></div>`;
 const sel=document.getElementById('gsel');Object.keys(D.gestiune_havi).forEach(g=>{const o=document.createElement('option');o.value=g;o.textContent=g;sel.appendChild(o);});
 const months=Object.keys(D.gestiune_havi[D.gestiune[0].nev]);
 let gc=new Chart(document.getElementById('gmon'),{type:'line',data:{labels:months.map(m=>HU[m]),
   datasets:[{label:sel.value,data:months.map(m=>D.gestiune_havi[sel.value][m]||0),borderColor:C[0],backgroundColor:'rgba(79,140,255,.15)',fill:true,tension:.3}]},
   options:{plugins:{legend:{display:false}},scales:{y:{ticks:{callback:v=>fmt(v)}}}}});
 sel.onchange=()=>{gc.data.datasets[0].label=sel.value;gc.data.datasets[0].data=months.map(m=>D.gestiune_havi[sel.value][m]||0);gc.update();};
 new Chart(document.getElementById('gavg'),{type:'bar',data:{labels:D.gestiune.map(x=>x.nev),
   datasets:[{data:D.gestiune.map(x=>x.atlag_szamla),backgroundColor:C[2],borderRadius:5}]},
   options:{plugins:{legend:{display:false}},scales:{y:{ticks:{callback:v=>fmt(v)}}}}});
})();

/* ---- KATEGÓRIA / ÁRRÉS ---- */
(()=>{const t=document.getElementById('tab-kategoria');const cats=D.adaos.kategoriak.filter(c=>c.forgalom>1000);
 t.innerHTML=`<div class="grid k3">
   ${kpiCard('Kasszás forgalom',fmtM(D.adaos.osszesen.forgalom)+' lej')}
   ${kpiCard('Árréstömeg',fmtM(D.adaos.osszesen.adaos)+' lej',pct(D.adaos.osszesen.arres_pct)+' a forgalomra')}
   ${kpiCard('Kategóriák',D.adaos.kategoriak.length+' db')}
 </div>
 <div class="card full"><h3>Forgalom vs. árrés% — buborék = árréstömeg</h3>
 <div class="legend-inline"><span><i style="background:#36c5a0"></i>magas árrés (jövedelmező)</span><span><i style="background:#f0506e"></i>alacsony árrés (volumen)</span></div>
 <canvas id="scatter"></canvas><div class="note">Jobbra-fent = nagy forgalom + jó árrés (ideális). Lent-jobbra = nagy forgalmú, de gyenge árrésű (pl. cigaretta).</div></div>
 <div class="grid k2" style="margin-top:16px">
 <div class="card"><h3>Top 10 árréstömeg szerint</h3><canvas id="topadaos"></canvas></div>
 <div class="card"><h3>Top / leggyengébb árrés%</h3><canvas id="arrespct"></canvas></div></div>
 <div class="card full"><h3>Összes kategória</h3><div class="tablewrap"><table><thead><tr><th>Kategória</th><th>Forgalom</th><th>Árrés</th><th>Árrés%</th><th>Áfa%</th></tr></thead>
 <tbody>${D.adaos.kategoriak.map(c=>`<tr><td>${c.kategoria}</td><td>${fmt(c.forgalom)}</td><td>${fmt(c.adaos)}</td><td><span class="pill ${c.arres_pct>=26?'good':c.arres_pct<15?'bad':'warn'}">${pct(c.arres_pct)}</span></td><td>${pct(c.tva_pct)}</td></tr>`).join('')}</tbody></table></div></div>`;
 new Chart(document.getElementById('scatter'),{type:'bubble',data:{datasets:cats.map((c,i)=>({label:c.kategoria,
   data:[{x:c.forgalom,y:c.arres_pct,r:Math.max(4,Math.sqrt(c.adaos)/30)}],
   backgroundColor:c.arres_pct>=26?'rgba(54,197,160,.6)':c.arres_pct<15?'rgba(240,80,110,.6)':'rgba(240,160,32,.55)'}))},
   options:{plugins:{legend:{display:false},tooltip:{callbacks:{label:ctx=>ctx.dataset.label+': forg '+fmt(ctx.raw.x)+', árrés '+pct(ctx.raw.y)}}},
   scales:{x:{title:{display:true,text:'Forgalom (lej)'},ticks:{callback:v=>fmtM(v)}},y:{title:{display:true,text:'Árrés %'}}}}});
 const top10=[...D.adaos.kategoriak].sort((a,b)=>b.adaos-a.adaos).slice(0,10);
 new Chart(document.getElementById('topadaos'),{type:'bar',data:{labels:top10.map(c=>c.kategoria),
   datasets:[{data:top10.map(c=>c.adaos),backgroundColor:C[1],borderRadius:4}]},
   options:{indexAxis:'y',plugins:{legend:{display:false}},scales:{x:{ticks:{callback:v=>fmt(v)}}}}});
 const big=D.adaos.kategoriak.filter(c=>c.forgalom>20000);const hi=[...big].sort((a,b)=>b.arres_pct-a.arres_pct).slice(0,5);
 const lo=[...big].sort((a,b)=>a.arres_pct-b.arres_pct).slice(0,5);const mix=[...hi,...lo];
 new Chart(document.getElementById('arrespct'),{type:'bar',data:{labels:mix.map(c=>c.kategoria),
   datasets:[{data:mix.map(c=>c.arres_pct),backgroundColor:mix.map((c,i)=>i<5?C[1]:C[3]),borderRadius:4}]},
   options:{indexAxis:'y',plugins:{legend:{display:false}},scales:{x:{ticks:{callback:v=>v+'%'}}}}});
})();

/* ---- PARTNEREK ---- */
(()=>{const t=document.getElementById('tab-partnerek');const p=D.partnerek;
 t.innerHTML=`<div class="grid k4">
   ${kpiCard('B2B forgalom',fmtM(p.osszesen)+' lej')}
   ${kpiCard('Partnerek',p.darab+' db')}
   ${kpiCard('Top 5 koncentráció',pct(p.top5_pct),'top 10: '+pct(p.top10_pct))}
   ${kpiCard('HHI index',fmt(p.hhi),p.hhi>2500?'magas koncentráció':p.hhi>1500?'közepes':'alacsony')}
 </div>
 <div class="card full"><h3>Pareto — vevők és kumulált részesedés</h3><canvas id="pareto"></canvas>
 <div class="note">A piros vonal a kumulált %-ot mutatja: kevés vevő adja a forgalom nagy részét → függőségi kockázat.</div></div>
 <div class="card full"><h3>Partnerlista</h3><div class="tablewrap"><table><thead><tr><th>#</th><th>Partner</th><th>Település</th><th>Érték</th><th>Rész.</th><th>Kumul.</th></tr></thead>
 <tbody>${p.lista.map((x,i)=>`<tr><td>${i+1}</td><td>${x.partner}</td><td class="tag">${x.telepules}</td><td>${fmt(x.ertek)}</td><td>${pct(x.reszesedes_pct)}</td><td>${pct(x.kumulativ_pct)}</td></tr>`).join('')}</tbody></table></div></div>`;
 const top=p.lista.slice(0,15);
 new Chart(document.getElementById('pareto'),{data:{labels:top.map(x=>x.partner.length>22?x.partner.slice(0,20)+'…':x.partner),
   datasets:[{type:'bar',data:top.map(x=>x.ertek),backgroundColor:C[0],borderRadius:4,yAxisID:'y'},
     {type:'line',data:top.map(x=>x.kumulativ_pct),borderColor:C[3],backgroundColor:'transparent',tension:.2,yAxisID:'y1',pointRadius:3}]},
   options:{plugins:{legend:{display:false}},scales:{y:{ticks:{callback:v=>fmt(v)}},y1:{position:'right',min:0,max:100,ticks:{callback:v=>v+'%'},grid:{drawOnChartArea:false}}}}});
})();

/* ---- IDŐ ---- */
(()=>{const t=document.getElementById('tab-ido');
 t.innerHTML=`<div class="card full"><h3>Teljes árbevétel havonta (GERDIT) vs. B2B számlás (P2025)</h3><canvas id="trend"></canvas>
 <div class="note">A teljes árbevételnek nyári csúcsa van, de nincs novemberi összeomlás — a novemberi gödör <b>kifejezetten a B2B csatorna</b> jelensége (turizmus/HoReCa vevők).</div></div>
 <div class="grid k2" style="margin-top:16px">
 <div class="card"><h3>B2B profit% havonta</h3><canvas id="prof"></canvas></div>
 <div class="card"><h3>B2B számlák száma havonta</h3><canvas id="inv"></canvas></div></div>`;
 const gm=D.gerdit_havi,sm=D.szamlas_havi;const labels=gm.map(x=>HU[x.honap]);
 new Chart(document.getElementById('trend'),{data:{labels,datasets:[
   {type:'bar',label:'Teljes árbevétel',data:gm.map(x=>x.arbevetel),backgroundColor:'rgba(79,140,255,.35)',yAxisID:'y'},
   {type:'line',label:'B2B számlás',data:sm.map(x=>x.ertek),borderColor:C[1],tension:.3,yAxisID:'y'}]},
   options:{plugins:{legend:{position:'bottom'}},scales:{y:{ticks:{callback:v=>fmt(v)}}}}});
 new Chart(document.getElementById('prof'),{type:'line',data:{labels:sm.map(x=>HU[x.honap]),
   datasets:[{data:sm.map(x=>x.profit_pct),borderColor:C[2],backgroundColor:'rgba(240,160,32,.15)',fill:true,tension:.3}]},
   options:{plugins:{legend:{display:false}},scales:{y:{ticks:{callback:v=>v+'%'}}}}});
 new Chart(document.getElementById('inv'),{type:'bar',data:{labels:sm.map(x=>HU[x.honap]),
   datasets:[{data:sm.map(x=>x.szamlak),backgroundColor:C[4],borderRadius:4}]},
   options:{plugins:{legend:{display:false}}}});
})();

/* ---- KÉSZLET ---- */
(()=>{const t=document.getElementById('tab-keszlet');const ke=D.keszlet_egeszseg;
 t.innerHTML=`<div class="grid k4">
   ${kpiCard('Vizsgált cikksor',fmt(ke.osszes_cikksor))}
   ${kpiCard('⚠️ Negatív készlet',fmt(ke.negativ_db),'hiba — kivizsgálandó')}
   ${kpiCard('🟡 Holt készlet',fmt(ke.holt_db),'0 éves eladás')}
   ${kpiCard('⚪ Mozdulatlan',fmt(ke.mozdulatlan_db),'törzsadat-gyanú')}
 </div>
 <div class="callout">📄 Részletes tételes lista: <b>Keszlet_problemak_2025.xlsx</b> (negatív + holt készlet, telephely szerint).</div>
 <div class="grid k2" style="margin-top:16px">
 <div class="card"><h3>Top 15 forgási cikk (mennyiség)</h3><canvas id="mov"></canvas><div class="note">A friss alapélelmiszer viszi a volument.</div></div>
 <div class="card"><h3>Szortiment-átfedés</h3><canvas id="ovl"></canvas><div class="note">Hány telephelyen szerepel egy cikk. Sok a lokális (1 boltos) tétel, kevés a közös mag (6 bolt).</div></div></div>`;
 const mov=D.top_mozgok.filter(m=>!/PUNGI|AMBALAT/.test(m.cikk)).slice(0,15);
 new Chart(document.getElementById('mov'),{type:'bar',data:{labels:mov.map(m=>m.cikk.length>26?m.cikk.slice(0,24)+'…':m.cikk),
   datasets:[{data:mov.map(m=>m.mennyiseg),backgroundColor:C[1],borderRadius:4}]},
   options:{indexAxis:'y',plugins:{legend:{display:false}},scales:{x:{ticks:{callback:v=>fmt(v)}}}}});
 const ov=D.szortiment_atfedes;
 new Chart(document.getElementById('ovl'),{type:'bar',data:{labels:Object.keys(ov).map(k=>k+' telephely'),
   datasets:[{data:Object.values(ov),backgroundColor:C[0],borderRadius:4}]},
   options:{plugins:{legend:{display:false}}}});
})();

/* ---- ÁFA ---- */
(()=>{const t=document.getElementById('tab-afa');const a=D.afa_szerkezet;
 t.innerHTML=`<div class="grid k2"><div class="card"><h3>Forgalom áfakulcs szerint (kasszás)</h3><canvas id="vat"></canvas>
   <div class="note">~9% = élelmiszer; ~19–21% = ital, ipari cikk, kozmetikum, cigaretta. A 2025 közepi áfa-emelés (19→21%) miatt a standard sáv átlaga ~20%.</div></div>
   <div class="card"><h3>Csatorna-arány</h3><canvas id="ch"></canvas>
   <div class="note">A kasszás kiskereskedelem adja a forgalom ~88%-át.</div></div></div>`;
 new Chart(document.getElementById('vat'),{type:'doughnut',data:{labels:['~9% kedvezményes (élelmiszer)','~19–21% standard','~vegyes'],
   datasets:[{data:[a.kedvezmenyes_9,a.standard_19_21,a.vegyes],backgroundColor:[C[1],C[3],C[2]],borderWidth:0}]},
   options:{plugins:{legend:{position:'bottom'}}}});
 new Chart(document.getElementById('ch'),{type:'doughnut',data:{labels:['Kasszás','B2B számlás'],
   datasets:[{data:[D.kpi.kassza_arbevetel,D.kpi.b2b_arbevetel],backgroundColor:[C[0],C[5]],borderWidth:0}]},
   options:{plugins:{legend:{position:'bottom'}}}});
})();
</script>
</body>
</html>'''

out = HTML.replace('__CHARTJS__', CHARTJS).replace('__DATA__', DATA)
with open(P('Dashboard_2025.html'),'w',encoding='utf-8') as f: f.write(out)
print('Dashboard mentve:', P('Dashboard_2025.html'), '(', len(out)//1024, 'KB )')
