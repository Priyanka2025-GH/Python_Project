# 3. Banking System in Python

account = {}

def create_account():
    name = input("Enter Name: ")
    balance = float(input("Enter Initial Balance: "))

    account["name"] = name
    account["balance"] = balance

    print("Account Created Successfully!")

def check_balance():
    if "name" in account:
        print(account["name"] + "'s Balance =", account["balance"])
    else:
        print("No Account Found!")

def deposit():
    if "name" in account:
        amount = float(input("Enter Amount to Deposit: "))
        account["balance"] += amount
        print("Deposit Successful!")
    else:
        print("No Account Found!")

def withdraw():
    if "name" in account:
        amount = float(input("Enter Amount to Withdraw: "))

        if account["balance"] >= amount:
            account["balance"] -= amount
            print("Withdrawal Successful!")
        else:
            print("Insufficient Balance!")
    else:
        print("No Account Found!")

while True:
    print("\n===== MyBank =====")
    print("1. Create Account")
    print("2. Check Balance")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        create_account()

    elif choice == "2":
        check_balance()

    elif choice == "3":
        deposit()

    elif choice == "4":
        withdraw()

    elif choice == "5":
        print("Thank You For Using MyBank!")
        break

    else:
        print("Invalid Choice! Please Try Again.")