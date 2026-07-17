class Vehicle:
    
    def __init__(self, make, year):
        self.make = make
        self.year = year
        
    def display_info(self):
        print(f"Vehicle Info: {self.make} ({self.year})")
        
        
            
    
class Car(Vehicle):
    
    def __init__(self, make , year, door):
        super().__init__(make, year)
        self.door = door
        
        
    def display_info(self):
        
        super().display_info()
        print(f"Car Detail: {self.door} doors")    
        
        
c1 = Car("Toyota", 2022, 4)        
c1.display_info()        
