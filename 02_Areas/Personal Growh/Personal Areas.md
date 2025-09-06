- [ ] Obsidian plugins #focus 
- [ ] PKM Learning #focus 
- [ ] List the ideas [link](https://chatgpt.com/g/g-p-68b7e126a2548191865449f2d76db264-pkm/c/68b7e177-7d10-8329-9d07-e4225653ad0a)

## To Read0
- [ ] https://tomtunguz.com/groves-stagger-chart
- [ ] High Output management https://www.google.ro/books/edition/High_Output_Management/piCeCgAAQBAJ?hl=en&gbpv=1&printsec=frontcover



## To Read
- [ ] Automate the list of the read books and scanned books as well. 

## Ideas


```dataviewjs

const TAG = "#idea";
const results = [];

for (const page of dv.pages().values) {
  const text = await dv.io.load(page.file.path);
  const lines = text.split(/\r?\n/);

  for (const line of lines) {
    if (/(^|\s)#idea(\b|\/)/.test(line)) {
      results.push({ line: line.trim(), file: page.file });
    }
  }
}

for (const r of results) {
  // Create container
  const block = dv.el("div", "", { cls: "idea-block" });

  // The idea line itself
  block.createEl("p", { text: r.line });

  // Right-aligned source note link
  const source = block.createEl("div", { cls: "idea-source" });
  source.appendChild(dv.fileLink(r.file.path).el);

  // Separator
  dv.el("hr");
}

// Optional CSS for nicer formatting (put in your snippets.css or Style Settings plugin):
/*
.idea-block {
  margin-bottom: 0.5em;
}
.idea-source {
  text-align: right;
  font-size: 0.8em;
  color: gray;
}
*/


```
