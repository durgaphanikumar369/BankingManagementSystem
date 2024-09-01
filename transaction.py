# transaction.py
def add_amount(account, amount):
    if amount > 0:
        account.balance += amount
        return True
    return False

def withdraw_amount(account, amount):
    if 0 < amount <= account.balance:
        account.balance -= amountS
        return True
    return False

