// === Shared weight matrix view ===========================================
// Renders a 7-day x 5-week weight table with daily readings, weekly averages,
// week-over-week deltas, and 8-week smart predictions for future days.
//
// Reference date: this note's title if it matches YYYY-MM-DD, else today.
// (No parameters — uses current note context automatically.)
//
// Usage:
//   await dv.view("02_Areas/Personal Growh/_views/weight-matrix");
// ============================================================================

// Reference date: use current note title if it's a date, else today
const title = dv.current().file.name;
const isoTitleMatch = /^\d{4}-\d{2}-\d{2}$/.test(title);
const refDate = isoTitleMatch ? dv.date(title) : dv.date("today");

// Helpers
function toNumberOrNull(v) {
  if (v === null || v === undefined) return null;
  if (typeof v === "number" && Number.isFinite(v)) return v;
  if (typeof v === "string") {
    const n = Number(v.replace(",", ".").trim());
    return Number.isFinite(n) ? n : null;
  }
  return null;
}

function getWeightForDate(dateObj) {
  const fname = dateObj.toFormat("yyyy-MM-dd");
  const page = dv.pages('"05_DailyNotes"')
    .where(p => p.file.name === fname)
    .first();
  const v = toNumberOrNull(page?.Weight);
  if (v !== null) return { value: v, imputed: false };
  // Fallback: walk back up to 7 days to find the most recent weight
  for (let back = 1; back <= 7; back++) {
    const prev = dateObj.minus({ days: back });
    const pname = prev.toFormat("yyyy-MM-dd");
    const ppage = dv.pages('"05_DailyNotes"')
      .where(p => p.file.name === pname)
      .first();
    const pv = toNumberOrNull(ppage?.Weight);
    if (pv !== null) return { value: pv, imputed: true };
  }
  return { value: null, imputed: false };
}

function fmt(v) {
  // Per your request: missing data should show as "-"
  return v === null ? "" : v;
}

function fmtDelta(curr, prev) {
  if (curr === null || prev === null) return "";
  const d = curr - prev;
  return `${d >= 0 ? "+" : ""}${d.toFixed(1)}`;
}

// Week boundaries (ISO weeks: Monday start)
const startOfCurrentWeek = refDate.startOf("week"); // Monday of this week
const startW1 = startOfCurrentWeek.minus({ weeks: 1 });
const startW2 = startOfCurrentWeek.minus({ weeks: 2 });
const startW3 = startOfCurrentWeek.minus({ weeks: 3 });
const startW4 = startOfCurrentWeek.minus({ weeks: 4 });

// Today's weekday index (0=Monday, 6=Sunday) based on refDate (note title if valid)
const todayIndex = refDate.weekday - 1;

// If the current note is NOT a daily note (no ISO title), still allow "today's weight"
// by using real current date for fetching today's weight.
const realToday = dv.date("today");
const realTodayIndex = realToday.weekday - 1;

// Decide which date represents "today" for the purpose of optionally including today's weight.
// - If note title is ISO date: treat that as "today" (use that day + index)
// - Else: treat actual today as "today"
const effectiveTodayDate = isoTitleMatch ? refDate : realToday;
const effectiveTodayIndex = isoTitleMatch ? todayIndex : realTodayIndex;

// Linear regression helper
function linReg(points) {
  const n = points.length;
  if (n < 2) return null;
  const sumX = points.reduce((s, p) => s + p.x, 0);
  const sumY = points.reduce((s, p) => s + p.y, 0);
  const sumXY = points.reduce((s, p) => s + p.x * p.y, 0);
  const sumX2 = points.reduce((s, p) => s + p.x * p.x, 0);
  const denom = n * sumX2 - sumX * sumX;
  if (denom === 0) return null;
  const slope = (n * sumXY - sumX * sumY) / denom;
  const intercept = (sumY - slope * sumX) / n;
  return { slope, intercept };
}

// === Smart prediction setup =================================================
// For future days this week, the prediction is:
//   baseline[i]  = linear regression on the same weekday across the last 8 weeks,
//                  projected to this week (x = 8). Captures the LONG-TERM rhythm.
//   bias         = mean( actual − baseline ) over days ALREADY measured this week.
//                  Captures whether THIS week is running below/above the long-term path.
//   confidence   = min(1, measuredDays / 3). Damps the bias when we have only 1–2 days.
//   predicted[i] = baseline[i] + bias × confidence.
// "Good week" with downward momentum → negative bias → predictions pulled down.
// "Bad week" → positive bias → predictions pushed up. Only real (non-imputed) measurements feed the bias.
const PRED_WEEKS_BACK = 8;

function baselineForWeekday(i) {
  const pts = [];
  for (let w = 1; w <= PRED_WEEKS_BACK; w++) {
    const day = startOfCurrentWeek.minus({ weeks: w }).plus({ days: i });
    const fname = day.toFormat("yyyy-MM-dd");
    const page = dv.pages('"05_DailyNotes"')
      .where(p => p.file.name === fname)
      .first();
    const v = toNumberOrNull(page?.Weight);
    if (v !== null) pts.push({ x: PRED_WEEKS_BACK - w, y: v });
  }
  const reg = linReg(pts);
  if (reg) return reg.slope * PRED_WEEKS_BACK + reg.intercept;
  return pts.length > 0 ? pts[pts.length - 1].y : null;
}

const baselines = [];
for (let i = 0; i < 7; i++) baselines[i] = baselineForWeekday(i);

// This-week residuals (real measurements only — skip imputed fallbacks)
const residuals = [];
for (let i = 0; i <= effectiveTodayIndex; i++) {
  const thisWeekDay = startOfCurrentWeek.plus({ days: i });
  const r = (i === effectiveTodayIndex)
    ? getWeightForDate(effectiveTodayDate)
    : getWeightForDate(thisWeekDay);
  if (r.value !== null && !r.imputed && baselines[i] !== null) {
    residuals.push(r.value - baselines[i]);
  }
}

