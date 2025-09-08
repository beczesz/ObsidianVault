# {{date:YYYY-MM-DD}} ({{date:dddd}})



---

## 📅 Events & Calendar
(Integrate with Calendar plugin or add manually)

---


## 🗂 Projects & Tasks

``` dataview
TASK
FROM "01_Projects"
WHERE !completed AND due <= date(today) and due
GROUP BY file.folder + "/" + file.name
```

## 📝Areas TODO

``` dataview
TASK
FROM "02_Areas"
WHERE !completed AND due <= date(today) and due
GROUP BY file.folder + "/" + file.name
```


### 📝 Other tasks

- [ ] Read the emails

---

## 🤝 Meetings
- Meeting: [[Project X Sync]]  
  - Notes:  
  - Decisions:  
  - Action items:  



---
# Personal
## 🌅 Morning Thoughts
_Free writing / journaling space for reflections, insights, or essay-style entries. Personal and unfiltered._

- 
- 


## 🌙 Reflection
- What went well today?  
- What challenged me?  
- What did I learn?  
- What am I grateful for?  
  
## Habit Tracker
Weight (kg): 96.
