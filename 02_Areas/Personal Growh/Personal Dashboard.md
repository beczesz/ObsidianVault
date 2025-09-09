```dataviewjs
// === CONFIG ===
const FOLDER    = "05_DailyNotes";     // daily notes folder
const FIELD_KEY = ["weight","Weight"]; // frontmatter or inline field names to read
const DAYS      = 30;                   // rolling window size
const FILL_MODE = "gap";                // "gap" | "carry" | "zero"
const W=640, H=220, PAD=30;             // chart size

// === COLLECT RAW DATA ===
const end   = dv.luxon.DateTime.now().startOf("day");
const start = end.minus({ days: DAYS - 1 }); // inclusive window
const notes = dv.pages(`"${FOLDER}"`)
  .where(p => p.file.day && p.file.day >= start && p.file.day <= end)
  .array();

const byDate = new Map(); // yyyy-MM-dd -> value
for (const p of notes) {
  const v = FIELD_KEY.map(k => p[k]).find(x => x != null);
  const n = Number(v);
  if (isFinite(n)) {
    const key = p.file.day.toFormat("yyyy-MM-dd");
    byDate.set(key, n);
  }
}

// === BUILD DAILY SERIES (fill missing days per FILL_MODE) ===
let lastSeen = null;
const days = [];
for (let d = 0; d < DAYS; d++) {
  const day = start.plus({ days: d });
  const key = day.toFormat("yyyy-MM-dd");
  let val = byDate.has(key) ? byDate.get(key) : null;

  if (val == null) {
    if (FILL_MODE === "carry") val = lastSeen;
    else if (FILL_MODE === "zero") val = 0;
    // else "gap" -> keep null
  }
  if (byDate.has(key)) lastSeen = byDate.get(key);

  days.push({ day, value: val });
}

// Determine y-domain from **available values** (fallback if none)
const values = days.map(d => d.value).filter(v => v != null);
let minY = values.length ? Math.min(...values) : 0;
let maxY = values.length ? Math.max(...values) : 1;
if (minY === maxY) { minY -= 0.5; maxY += 0.5; } // avoid flat scale

// Scales
const minX = +days[0].day, maxX = +days[days.length-1].day;
const spanX = (maxX - minX) || 1;
const spanY = (maxY - minY) || 1;
const sx = ms => PAD + ((ms - minX) * (W - 2*PAD) / spanX);
const sy = v  => H - PAD - ((v - minY) * (H - 2*PAD) / spanY);

// Build polylines: break at gaps when FILL_MODE === "gap"
const segments = [];
let seg = [];
for (const r of days) {
  if (r.value == null && FILL_MODE === "gap") {
    if (seg.length > 0) { segments.push(seg); seg = []; }
  } else {
    if (r.value == null) continue; // gap & not drawing nulls
    seg.push([sx(+r.day), sy(r.value)]);
  }
}
if (seg.length) segments.push(seg);

// Points (show only for actual values we plot)
const dots = [];
for (const r of days) {
  if (r.value == null && FILL_MODE === "gap") continue;
  if (r.value == null) continue;
  dots.push(`<circle cx="${sx(+r.day)}" cy="${sy(r.value)}" r="2" fill="currentColor"/>`);
}

// Y ticks
const midY = (minY + maxY)/2;
const fmt = n => (Math.round(n*10)/10).toString();

// Stats (based on available values)
const avg = values.length ? (values.reduce((a,b)=>a+b,0)/values.length).toFixed(1) : "—";

// Render
let svgLines = segments.map(s => {
  const pts = s.map(([x,y]) => `${x},${y}`).join(" ");
  return `<polyline fill="none" stroke="currentColor" stroke-width="2" points="${pts}"/>`;
}).join("");

const svg = `
<div style="margin:4px 0 8px 0;font-weight:600;">Weight (last ${DAYS} days)</div>
<svg viewBox="0 0 ${W} ${H}" width="100%" height="auto" role="img" aria-label="Weight chart">
  <!-- axes -->
  <line x1="${PAD}" y1="${H-PAD}" x2="${W-PAD}" y2="${H-PAD}" stroke="currentColor" stroke-width="1"/>
  <line x1="${PAD}" y1="${PAD}"   x2="${PAD}"   y2="${H-PAD}" stroke="currentColor" stroke-width="1"/>
  <!-- y ticks -->
  <text x="${PAD-6}" y="${sy(minY)}" fill="currentColor" font-size="11" text-anchor="end">${fmt(minY)}</text>
  <text x="${PAD-6}" y="${sy(midY)}" fill="currentColor" font-size="11" text-anchor="end">${fmt(midY)}</text>
  <text x="${PAD-6}" y="${sy(maxY)}" fill="currentColor" font-size="11" text-anchor="end">${fmt(maxY)}</text>
  ${svgLines}
  ${dots.join("")}
</svg>
<div style="font-size:12px;color:var(--text-muted);margin-top:6px;">
  Avg ${avg} • Range ${fmt(minY)}–${fmt(maxY)}
  • Mode: ${FILL_MODE}
</div>
`;
dv.el("div", svg);

```

```habittracker
{
	"path": "Habits/"
}
```

## Ideas

- Personal trends like weight, habbits
- Active Areas progress
	- Ignis Academy
	- CPS
	- PErsonal
	- ETc...


