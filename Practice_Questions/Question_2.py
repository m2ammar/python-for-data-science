#Write a class Account with attributes owner and balance (starts at 0).
#Give it two methods: deposit(amount) which adds to the balance 
#(but rejects negative amounts — just print a message and don't change balance),
#and __str__ which returns something like "Ammar's account: Rs. 500".

class Account:


    
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
        
            
    def deposit(self, amount):
        
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid input!") 
    
    def __str__(self):
        return f"{self.owner}'s account: Rs. {self.balance}"  
    

a1 = Account("Ammar")    
a1.deposit(500)
print(a1)
        



