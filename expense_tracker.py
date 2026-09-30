"""Expense Tracker - a simple command-line app to record and summarise spending.

Data is saved to expenses.json so it persists between runs.
"""

import json
from datetime import date
from pathlib import Path

DATA_FILE = Path("expenses.json")
CATEGORIES = ["Food", "Transport", "Bills", "Shopping", "Entertainment", "Other"]


def load_expenses():
    """Load expenses from the JSON file (empty list if none exists)."""
    if DATA_FILE.exists():
        try:
            return json.loads(DATA_FILE.read_text())
        except json.JSONDecodeError:
            print("Warning: data file was corrupted. Starting fresh.")
    return []


def save_expenses(expenses):
    """Write expenses to the JSON file."""
    DATA_FILE.write_text(json.dumps(expenses, indent=2))


def get_amount():
    """Keep asking until the user enters a valid positive number."""
    while True:
        try:
            amount = float(input("Amount: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            return round(amount, 2)
        except ValueError:
            print("Please enter a valid number.")


def choose_category():
    """Let the user pick a category from a numbered list."""
    for i, cat in enumerate(CATEGORIES, start=1):
        print(f"  {i}. {cat}")
    while True:
        choice = input("Choose category number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            return CATEGORIES[int(choice) - 1]
        print("Invalid choice, try again.")


def add_expense(expenses):
    """Add a new expense."""
    description = input("Description: ").strip() or "No description"
    amount = get_amount()
    category = choose_category()
    expenses.append(
        {
            "date": date.today().isoformat(),
            "description": description,
            "amount": amount,
            "category": category,
        }
    )
    save_expenses(expenses)
    print(f"Added: {description} - {amount:.2f} ({category})")


def view_expenses(expenses):
    """Print all expenses in a table."""
    if not expenses:
        print("No expenses recorded yet.")
        return
    print(f"\n{'#':<4}{'Date':<12}{'Category':<15}{'Description':<25}{'Amount':>10}")
    print("-" * 66)
    for i, e in enumerate(expenses, start=1):
        print(
            f"{i:<4}{e['date']:<12}{e['category']:<15}"
            f"{e['description'][:24]:<25}{e['amount']:>10.2f}"
        )
    print("-" * 66)
    print(f"{'Total':<56}{sum(e['amount'] for e in expenses):>10.2f}")


def summary_by_category(expenses):
    """Show total spending per category."""
    if not expenses:
        print("No expenses recorded yet.")
        return
    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    grand_total = sum(totals.values())
    print("\nSpending by category:")
    for cat, total in sorted(totals.items(), key=lambda x: x[1], reverse=True):
        print(f"  {cat:<15}{total:>10.2f}  ({total / grand_total:.0%})")


def delete_expense(expenses):
    """Delete an expense by its number."""
    view_expenses(expenses)
    if not expenses:
        return
    choice = input("Enter the # to delete (or press Enter to cancel): ")
    if choice.isdigit() and 1 <= int(choice) <= len(expenses):
        removed = expenses.pop(int(choice) - 1)
        save_expenses(expenses)
        print(f"Deleted: {removed['description']}")
    else:
        print("Cancelled.")


def main():
    expenses = load_expenses()
    actions = {
        "1": ("Add expense", add_expense),
        "2": ("View expenses", view_expenses),
        "3": ("Summary by category", summary_by_category),
        "4": ("Delete expense", delete_expense),
    }
    while True:
        print("\n=== Expense Tracker ===")
        for key, (label, _) in actions.items():
            print(f"{key}. {label}")
        print("5. Quit")
        choice = input("Select an option: ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        if choice in actions:
            actions[choice][1](expenses)
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
