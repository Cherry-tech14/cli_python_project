print("==CLI Expense Tracker==")

expenses = []

while True:
    print("1. Add expense")
    print("2. View expenses")
    print("3. Show total")
    print("q. Quit\n")

    choice = input("Choose an option:").strip()

    if choice == "q":
        print("Goodbye")
        break

    elif choice == "1":
        description = input("Enter description:").strip()
        if not description:
            print("Description cannot be empty\n")
            continue

            amount_str = input("Enter amount in Naira: ")
            try:
                amount = float(amount_str)
                if amount <= 0:
                    print("Amount must be a positive number")
                    continue
                except ValueError:
                    print("Please enter a valid numeric amount")
                    continue

                    expense = {"description":description, "amount":amount}
                    expenses.append(expense)
                    print("Expense added successfully")

                    elif choice == "2":
                        if not expenses:
                            print("No expenses recorded yet")
                        else:
                            print("\n---Recorded Expenses---")
                            for index, item in enumerate(expenses, start=1):
                                print(f"{index}.{item['description']} {item['amount']:.2f}")
                                print()
                            elif choice == "3":
                                total = 0.0
                                for item in expenses:
                                    total += item['amount']
                                    print(f"Total Spent: {total:.2f}\n")
                                else:
                                    print("Invalid choice. Please choose 1,2,3, or q.\n")

                    if__name__ == "__main__":
                        expense_tracker()


