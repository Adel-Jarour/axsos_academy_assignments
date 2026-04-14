class User:
    def __init__(self, balance = 0):
        self.balance = balance

    def make_withdrawal(self, amount):
        if self.balance < amount:
            print('There is not enough money to make transfer...')
        else:
            self.balance -= amount
        return self
    
    def display_user_balance(self):
        print(self.balance)
        return self

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def transfer_money(self, other_user, amount):
        if amount <= 0:
            print('Invalid amount')
            return
        else:
            self.make_withdrawal(amount)
            other_user.deposit(amount)
        return self


amjad = User().deposit(100)
ali = User().deposit(200).display_user_balance().make_withdrawal(30).display_user_balance().transfer_money(amjad, 100).display_user_balance()
amjad.display_user_balance()