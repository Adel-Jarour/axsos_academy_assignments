from account import BankAccount

class User:
    def __init__(self, int_rate):
        self.accounts = {}
        self.accounts['default'] = BankAccount(int_rate)

    def get_account(self, acc_name, msg="Account not found"):
        if acc_name not in self.accounts:
            print(msg)
            return None
        else:
            return self.accounts[acc_name] 
    
    def add_account(self, acc_name, int_rate, balance=0):
        if self.get_account(acc_name, msg=''):
            return self
        
        self.accounts[acc_name] = BankAccount(int_rate, balance)
        return self

    def deposit(self, acc_name, amount):
        if not self.get_account(acc_name):
            return self
        
        self.accounts[acc_name].deposit(amount)
        return self

    def make_withdrawal(self, acc_name, amount): 
        if not self.get_account(acc_name):
            return self
        
        self.accounts[acc_name].withdraw(amount)
        return self

    def display_user_balance(self, acc_name):
        if not self.get_account(acc_name):
            return self
        
        self.accounts[acc_name].display_account_info()
        return self

    def transfer_money(self, from_account, other_user, to_account, amount):
        if amount <= 0:
            print("Invalid amount")
            return self
        
        if not self.get_account(from_account, msg='Source account not found.'):
            return self
        
        if not other_user.get_account(to_account, msg='Destination account not found.'):
            return self
        
        if self.accounts[from_account].balance < amount:
            print('Insufficient funds for transfer')
            return self

        self.accounts[from_account].withdraw(amount)
        other_user.accounts[to_account].deposit(amount)
        return self

u1 = User(5)
u2 = User(3)

u2.add_account("wallet", 3, 200).display_user_balance("wallet")
u1.add_account("savings", 5, 1000).make_withdrawal("savings", 200).display_user_balance("savings").transfer_money("savings", u2, "wallet", 300).display_user_balance("savings")
u2.display_user_balance("wallet")