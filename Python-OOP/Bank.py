#A bank wants to track how many accounts have been created. 
#Every account has an owner name and a balance. There should
#also be a utility method that checks if a given amount is valid
#(greater than zero) — this method doesn't need any account data to do its job.

class Bank:
    count = 0
    
    
    def __init__(self, name , balance):
        
        self.name = name
        if Bank.utility(balance):
            self.balance = balance
            Bank.count += 1
        else:
            print("Invalid input!")    
        
        
        
    @staticmethod 
    def utility(balance):
        if balance > 0:
            return True
        else:
            return False        
            
    @classmethod    
    def total_count(cls):
        print(f"Total accoutns: {cls.count}")
   
        
b1 = Bank("Ali", 88)
b2 = Bank("Ammar", 28)
b3 = Bank("Ahmed", 43)
b4 = Bank("Saad", -11)
b5 = Bank("Khwaja", 53)
b6 = Bank("Hassaan", 99)
Bank.total_count()
        
              



