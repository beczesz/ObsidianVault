// === Shared rolling-delta chart view =========================================
// Bar chart of EMA-14 delta vs N days ago. Green bar = trend going down (good),
// Red bar = trend going up.
//
// Parameters (via dv.view's second argument):
//   defaultRangeDays?: number | null  // initial chart range; null = All time. Default 90.
//   windowDays?: number               // delta window — compare today's EMA to N days ago. Default 30.
//
// Usage:
//   await dv.view("02_Areas/Personal Growh/_views/weight-delta", { defaultRangeDays: 90 });
// ============================================================================

const inp = (typeof input !== "undefined" && input) ? input : {};
const DEFAULT_RANGE_DAYS = inp.defaultRangeDays === undefined ? 90 : inp.defaultRangeDays;
const WINDOW_DAYS = inp.windowDays === undefined ? 30 : inp.windowDays;

// STRICT date regex — only accept YYYY-MM-DD filenames.
// Drive sync produces conflict-copy files like "2025-12-19 (1).md" — those break
// native `new Date()` parsing on iOS WebKit (works on Mac Chromium, hence the asymmetry).
const ISO_DATE_RE = /^\d{4}-\d{2}-\d{2}$/;

const pages = dv.pages('"05_DailyNotes"')
  .where(p => p.Weight != null && ISO_DATE_RE.test(p.file.name))
  .sort(p => p.file.name, "asc");

const weightMap = {};
const allDates = [];
for (const p of pages) {
  const w = typeof p.Weight === "string"
    ? parseFloat(p.Weight.replace(",", "."))
    : p.Weight;
  if (Number.isFinite(w)) {
    weightMap[p.file.name] = w;
    allDates.push(p.file.name);
  }
}

// EMA-14 trend
const span = 14;
const kk = 2 / (span + 1);
const emaMap = {};
let ema = weightMap[allDates[0]] ?? 0;
for (const date of allDates) {
  ema = weightMap[date] * kk + ema * (1 - kk);
  emaMap[date] = parseFloat(ema.toFixed(2));
}

// Delta vs WINDOW_DAYS ago (fuzzy match ±3 days). Guarded against Invalid Date.
const allLabels = [];
const allDeltas = [];
for (const date of allDates) {
  const d = new Date(date);
  if (isNaN(d.getTime())) continue;   // defensive: skip if somehow still invalid
  d.setDate(d.getDate() - WINDOW_DAYS);

  let prevEma = null;
  for (let offset = 0; offset <= 3; offset++) {
    const try1 = new Date(d);
    try1.setDate(try1.getDate() + offset);
    if (!isNaN(try1.getTime())) {
      const k1 = try1.toISOString().slice(0, 10);
      if (emaMap[k1] != null) { prevEma = emaMap[k1]; break; }
    }
    if (offset > 0) {
      const try2 = new Date(d);
      try2.setDate(try2.getDate() - offset);
      if (!isNaN(try2.getTime())) {
        const k2 = try2.toISOString().slice(0, 10);
        if (emaMap[k2] != null) { prevEma = emaMap[k2]; break; }
      }
    }
  }

  if (prevEma !== null) {
    const delta = parseFloat((emaMap[date] - prevEma).toFixed(1));
    allLabels.push(date);
    allDeltas.push(delta);
  }
}

// Slice helper
function sliceLastDays(n) {
  if (n == null) return { labels: allLabels.slice(), deltas: allDeltas.slice() };
  const today = new Date(); today.setHours(0,0,0,0);
  const cutoff = new Date(today); cutoff.setDate(today.getDate() - n);
  const labels = [], deltas = [];
  for (let i = 0; i < allLabels.length; i++) {
    const d = new Date(allLabels[i]);
    if (!isNaN(d.getTime()) && d >= cutoff) {
      labels.push(allLabels[i]);
      deltas.push(allDeltas[i]);
    }
  }
  return { labels, deltas };
}

// UI scaffolding
const root = dv.container.createDiv();
root.style.cssText = "display:flex;flex-direction:column;gap:8px;width:100%;";
const btnBar = root.createDiv();
btnBar.style.cssText = "display:flex;flex-wrap:wrap;gap:6px;";
const chartWrap = root.createDiv();
chartWrap.style.cssText = "height:300px;position:relative;width:100%;";

const ranges = [
  { label: "30d", days: 30 },
  { label: "90d", days: 90 },
  { label: "6m",  days: 180 },
  { label: "1y",  days: 365 },
  { label: "All", days: null },
];

function render(days) {
  for (const b of btnBar.querySelectorAll("button")) {
    const d = b.dataset.days === "" ? null : parseInt(b.dataset.days);
    const active = d === days;
    b.style.background = active ? "var(--interactive-accent)" : "var(--background-secondary)";
    b.style.color      = active ? "var(--text-on-accent)"      : "var(--text-normal)";
  }

  const { labels, deltas } = sliceLastDays(days);
  chartWrap.empty();

  if (deltas.length === 0) {
    chartWrap.createEl("div", {
      text: "No delta data in this range.",
      attr: { style: "padding:20px;text-align:center;color:var(--text-muted);" }
    });
    return;
  }

  const colors = deltas.map(d => d <= 0 ? "rgba(34, 197, 94, 0.7)" : "rgba(239, 68, 68, 0.7)");
  const yMin = Math.floor(Math.min(...deltas) - 0.5);
  const yMax = Math.ceil(Math.max(...deltas) + 0.5);
  const titleText = `Monthly Trend (${WINDOW_DAYS}d EMA-14 delta) — ${days == null ? "All time" : "Last " + days + "d"}`;

  const chartData = {
    type: "bar",
    data: {
      labels,
      datasets: [{
        label: `${WINDOW_DAYS}d EMA delta (kg)`,
        data: deltas,
        backgroundColor: colors,
        borderColor: colors,
        borderWidth: 1,
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        y: {
          min: yMin, max: yMax,
          title: { display: true, text: "kg" },
          grid: { color: "rgba(100,100,100,0.1)" }
        },
        x: { ticks: { maxTicksLimit: 10, maxRotation: 45 } }
      },
      plugins: {
        legend: { position: "bottom" },
        title:  { display: true, text: titleText, font: { size: 13 } },
        tooltip: {
          callbacks: {
            label: (ctx) => {
              const v = ctx.parsed.y;
              const sign = v >= 0 ? "+" : "";
              return `${sign}${v} kg vs EMA ${WINDOW_DAYS} days ago`;
            }
          }
        },
        annotation: {
          annotations: {
            zeroLine: {
              type: "line",
              yMin: 0, yMax: 0,
              borderColor: "rgba(100,100,100,0.8)",
              borderWidth: 2,
            }
          }
        }
      }
    }
  };

  window.renderChart(chartData, chartWrap);
}

for (const r of ranges) {
  const b = btnBar.createEl("button", { text: r.label });
  b.dataset.days = r.days == null ? "" : String(r.days);
  b.style.cssText = "border:none;padding:4px 12px;border-radius:6px;cursor:pointer;font-size:13px;";
  b.onclick = () => render(r.days);
}

render(DEFAULT_RANGE_DAYS);
