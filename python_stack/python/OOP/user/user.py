class User:
    def __init__(self, balance = 0):
        self.balance = balance

    def make_withdrawal(self, amount):
        if self.balance < amount:
            print('There is not enough money to make transfer...')
        else:
            self.balance -= amount
    
    def display_user_balance(self):
        print(self.balance)

    def deposit(self, amount):
        self.balance += amount
    
    def transfer_money(self, other_user, amount):
        if amount <= 0:
            print('Invalid amount')
            return
        else:
            self.make_withdrawal(amount)
            other_user.deposit(amount)


adel = User(200)
ahmad = User(150)

adel.make_withdrawal(20)
adel.transfer_money(other_user=ahmad, amount=50)
adel.display_user_balance()
ahmad.display_user_balance()