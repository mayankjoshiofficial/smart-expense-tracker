import os

from datetime import date

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "expenses.txt")



def initialize_file():
    open(FILE_NAME, "a").close()


def show_menu():
    print("\n==============================")
    print("     SMART EXPENSE TRACKER")
    print("==============================")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spent")
    print("4. Exit")


def add_expense():
    name = input("Enter item name: ")
    category=input("Enter the category (FOOD/TRAVEL/etc.): ")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("❌ Invalid amount! Please enter numbers only.")
        return

    today = date.today()

    with open(FILE_NAME, "a") as file:
        file.write(f"{today},{name},{category},{amount}\n")

    print("✅ Expense saved successfully!")


def view_expenses():
    print("\n📋 Your Expenses:")
    print("------------------------------")

    try:
        with open(FILE_NAME, "r") as file:
            empty = True

            for line in file:
                empty = False
                parts = line.strip().split(",")

                if len(parts) >= 3:
                    date_val = parts[0]
                    name = parts[1]
                    category = parts[2]
                    amount = parts[-1]   

                    print(f"{date_val} | {name} | {category} → ₹{amount}")

            if empty:
                print("No expenses found.")

    except FileNotFoundError:
        print("No expense file found.")




def total_spent():
    total = 0

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                amount = parts[-1]
                total += float(amount)

        print(f"\n💰 Total Spent = ₹{total}")
    except FileNotFoundError:
        print("No expense file found.")


def main():
    initialize_file()

    while True:
        show_menu()

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        if choice == 1:
            add_expense()
        elif choice == 2:
            view_expenses()
        elif choice == 3:
            total_spent()
        elif choice == 4:
            print("👋 Goodbye! Keep tracking your expenses.")
            break
        else:
            print("❌ Invalid choice. Please select 1–4.")


main()
