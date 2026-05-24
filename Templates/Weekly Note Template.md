# Week <% tp.date.now("YYYY-[W]WW") %>

```dataviewjs
// Weekly open tasks inbox: pull unchecked tasks from each daily note in this ISO week.

const weeklyTitle = dv.current().file.name;                 // e.g. 2026-W08
const weekMatch = weeklyTitle.match(/^(\d{4})-W(\d{2})$/);  // ISO week format

if (!weekMatch) {
  dv.paragraph("Weekly note title must be like YYYY-Www (e.g. 2026-W08).");
} else {
  const isoYear = Number(weekMatch[1]);
  const isoWeek = Number(weekMatch[2]);

  // Build Monday of ISO week
  // Luxon style: start with a date-like object and set week fields.
  const monday = dv.date("today").set({ weekYear: isoYear, weekNumber: isoWeek, weekday: 1 });

  function dailyPage(dateObj) {
    const fname = dateObj.toFormat("yyyy-MM-dd");
    return dv.pages('"05_DailyNotes"').where(p => p.file.name === fname).first();
  }

  for (let i = 0; i < 7; i++) {
    const day = monday.plus({ days: i });
    const fname = day.toFormat("yyyy-MM-dd");
    const page = dailyPage(day);

    const header = `### ${day.toFormat("cccc")} (${fname})`;

    if (!page) {
      dv.header(3, `${day.toFormat("cccc")} (${fname})`);
      dv.paragraph("- (no daily note)");
      continue;
    }

    // Dataview task objects include: text, checked, line, path, etc.
    const openTasks = (page.file.tasks ?? []).where(t => !t.checked);

    dv.header(3, `${day.toFormat("cccc")} (${fname})`);
    dv.paragraph(dv.fileLink(page.file.path, false, fname));

    if (openTasks.length === 0) {
      dv.paragraph("- (no open tasks)");
    } else {
      // Show tasks. These are "live" tasks (checking them affects the original file in Obsidian UI).
      dv.taskList(openTasks, false);
    }
  }
}

```
