"""
Creating two classes: Bank and BankAccount.
BankAccount
Attributes:
- owner (string) and balance(float)

Methods:
- deposit(value) -> adds the value to the current balance
- withdraw(value) -> if there is sufficient balance, subtracts; else, returns "Insufficient balance"
- valid_value(value) -> returns True if value > 0

Bank
Attributes:
- name (string) and accounts(list of BankAccount objects)

Methods:
- open_account(account) -> Add BankAccount to the list (instance method)
- total_balance() -> Returns the sum of the balance of all accounts (class method)
- bank_info() ->  Returns the bank name and number of accounts (class method)
"""
class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def open_account(self, account):
        self.accounts.append(account)

    def total_balance(self):
        total = 0
        for account in self.accounts:
            total += account.balance
        return total
    
    def get_bank_info(self):
        return f"{self.name}\nAccounts: {self.accounts}\nTotal balance: {self.total_balance()}"
    
class BankAccount:
    def __init__(self, username):
        self.username = username
        self.balance = 0

    def __repr__(self):
        return f"BankAccount(owner: {self.username}, balance: {self.balance})"

    @staticmethod
    def is_valid_value(value):
        return value > 0
    
    def deposit(self, value):
        if BankAccount.is_valid_value(value):
            self.balance += value

    def withdraw(self, value):
        if self.is_valid_value(value):
            if value < self.balance:
                self.balance -= value
            else:
                return "Insufficient funds!"

    def get_account_info(self):
        return f"Username: {self.username}\nBalance: {self.balance}"
    
bank = Bank("Python Bank")
account1 = BankAccount("John")
account2 = BankAccount("Max")

print("Problem data...")
print("-"*10)
print(f"Before: {bank.get_bank_info()}")
account1.deposit(100)
account2.deposit(1000)
bank.open_account(account1)
bank.open_account(account2)
print(f"After: {bank.get_bank_info()}")
    