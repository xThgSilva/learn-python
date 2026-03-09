"""
Bank Account - Exercise

Implement the following class attribute: `bank_name = "Python Bank"`

The constructor receives:
- Owner (string)
- Balance (float)

Methods:
- deposit(value) -> adds the value to the current balance
- withdraw(value) -> if there is sufficient balance, subtracts; else, returns "Insufficient balance"
- get_bank_name() -> returns the bank name
- valid_value(value) -> returns True if value > 0
"""
class BankAccount:
    bank_name = "Python Bank"

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0
    
    def deposit(self, amount):
        if not self.is_valid_amount(amount):
            return "Invalid amount"
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if not self.is_valid_amount(amount):
            return "Invalid amount"
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance

    @classmethod
    def get_bank_name(cls):
        return cls.bank_name
    
    def show_info(self):
        return f"Owner: {self.owner}\nBalance: {self.balance}"
    
account1 = BankAccount("People1", 1000)
account2 = BankAccount("People2", 1100)

print("Actions with Account1")
account1.deposit(100)
account1.withdraw(50)
print(account1.show_info())
print("-"*20)
print("Actions with Account2")
account2.deposit(200)
account2.withdraw(100)
print(account2.show_info())
    