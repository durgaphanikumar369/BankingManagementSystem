# Main.py
from account import create_account
from balance import check_balance 
from transaction import add_amount, withdraw_amount
from details import check_account_details

accounts = []

def find_account(account_number):
    for account in accounts:
        if account.account_number == account_number:
            return account
    return None

while True:
    print("\nBanking System Menu:")
    print("1. Create Account")
    print("2. Check Balance")
    print("3. Add Amount")
    print("4. Withdraw Amount")
    print("5. Check Account Details")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        account_number = input("Enter account number : ")
        name = input("Enter account holder's name: ")
        initial_balance = float(input("Enter initial balance: "))
        account = create_account(account_number, name, initial_balance)
        accounts.append(account)
        print("Account created successfully.")
    
    elif choice == '2':
        account_number = input("Enter account number: ")
        account = find_account(account_number)
        if account:
            print(f"Balance: {check_balance(account)}")
        else:
            print("Account not found.")
    
    elif choice == '3':
        account_number = input("Enter account number: ")
        account = find_account(account_number)
        if account:
            amount = float(input("Enter amount to add: "))
            if add_amount(account, amount):
                print("Amount added successfully.")
            else:
                print("Invalid amount.")
        else:
            print("Account not found.")
    
    elif choice == '4':
        account_number = input("Enter account number: ")
        account = find_account(account_number)
        if account:
            amount = float(input("Enter amount to withdraw: "))
            if withdraw_amount(account, amount):
                print("Amount withdrawn successfully.")
            else:
                print("Invalid amount or insufficient balance.")
        else:
            print("Account not found.")
    
    elif choice == '5':
        account_number = input("Enter account number: ")
        account = find_account(account_number)
        if account:
            details = check_account_details(account)
            for key, value in details.items():
                print(f"{key}: {value}")
        else:
            print("Account not found.")
    
    elif choice == '6':
        print("Thank you visit again...🙏")
        break
    
    else:
        print("Invalid choice. Please try again.")
