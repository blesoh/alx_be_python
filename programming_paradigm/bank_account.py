class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self):
        amount = float(input("Deposit: "))
        if amount > 0:
            self.balance += amount
            print("Deposited: $", amount)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self):
        amount = float(input("Withdraw: "))
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Withdrew: $", amount)
        else:
            print("Insufficient funds or invalid amount.")  
            

    def display_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")