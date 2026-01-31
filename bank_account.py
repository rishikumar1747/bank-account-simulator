"""
bank_account.py
---------------
A demo project simulating real bank operations using OOP concepts:
- Class and constructor definition
- Attributes and methods
- Encapsulation
- Inheritance
- Method overriding
- Multiple objects
- Simulation of deposits, withdrawals, transfers
"""

# Base Class
class BankAccount:
    def _init_(self, account_number, owner, balance=0.0):
        # Encapsulation: private attributes with leading underscore
        self._account_number = account_number
        self._owner = owner
        self._balance = balance

    # Getter for balance
    def get_balance(self):
        return self._balance

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount} into {self._owner}'s account.")
        else:
            print("Deposit amount must be positive.")

    # Withdraw method
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount} from {self._owner}'s account.")
        else:
            print("Insufficient funds or invalid amount.")

    # Transfer method
    def transfer(self, target_account, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            target_account._balance += amount
            print(f"Transferred {amount} from {self._owner} to {target_account._owner}.")
        else:
            print("Transfer failed due to insufficient funds or invalid amount.")

    # String representation
    def _str_(self):
        return f"Account({self._account_number}, Owner: {self._owner}, Balance: {self._balance})"


# Derived Class: SavingsAccount
class SavingsAccount(BankAccount):
    def _init_(self, account_number, owner, balance=0.0, interest_rate=0.02):
        super()._init_(account_number, owner, balance)
        self._interest_rate = interest_rate

    # Override withdraw method (Savings accounts may restrict withdrawals)
    def withdraw(self, amount):
        if amount > self._balance:
            print("Cannot withdraw more than balance in Savings Account.")
        else:
            super().withdraw(amount)

    # Add interest
    def add_interest(self):
        interest = self._balance * self._interest_rate
        self._balance += interest
        print(f"Interest of {interest} added to {self._owner}'s savings account.")


# Derived Class: CheckingAccount
class CheckingAccount(BankAccount):
    def _init_(self, account_number, owner, balance=0.0, overdraft_limit=500.0):
        super()._init_(account_number, owner, balance)
        self._overdraft_limit = overdraft_limit

    # Override withdraw method (Checking accounts allow overdraft)
    def withdraw(self, amount):
        if amount <= self._balance + self._overdraft_limit:
            self._balance -= amount
            print(f"Withdrew {amount} from {self._owner}'s checking account (Overdraft allowed).")
        else:
            print("Withdrawal exceeds overdraft limit.")


# Simulation of real bank operations
if __name__ == "_main_":
    # Create multiple objects
    acc1 = SavingsAccount("SA1001", "Alice", 1000.0, interest_rate=0.05)
    acc2 = CheckingAccount("CA2001", "Bob", 500.0, overdraft_limit=300.0)

    # Display initial state
    print(acc1)
    print(acc2)

    # Perform operations
    acc1.deposit(200)
    acc1.withdraw(150)
    acc1.add_interest()

    acc2.deposit(300)
    acc2.withdraw(1000)  # Overdraft usage
    acc2.transfer(acc1, 200)

    # Final state
    print(acc1)
    print(acc2)