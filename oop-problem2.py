
# Create account class with 2 attribute balance and account no.
# Create methods for debit credit and printing balance.

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account = acc
    
    def debit(self, amount):
        self.balance -= amount
        print('Bdt: ', amount, 'was debited')
        print('Total balance bdt: ', self.total_balance())
    
    def credit(self, amount):
        self.balance += amount
        print('Bdt: ', amount, 'was credited')
        print('Total balance: ', self.total_balance())

    def total_balance(self):
        return self.balance


a1 = Account(10000, 7017326723475)
a1.debit(1000)
a1.credit(20000)
a1.credit(10000)
