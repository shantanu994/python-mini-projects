import datetime
import matplotlib.pyplot as plt

# File name to store expenses
FILENAME = "expenses.txt"

# Function to add a new expense
def add_expense(amount, category):
    today = datetime.date.today()  
    with open(FILENAME, "a+") as file:
        file.write(f"{today},{category},{amount}\n")
    print("\nExpense added successfully!")

# Function to view all expenses
def view_expenses():
    print("\n All Expenses are:")
    with open(FILENAME, "r") as file:
        lines = file.readlines()
        if len(lines) == 0:
            print("No expenses found yet.")
        else:
            for idx, line in enumerate(lines, start=1):
                date, category, amount = line.strip().split(",")
                print(f"\n{idx}. Date: {date} | Category: {category} | Amount: ₹{amount}")
    
        
# Function to calculate total expenses
def total_expenses():
    total = 0
    with open(FILENAME, "r") as file:
        for line in file:
            _, _, amount = line.strip().split(",")
            total += float(amount)
    print(f"\nTotal Expenses: ₹",total)


# Function to delete an expense
def delete_expense():
   
    with open(FILENAME, "r") as file:
        lines = file.readlines()
        
    if len(lines) == 0:
        print("\nNo expenses to delete.")
        return
        
    print("\nDelete an Expense:")
    for idx, line in enumerate(lines, start=1):
        date, category, amount = line.strip().split(",")
        print(f"\n{idx}. Date: {date} | Category: {category} | Amount: ₹{amount}")

    choice = int(input("Enter the number of the expense to delete: "))
        
    if 1 <= choice <= len(lines):
        deleted_line = lines.pop(choice - 1)
        with open(FILENAME, "w") as file:
            file.writelines(lines)
        print("\nDeleted successfully!")
        print(f"\nRemoved: {deleted_line.strip()}")
    else:
        print("\nInvalid number. No expense deleted.")

# Function to show a pie chart of expenses by category   
def show_chart():
    categories = {}
    with open(FILENAME, "r") as file:
        for line in file:
            _, category, amount = line.strip().split(",")
            amount = float(amount)
            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount

    if categories:
        plt.figure(figsize=(6,6))
        plt.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%', startangle=90)
        plt.title("\nExpense Breakdown by Category")
        plt.show()
    else:
        print("\nNo data to show chart.")
    
# Main menu loop
while True:
    print("\nWelcome to Expense Tracker")
    print("Type 1 to Add Expense")
    print("Type 2 to View Expenses")
    print("Type 3 to Total Expenses")
    print("Type 4 to Delete Expense")
    print("Type 5 to show pie chart")
    print("Type 6 to Exit")
    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        try:
            amount = float(input("Enter amount (₹): "))
            category = input("Enter category (Food, Travel, etc.): ")
            add_expense(amount, category)
        except ValueError:
            print("Invalid amount! Please enter a number.")
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expenses()
    elif choice == "4":
        delete_expense()
    elif choice == "5":
        show_chart()
    elif choice == "6":
        print("\nThanks for using Expense Tracker! ")
        break
    else:
        print("\nInvalid choice. Please pick 1, 2, 3, 4, 5 or 6.")
