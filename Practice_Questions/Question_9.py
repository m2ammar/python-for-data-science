class BankAccount:
    
    def __init__(self, owner, balance=0):
        
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount    

    def __str__(self):
       
       return(f"{self.owner}'s account: Rs. {self.balance}")


# Test
acc = BankAccount("Ammar", 1000)
acc.deposit(500)
acc.withdraw(2000)   # should fail — insufficient balance
acc.withdraw(300)    # should succeed
print(acc)