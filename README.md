# Calculator

A full-featured desktop calculator built with Python's stdlib `tkinter` — no pip install required.

## Features

- Basic arithmetic: `+`, `-`, `×`, `÷`
- Percentage (`%`) and sign toggle (`±`)
- Expression history line above main display
- Backspace (`⌫`) to correct last digit
- Full keyboard support
- Zero-division error handling
- Dark theme (Catppuccin Mocha palette)

## Run

```bash
python main.py
```

Requires Python 3.10+ with `tkinter` (bundled with standard Python installs on Windows and macOS; on Linux: `sudo apt install python3-tk`).

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `0–9`, `.` | Input digits |
| `+`, `-`, `*`, `/` | Operators |
| `Enter` | Evaluate |
| `Backspace` | Delete last digit |
| `Esc` | Clear (AC) |
| `%` | Percent |

## Structure

```
calculator/
└── main.py      # single-file app: CalcEngine (logic) + CalculatorApp (UI)
```

`CalcEngine` is pure Python with no tkinter imports — logic is fully separable and testable.
