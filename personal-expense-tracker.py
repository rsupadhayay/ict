import csv

# Initialize the list to store expenses
expenses = []

# Function to add an expense
def add_expense():
    date = input("Enter the date of the expense (YYYY-MM-DD): ")
    category = input("Enter the category of the expense: ")
    amount = float(input("Enter the amount spent: "))
    description = input("Enter a brief description of the expense: ")

    expense = {
        'date': date,
        'category': category,
        'amount': amount,
        'description': description
    }

    expenses.append(expense)
    print("✅ Expense added successfully!")

# Function to view expenses
def view_expenses():
    if not expenses:
        print("📭 No expenses recorded.")
        return

    for expense in expenses:
        if all(key in expense for key in ('date', 'category', 'amount', 'description')):
            print(f"📅 {expense['date']} | 🗂 {expense['category']} | 💸 {expense['amount']} | 📝 {expense['description']}")
        else:
            print("⚠️ Incomplete expense entry found and skipped.")

# Function to set and track the budget
def track_budget():
    monthly_budget = float(input("Enter your monthly budget: "))
    total_expenses = sum(float(expense['amount']) for expense in expenses)

    if total_expenses > monthly_budget:
        print("🚨 You have exceeded your budget!")
    else:
        remaining_budget = monthly_budget - total_expenses
        print(f"✅ You have {remaining_budget:.2f} left for the month.")

# Function to save expenses to a CSV file
def save_expenses():
    with open('expenses.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['date', 'category', 'amount', 'description'])
        writer.writeheader()
        writer.writerows(expenses)
    print("💾 Expenses saved to expenses.csv")

# Function to load expenses from a CSV file
def load_expenses():
    try:
        with open('expenses.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['amount'] = float(row['amount'])  # Convert amount back to float
                expenses.append(row)
        print("📂 Expenses loaded from expenses.csv")
    except FileNotFoundError:
        print("📁 No saved expenses found.")

# Function to display the menu
def display_menu():
    print("\n📊 Personal Expense Tracker")
    print("1. ➕ Add expense")
    print("2. 📋 View expenses")
    print("3. 💰 Track budget")
    print("4. 💾 Save expenses")
    print("5. ❌ Exit")

# Main function to run the expense tracker
def main():
    load_expenses()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            track_budget()
        elif choice == '4':
            save_expenses()
        elif choice == '5':
            save_expenses()
            print("👋 Exiting the program. Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
