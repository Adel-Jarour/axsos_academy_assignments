class BankAccount:
    def __init__(self, int_rate, balance = 0):
        self.balance = balance
        self.int_rate = int_rate / 100

    def depoit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance < amount:
            print('Insufficient funds: Charging a $5 fee')
        else:
            self.balance -= amount
        return self
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    
    def yield_interest(self): 
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self
    

acc1 = BankAccount(5).depoit(250).depoit(250).depoit(100).withdraw(400).yield_interest().display_account_info()
acc2 = BankAccount(25).depoit(300).depoit(200).withdraw(50).withdraw(100).withdraw(75).withdraw(125).yield_interest().display_account_info()