const meanBias = residuals.length > 0
  ? residuals.reduce((a, b) => a + b, 0) / residuals.length
  : 0;
const confidence = Math.min(1, residuals.length / 3);
const effectiveBias = meanBias * confidence;
// === End prediction setup ===================================================

// Pass 1: collect raw data
let rawRows = [];
let allWeights = [];
let weekSums = { w4: [], w3: [], w2: [], w1: [], w: [] };

for (let i = 0; i < 7; i++) {
  const thisWeekDay = startOfCurrentWeek.plus({ days: i });
  const w1Day = startW1.plus({ days: i });
  const w2Day = startW2.plus({ days: i });
  const w3Day = startW3.plus({ days: i });
  const w4Day = startW4.plus({ days: i });

  const dayName = thisWeekDay.toFormat("ccccc");

  const rw4 = getWeightForDate(w4Day);
  const rw3 = getWeightForDate(w3Day);
  const rw2 = getWeightForDate(w2Day);
  const rw1 = getWeightForDate(w1Day);

  let rCurr = { value: null, imputed: false };
  let predicted = null;

  if (i < effectiveTodayIndex) {
    rCurr = getWeightForDate(thisWeekDay);
  } else if (i === effectiveTodayIndex) {
    rCurr = getWeightForDate(effectiveTodayDate);
  } else {
    // Future day: 8-week same-weekday baseline + this-week level-shift bias (setup above).
    if (baselines[i] !== null) {
      predicted = parseFloat((baselines[i] + effectiveBias).toFixed(1));
    }
  }

  // Collect for weekly averages
  if (rw4.value !== null) weekSums.w4.push(rw4.value);
  if (rw3.value !== null) weekSums.w3.push(rw3.value);
  if (rw2.value !== null) weekSums.w2.push(rw2.value);
  if (rw1.value !== null) weekSums.w1.push(rw1.value);
  if (rCurr.value !== null) weekSums.w.push(rCurr.value);

  for (const r of [rw4, rw3, rw2, rw1, rCurr]) {
    if (r.value !== null) allWeights.push(r.value);
  }

  let displayDay = dayName;
  if (i === effectiveTodayIndex) displayDay = `**${dayName}**`;

  rawRows.push({ displayDay, rw4, rw3, rw2, rw1, rCurr, predicted });
}

// Find global max and min (real data only)
const globalMax = allWeights.length > 0 ? Math.max(...allWeights) : null;
const globalMin = allWeights.length > 0 ? Math.min(...allWeights) : null;

function fmtStyled(r) {
  if (r.value === null) return "";
  let txt = `${r.value}`;
  if (r.value === globalMax) {
    txt = `<span style="color:red;font-weight:bold">${r.value}</span>`;
  } else if (r.value === globalMin) {
    txt = `<span style="color:green;font-weight:bold">${r.value}</span>`;
  } else if (r.imputed) {
    txt = `<span style="color:lightgray">${r.value}</span>`;
  }
  return txt;
}

function fmtPred(v) {
  if (v === null) return "";
  return `<span style="color:lightgray">${v}</span>`;
}

// Pass 2: build styled rows
let rows = rawRows.map(r => {
  let wCell;
  if (r.rCurr.value !== null) {
    wCell = fmtStyled(r.rCurr);
  } else if (r.predicted !== null) {
    wCell = fmtPred(r.predicted);
  } else {
    wCell = "";
  }
  return [
    r.displayDay,
    fmtStyled(r.rw4),
    fmtStyled(r.rw3),
    fmtStyled(r.rw2),
    fmtStyled(r.rw1),
    wCell,
  ];
});

// Weekly averages row — only real measurements; predictions are NOT included.
function avg(arr) {
  return arr.length > 0 ? (arr.reduce((a, b) => a + b, 0) / arr.length).toFixed(1) : "";
}
const avgs = {
  w4: avg(weekSums.w4),
  w3: avg(weekSums.w3),
  w2: avg(weekSums.w2),
  w1: avg(weekSums.w1),
  w:  avg(weekSums.w)
};

// Bold + accent color so the average row stands out from daily rows
function fmtAvg(v) {
  if (v === "" || v == null) return "";
  return `<span style="font-weight:bold;color:var(--text-accent)">${v}</span>`;
}

rows.push([
  "**\u00d8**",
  fmtAvg(avgs.w4),
  fmtAvg(avgs.w3),
  fmtAvg(avgs.w2),
  fmtAvg(avgs.w1),
  fmtAvg(avgs.w),
]);

// Week-over-week change row: arrow up/down + color.
// Green ↓ = weight loss (good), Red ↑ = weight gain. Within ±0.05 kg shown as → 0.0.
function wowDelta(curr, prev) {
  if (curr === "" || prev === "") return "";
  const d = parseFloat(curr) - parseFloat(prev);
  if (Math.abs(d) < 0.05) {
    return `<span style="color:var(--text-muted)">→ 0.0</span>`;
  }
  const arrow = d > 0 ? "↑" : "↓";
  const color = d > 0 ? "red" : "green";
  const sign  = d > 0 ? "+" : "";
  return `<span style="color:${color};font-weight:bold">${arrow} ${sign}${d.toFixed(1)}</span>`;
}

rows.push([
  "**\u0394**",
  "",
  wowDelta(avgs.w3, avgs.w4),
  wowDelta(avgs.w2, avgs.w3),
  wowDelta(avgs.w1, avgs.w2),
  wowDelta(avgs.w, avgs.w1)
]);

dv.table(
  ["D", "W-4", "W-3", "W-2", "W-1", "W"],
  rows
);

