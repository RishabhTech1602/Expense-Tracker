# Expense Tracker

A simple command-line expense tracker written in Python. Expenses are saved to a local JSON file so your data persists between sessions.

## Features
- Add expenses with a description, amount, and category
- View all expenses in a formatted table with a running total
- See spending totals and percentages by category
- Delete expenses
- Input validation and automatic saving

## Concepts Used
Functions, loops, dictionaries and lists, file handling (JSON), exception handling, string formatting, and the `datetime` and `pathlib` modules.

## Requirements
Python 3.7+ (no external libraries needed).

## How to Run
```bash
python expense_tracker.py
```

## Example
```
=== Expense Tracker ===
1. Add expense
2. View expenses
3. Summary by category
4. Delete expense
5. Quit
```

## Possible Improvements
- Filter expenses by date range or month
- Export to CSV
- Set monthly budgets with warnings
- Add a GUI with Tkinter
