class Vehicle:
    def __init__(self, make, model, fuel_level=0):
        self.make = make
        self.model = model
        self.fuel_level = fuel_level  # in liters
        self._is_running = False

    def start(self):
        if self.fuel_level > 0:
            self._is_running = True
            print(f"{self.make} {self.model} started.")
        else:
            print(f"{self.make} {self.model} cannot start — no fuel.")

    def refuel(self, amount):
        self.fuel_level += amount
        print(f"Refueled. Fuel level: {self.fuel_level}L")

    def __str__(self):
        status = "running" if self._is_running else "off"
        return f"{self.make} {self.model} ({status}, {self.fuel_level}L)"
    
class ElectricCar(Vehicle):    
    
    def __init__(self, make, model, battery_level=0):
        super().__init__(make, model)
        self.battery_level = battery_level
        
    def start(self):
        if self.battery_level > 0:
            self._is_running = True
            print(f"Staring {self.make} {self.model} with battery level {self.battery_level}")    
        else:
            print(f"Cannot start {self.make} {self.model} due to battery level {self.battery_level}") 
            
            
    def charge(self, amount):
        if self.battery_level < 100:
            self.battery_level = min(self.battery_level + amount, 100)
            print(f"Battery level {self.battery_level}%") 
        else:
            print("Battery is fully charged!")               
            
    
    def __str__(self):
        result = super().__str__()
        temp = result.split(" ")[3].strip("(,")
        return f"{self.make} {self.model} ({temp}, {self.battery_level}%)"
            
 
tesla = ElectricCar("Tesla", "Model 3", battery_level=0)
tesla.start()
tesla.charge(150)
tesla.start()
print(tesla)
            