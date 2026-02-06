def login():
    print("        WELCOME TO ATM            ")

    pin = input("Enter your 4-digit PIN: ")

    if pin == "1234":
        print("Login successful!\n")
        return True
    else:
        print("Invalid PIN. Access Denied.")
        return False
