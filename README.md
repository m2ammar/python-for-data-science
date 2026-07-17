# Python for Data Science

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Learning-yellow)

Self-taught coursework and practice as I learn Python fundamentals and OOP, on my 
way toward Python/ML for data science — part of a broader path that started with 
Data Analyst fundamentals (SQL, Excel, Tableau). This is ongoing coursework, not 
polished end-to-end projects — code here reflects active learning, not finished 
production work.

## Structure

| Folder | Contents | Status |
|---|---|---|
| `Basic/` | Lectures 1-7 — variables, control flow, functions, file I/O, with practice files per lecture | ✅ Complete |
| `Practice_Questions/` | 11 standalone practice problems | 🟡 Ongoing |
| `Python-OOP/` | Lectures 8-9 on OOP, plus applied projects: Bank, Box_Area, School_System, Student_Grade, Vehicle_System | ✅ Complete |
| `notes/` | Reference notes — Python fundamentals, OOP concepts, zip/slicing | ✅ Complete |

## What I learned

Coming into Python with a Java background, most of the friction wasn't logic — it 
was syntax habits I had to unlearn:

```python
# Java instinct
if (x > 5) {
    doSomething();
}

# Python
if x > 5:
    do_something()
```

- **No parentheses around conditions.** Java's `if (x > 5)` muscle memory kept 
  showing up; Python just wants `if x > 5:`.
- **Indentation is the block structure**, not `{}`. Spacing isn't a style choice — 
  get it wrong and the code doesn't run.
- **No semicolons.** Small thing, but it took a while to stop typing them out of habit.

Beyond syntax, working through File I/O and then OOP — where classes translate 
differently than Java's — was where things actually started clicking: seeing the 
same OOP concepts (encapsulation, classes/objects) expressed with Python's 
simpler syntax.
