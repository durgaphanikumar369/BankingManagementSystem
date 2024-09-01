# account.py
class Account:
    def __init__(self, account_number, name, initial_balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = initial_balance

    def get_details(self):
        return {
            'Account Number': self.account_number,
            'Name': self.name,
            'Balance': self.balance
        }

# Function to create an account
def create_account(account_number, name, initial_balance=0):
    return Account(account_number, name, initial_balance)
