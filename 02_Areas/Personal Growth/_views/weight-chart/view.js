// === Shared weight + trend chart view =======================================
// Parameters (via dv.view's second argument):
//   defaultRangeDays?: number | null  // initial range in days; null = All time. Default 90.
//   useNoteAsRefDate?: boolean        // if true, treats the current note's date (YYYY-MM-DD)
//                                     // as "today" and only includes data <= that date.
//                                     // Default false (= live "today").
//
// Usage:
//   await dv.view("02_Areas/Personal Growh/_views/weight-chart", { defaultRangeDays: 30, useNoteAsRefDate: true });
// ============================================================================

const inp = (typeof input !== "undefined" && input) ? input : {};
const DEFAULT_RANGE_DAYS = inp.defaultRangeDays === undefined ? 90 : inp.defaultRangeDays;
const useNoteAsRefDate = !!inp.useNoteAsRefDate;

// Reference date
let refDate;
if (useNoteAsRefDate) {
  const noteTitle = dv.current().file.name;
  refDate = /^\d{4}-\d{2}-\d{2}$/.test(noteTitle) ? dv.date(noteTitle) : dv.date("today");
} else {
  refDate = dv.date("today");
}

// 1. Pull weight readings
const allPages = dv.pages('"05_DailyNotes"')
  .where(p => {
    if (p.Weight == null) return false;
    if (!useNoteAsRefDate) return true;
    const d = dv.date(p.file.name);
    return d && d <= refDate;
  })
  .sort(p => p.file.name, "asc");

const allLabels = [];
const allData = [];
for (const p of allPages) {
  const w = typeof p.Weight === "string"
    ? parseFloat(p.Weight.replace(",", "."))
    : p.Weight;
  if (Number.isFinite(w)) {
    allLabels.push(p.file.name);
    allData.push(w);
  }
}

// 2. EMA-14 trend on the full series
const span = 14;
const k = 2 / (span + 1);
const fullTrend = [];
let ema = allData[0] ?? 0;
for (let i = 0; i < allData.length; i++) {
  ema = allData[i] * k + ema * (1 - k);
  fullTrend.push(parseFloat(ema.toFixed(1)));
}

const trendMinAllTime = fullTrend.length ? parseFloat(Math.min(...fullTrend).toFixed(1)) : null;
const trendToday = fullTrend.length ? fullTrend[fullTrend.length - 1] : null;

const trendMinLabel = (() => {
  if (trendMinAllTime == null) return "";
  if (trendToday != null && Math.abs(trendToday - trendMinAllTime) < 0.05) {
    return `Today all-time low: ${trendMinAllTime}`;
  }
  if (trendToday != null) {
    const d = trendToday - trendMinAllTime;
    const sign = d >= 0 ? "+" : "";
    return `Min trend ${trendMinAllTime} (Today ${sign}${d.toFixed(1)})`;
  }
  return `Min trend ${trendMinAllTime}`;
})();

// 3. Slice helper — last N calendar days relative to refDate
function sliceLastDays(n) {
  if (n == null) return { labels: allLabels.slice(), data: allData.slice(), trend: fullTrend.slice() };
  const cutoff = refDate.minus({ days: n });
  const labels = [], data = [], trend = [];
  for (let i = 0; i < allLabels.length; i++) {
    const d = dv.date(allLabels[i]);
    if (d && d >= cutoff) {
      labels.push(allLabels[i]);
      data.push(allData[i]);
      trend.push(fullTrend[i]);
    }
  }
  return { labels, data, trend };
}

// 4. UI scaffolding
const root = dv.container.createDiv();
root.style.cssText = "display:flex;flex-direction:column;gap:8px;width:100%;";
const btnBar = root.createDiv();
btnBar.style.cssText = "display:flex;flex-wrap:wrap;gap:6px;";
const chartWrap = root.createDiv();
chartWrap.style.cssText = "height:340px;position:relative;width:100%;";

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

  const { labels, data, trend } = sliceLastDays(days);
  chartWrap.empty();

  if (data.length === 0) {
    chartWrap.createEl("div", {
      text: "No weight data in this range.",
      attr: { style: "padding:20px;text-align:center;color:var(--text-muted);" }
    });
    return;
  }

  const minVal = Math.min(...data);
  const maxVal = Math.max(...data);
  const minIdx = labels[data.indexOf(minVal)];
  const maxIdx = labels[data.lastIndexOf(maxVal)];

  const pad = 0.5;
  const yMin = Math.floor(Math.min(minVal, ...trend, trendMinAllTime ?? Infinity) - pad);
  const yMax = Math.ceil(Math.max(maxVal, ...trend) + pad);

  const titleText = `Weight + Trend — ${days == null ? "All time" : "Last " + days + " days"} · ${data.length} readings`;

  const chartData = {
    type: "line",
    data: {
      labels,
      datasets: [
        {
          label: "Weight (kg)",
          data,
          borderColor: "rgba(130, 160, 210, 0.6)",
          backgroundColor: "rgba(130, 160, 210, 0.1)",
          tension: 0.3,
          pointRadius: 1,
          pointHitRadius: 18,
          borderWidth: 1.5,
          fill: true,
        },
        {
          label: "Trend (EMA-14)",
          data: trend,
          borderColor: "rgba(239, 68, 68, 1)",
          pointRadius: 0,
          pointHitRadius: 18,
          fill: false,
          borderWidth: 3,
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      interaction: { mode: "index", intersect: false },
      scales: {
        y: { min: yMin, max: yMax, title: { display: true, text: "kg" } },
        x: { ticks: { maxTicksLimit: 8, maxRotation: 45 } }
      },
      plugins: {
        legend: { position: "bottom" },
        title:  { display: true, text: titleText, font: { size: 13 } },
        tooltip: {
          padding: 10,
          titleFont: { size: 13 },
          bodyFont:  { size: 13 },
          callbacks: {
            label: (ctx) => `${ctx.dataset.label}: ${ctx.parsed.y} kg`
          }
        },
        annotation: {
          annotations: {
            minLine: {
              type: "line", xMin: minIdx, xMax: minIdx,
              borderColor: "rgba(34, 197, 94, 0.6)", borderWidth: 2,
              label: {
                display: true, content: minVal + " kg", position: "start",
                backgroundColor: "rgba(34, 197, 94, 0.7)",
              }
            },
            maxLine: {
              type: "line", xMin: maxIdx, xMax: maxIdx,
              borderColor: "rgba(239, 68, 68, 0.6)", borderWidth: 2,
              label: {
                display: true, content: maxVal + " kg", position: "start",
                backgroundColor: "rgba(239, 68, 68, 0.7)",
              }
            },
            trendMinLine: {
              type: "line",
              yMin: trendMinAllTime, yMax: trendMinAllTime,
              borderColor: "rgba(239, 68, 68, 0.35)",
              borderWidth: 2,
              borderDash: [6, 4],
              label: {
                display: true,
                content: trendMinLabel,
                position: "start",
                backgroundColor: "rgba(239, 68, 68, 0.45)",
                color: "#fff",
                font: { size: 11 }
              }
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
  b.style.cssText = "padding:6px 12px;border:1px solid var(--background-modifier-border);border-radius:6px;cursor:pointer;font-size:13px;min-width:48px;";
  b.onclick = () => render(r.days);
}

render(DEFAULT_RANGE_DAYS);
