def balance_enquiry(balance):
    print("Your current balance is ₹", balance)

def deposit(balance):
    amount = int(input("Enter amount to deposit: ₹"))
    if amount > 0:
        balance += amount
        print("Amount deposited successfully.")
    else:
        print("Invalid amount.")
    return balance

def withdraw(balance):
    amount = int(input("Enter amount to withdraw: ₹"))
    if amount > 0 and amount <= balance:
        balance -= amount
        print("Please collect your cash.")
    else:
        print("Insufficient balance or invalid amount.")
    return balance