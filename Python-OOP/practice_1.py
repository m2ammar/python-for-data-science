#WAP to take name and marks of three subject then print avg

class Student:
    
    def __init__(self, name, phy, chem , math):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.math = math
        
    
    def calc_avg(self):
        
        avg = (self.phy + self.chem + self.math) /3
        print(f"The average of student {self.name} is: {avg:.2f}")  
        
        
    @staticmethod # decorator. this is an static method. it'll be called with class name with no self parameter
    def welcome():
        print("Welcome ")     
        
        
s1 = Student("Ammar", 99, 77, 33)
s1.calc_avg()       
Student.welcome()  
        
        
        
        
    