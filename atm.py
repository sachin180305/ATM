print("WELCOME TO ATM")

CORRECT_PIN = "1234"
balance = 10000

# Login
pin = input("Enter your 4-digit PIN: ")

if pin == CORRECT_PIN:
    print("\nLogin successful!")

    while True:
        print("\n-- ATM MENU --")
        print("1. Balance Enquiry")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        # Balance Enquiry
        if choice == "1":
            print("Your current balance is: ₹", balance)

        # Deposit
        elif choice == "2":
            amount = int(input("Enter amount to deposit: ₹"))
            if amount > 0:
                balance += amount
                print("₹", amount, "deposited successfully.")
            else:
                print("Invalid amount.")

        # Withdraw
        elif choice == "3":
            amount = int(input("Enter amount to withdraw: ₹"))
            if amount <= balance and amount > 0:
                balance -= amount
                print("Please collect your cash.")
            else:
                print("Insufficient balance or invalid amount.")

        # Exit
        elif choice == "4":
            print("Thank you for using the ATM.")
            print("Have a nice day!")
            break

        else:
            print("Invalid choice. Please try again.")

else:
    print("Invalid PIN. Access denied.")
