def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class insufficientFunds(Exception):
    pass

class BankAccount():
    def __init__(self,starting_balance=0):
        self.balance = starting_balance

    def deposit(self,amount):
        self.balance += amount
    
    def withdraw(self,amount):
        if amount > self.balance:
            raise insufficientFunds("insufficient funds in account")
        self.balance -= amount

    def collect_interest(self):
        self.balance *= 1.1