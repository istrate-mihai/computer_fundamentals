# Fundamental Algorithms & Computer Science Foundations

A personal deep-dive into computer science fundamentals — built by reading technical books cover to cover and running every significant code example, implementation, and algorithm by hand.

The goal is not to follow tutorials. The goal is to understand what production software, machine learning pipelines, and AI systems are actually doing under the hood.

---

## Philosophy

Most developers use libraries without understanding what runs beneath them. This repository is the opposite approach: read the book, understand the theory, implement the code, observe the output. Every file here is the result of working through a chapter with intention — not copy-pasting, not vibe coding.

This is a long-term project. Books will be added as they are completed.

---

## Books Covered

### 1. Python Data Structures and Algorithms — Benjamin Baka (Packt, 2017)
> Covers fundamental data structures and algorithms in Python: numerical algorithms, data types, linked lists, stacks, queues, trees, hash tables, searching, sorting, selection, and ML applications via scikit-learn.

**Folder:** `Python_Data_Structures_and_Algorithms_by_Benjamin_Baka/`

| File | Topic |
|------|-------|
| `01_numerical_algorithms.py` | Numerical algorithms and Python objects |
| `03_data_types.py` | Python data types and structures |
| `04_lists_and_pointer_structures.py` | Linked lists and pointer structures |
| `05_stacks_and_queues.py` | Stacks and queues |
| `06_trees.py` | Binary trees, BSTs, traversals |
| `07_hashing_and_symbol_tables.py` | Hash tables and symbol tables |
| `08_searching_algorithms.py` | Linear search, binary search, interpolation search |
| `09_sorting_algorithms.py` | Bubble, insertion, selection, merge, quick sort |
| `10_selection_algorithms.py` | Selection algorithms, median finding |
| `13_supervised_learning_implementations_applications_and_tools.py` | Supervised ML: classification, Naive Bayes, scikit-learn |
| `13_unsupervised_learning_implementations_applications_and_tools.py` | Unsupervised ML: clustering, preprocessing, k-means |

> **Note:** Chapters 02, 11, and 12 are not represented as standalone files — their content was either covered inline or skipped as review material.

---

### 2. Python Crash Course — Eric Matthes (No Starch Press, 3rd Edition)
> A fast-paced, hands-on introduction to Python. Part 1 covers language fundamentals; Part 2 applies them in three real projects: a game, data visualizations, and a web application.

**Folder:** `Python_Crash_Course_by_Eric_Matthes/`

#### Part 1 — Language Fundamentals

| Chapter Name | Topic |
|------|---------|-------|
| `Chapter_1_Getting_Started` | printing and basic setup |
| `Chapter_2_Variables_and_Basic_Datatypes` | Variables, strings, numbers |
| `Chapter_3_Introducing_Lists` | Lists, indexing, modifying |
| `Chapter_4_Working_with_Lists` | Loops, slicing, tuples |
| `Chapter_5_if_statements` | Conditionals, boolean logic |
| `Chapter_6_Dictionaries` | Dictionaries, nesting |
| `Chapter_7_User_Input_And_While_Loops` | Input, while loops, flags |
| `Chapter_8_Functions` | Functions, args, kwargs, modules |
| `Chapter_9_Classes` | OOP, inheritance, encapsulation |
| `Chapter_10_Files_and_Exceptions` | File I/O, exceptions, JSON |
| `Chapter_11_Test_Your_Code` | unittest, pytest, test cases |

#### Part 2 — Projects

Part 2 projects live in the dedicated **[python_projects](https://github.com/istrate-mihai/python_projects)** repository.

| Project | Folder (in python-projects) | Description |
|---------|----------------------------|-------------|
| Alien Invasion | `alien_invasion/` | 2D arcade shooter built with pygame |
| Data Visualization | `data_visualization/` | Charts and graphs with Matplotlib & Plotly |
| Web Application | `learning_log/` | Django CRUD web app with user authentication |

> The `python_projects` repo is a standalone collection of vanilla Python applications. Part 2 projects from this book are its foundation, with additional independent projects added over time.

---

## What This Is Not

- Not a tutorial project
- Not a bootcamp exercise set
- Not vibe-coded with AI

---

## What This Is

- A living reference of implemented algorithms and data structures
- A foundation for understanding ML, AI, and systems software at a deeper level
- A multi-book curriculum that grows over time as new books are added

---

## Stack

- Python 3.x
- NumPy, Pandas, scikit-learn, Matplotlib, Plotly, TextBlob, pygame, Django (where applicable)
- No frameworks — raw implementations where possible

---

## How to Run

```bash
# Clone the repo
git clone https://github.com/istrate-mihai/computer_fundamentals
cd computer_fundamentals

# Benjamin Baka examples
cd Python_Data_Structures_and_Algorithms_by_Benjamin_Baka
pip install numpy pandas scikit-learn matplotlib textblob
python 09_sorting_algorithms.py

# Eric Matthes Part 1 examples
cd ../Python_Crash_Course_by_Eric_Matthes
python 09_classes.py

# Eric Matthes Part 2 projects (separate repo)
# See: https://github.com/istrate-mihai/python_projects
```

---

## Roadmap

Books to be added as completed:

- [x] *Python Data Structures and Algorithms* — Benjamin Baka
- [x] *Python Crash Course* — Eric Matthes *(in progress)*
- [ ] *Grokking Algorithms* — Aditya Bhargava
- [ ] *Introduction to Algorithms (CLRS)* — Cormen, Leiserson, Rivest, Stein
- [ ] *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow* — Aurélien Géron
- [ ] *Deep Learning* — Goodfellow, Bengio, Courville
- [ ] *(more to be added)*

---

## Author

**Mihai** — Full-stack developer transitioning into DevOps and systems engineering.  
Building from first principles. Brașov, Romania.
