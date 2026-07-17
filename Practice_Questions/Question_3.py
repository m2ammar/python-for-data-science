class Wallet:
    
     def __init__(self, starting_balance=0):
        if starting_balance < 0:
            raise ValueError("Starting balance cannot be negative.")
        self._balance = starting_balance

    
     @property
     def balance(self):
        return self._balance
    
    
     def __add__(self, other):
        if isinstance(other, Wallet):
            return Wallet(self._balance + other.balance)
        return Wallet(self._balance + other)
    
    
     @classmethod
     def from_dict(cls, data):
      balance = data.get("starting_balance", 0)
      return cls(balance)
    
     @staticmethod
     def is_valid_amount(amount):
        
        if amount >= 0:
            return True
        else:
            return False
    
     def __str__(self):
        return (f"Wallet(balance={self._balance})")             
    
    
w1 = Wallet(100)
w2 = Wallet.from_dict({"starting_balance": 250})

w3 = w1 + w2
print(w3)                          # Wallet(balance=350)
print(w1.balance, w2.balance)      # 100 250   <- originals unchanged

print(Wallet.is_valid_amount(-5))  # False
print(Wallet.is_valid_amount(20))  # True

try:
    w4 = Wallet(-50)
except ValueError as e:
    print("Caught:", e)
           
        
