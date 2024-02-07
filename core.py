import json
from datetime import datetime

# The file to store the expenses
expenses_file = 'expenses.json'

# Function to load existing expenses from the file
def load_expenses():
    try:
        with open(expenses_file, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Function to save expenses to the file
def save_expenses(expenses):
    with open(expenses_file, 'w') as file:
        json.dump(expenses, file, indent=4)

# Function to add a new expense
def add_expense(amount, category, date):
    expenses = load_expenses()
    expenses.append({
        'amount': amount,
        'category': category,
        'date': date
    })
    save_expenses(expenses)

# Function to view all expenses
def view_expenses():
    expenses = load_expenses()
    for expense in expenses:
        print(f"Amount: {expense['amount']}, Category: {expense['category']}, Date: {expense['date']}")

# Main program loop
def main():
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            amount = float(input("Amount: "))
            category = input("Category: ")
            date = input("Date (YYYY-MM-DD): ")
            add_expense(amount, category, date)
            print("Expense added successfully.")
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
