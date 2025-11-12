class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    # Add money into the account and return the new balance.
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    # Take money out by subtracting from balance and returning the withdrawn amount.
    def withdraw(self, amount):
        if amount > self.balance:
            print ("Error. You don't have enough mone in your account.")
        else:
            self.balance -= amount
            return amount
    
    # Print the current value of balance.Lastly, initialize a new object from the BankAccount class and use these methods to do the following:   
    def display_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

# Example usage:
my_account = BankAccount("Sofia", "Sousa", 12345, "checking", 6789, 0.00)

# Deposit $96
my_account.deposit(96)

# Withdraw $25
withdrawn_amount = my_account.withdraw(25)

# Display current balance
my_account.display_balance()
      
