expenses = []

file = open("expenses.txt", "a+")  
file.close()



while(True):
    print("SMART EXPENSE TRACKER")
    print("-----------------------")

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spent")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    print("You chose:", choice)

    if choice == 1:
        name = input("Enter item name: ")
        amount = float(input("Enter amount: "))

        file = open("expenses.txt", "a")
        file.write(f"{name},{amount}\n")
        file.close()

        print("Expense saved !!!")



    elif choice == 2:
        file = open("expenses.txt", "r")
        print("\nYour Expenses:")
        for line in file:
            name, amount = line.strip().split(",")
            print(name, "→ ₹", amount)
        file.close()


    elif choice == 3:
        total = 0
        file = open("expenses.txt", "r")
        for line in file:
            name, amount = line.strip().split(",")
            total += float(amount)
        file.close()
 
        print("Total Spent = ₹", total)

    elif (choice==4):
        print("Bye")
        break
    else:
        print("Invalid Choice")