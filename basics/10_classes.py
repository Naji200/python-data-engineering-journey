class car:
    def __init__(self, make, model, year):
        self.brand = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"{self.make} {self.model} engine started.")

class bank_account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")