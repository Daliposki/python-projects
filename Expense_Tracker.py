class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, amount):
        self.expenses.append((description, amount))

    def total_expenses(self):
        return sum(amount for _, amount in self.expenses)

    def print_expenses(self):
        print("Expense List:")
        for i, (description, amount) in enumerate(self.expenses, start=1):
            print(f"{i}. {description}: ${amount}")


if __name__ == "__main__":
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expenses")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            tracker.add_expense(description, amount)
            print("Expense added successfully!")
        elif choice == '2':
            tracker.print_expenses()
        elif choice == '3':
            total = tracker.total_expenses()
            print(f"Total Expenses: ${total}")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            
