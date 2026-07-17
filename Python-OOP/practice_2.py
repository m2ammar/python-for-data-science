# WAP to take acc_no and balance and print credit, debit, abd balance
class Account:
    
    def __init__(self, balance, account_number ):
        self.balance = balance
        self.account_number = account_number
        
    
    def  debit(self, amount):
        self.balance -= amount
        print(f"New Balance after transaction is : {self.balance} ")
        
    
    def  credit(self, amount):
        self.balance += amount
        print(f"New Balance after transaction is : {self.balance} ")    
        
    def get_balance(self):
        return self.balance
    
    def get_account_number(self):
        return self.account_number    
    
    
a1 = Account(19999, 32143)
a1.credit(1000.66)
a1.debit(300.09)    
print(a1.get_account_number())
print(a1.get_balance())
# in this program we use absraction since every process is
# not being printed but only the result. means only necessary things are 
# are being printed. this is what Abstraction is in python.
# Encapsultion is wrapping all data in a capsule. means all acoount data here in a1 object
    
    
    
         