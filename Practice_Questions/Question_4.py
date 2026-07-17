class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
        return self._balance

    def __str__(self):
        return f"{self.owner}'s account: {self._balance}"
    
    

class SavingsAccount(Account):
    
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)    
        self.interest_rate = interest_rate
        
    def deposit(self, amount):
        self._balance += amount + ( amount * self.interest_rate)
        return self._balance 
       
    def apply_yearly_interest(self):
        
        self._balance +=  self._balance * self.interest_rate   
        return self._balance 
        
s = SavingsAccount("Ali", 1000, 0.05)
print(s.deposit(200))   # 1210.0  -> 200 deposit + 10 bonus (5% of 200) = 210, balance 1000+210
print(s.apply_yearly_interest())  # 1270.5 -> 1210 + 5% of 1210 = 1270.5
print(s)   # Ali's account: 1270.5        
        
        