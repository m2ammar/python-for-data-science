#A student has a name and marks. Marks should be protected — 
#if someone tries to set marks below 0 or above 100, reject it.
#Also the grade should be computed automatically based on marks
#— A for 80+, B for 60+, C for anything below.

class Student:
    
    def __init__(self, name, marks):
        self.name = name
        if marks >= 0 and marks <= 100:
            self.__marks = marks
            
        else:
            print("Invalid marks!")    
            
    @property
    def calc_grade(self):
        
        if self.__marks > 80:
            grade = "A"
        elif self.__marks > 60:
            grade = "B"
        else:
            grade = "C"      
            
        return grade     
           
          
    @property
    def marks(self):
        return self.__marks   
    
    @marks.setter
    def marks(self, value):
        if value >= 0 and value <= 100:
            self.__marks = value
            
        else:
            print("Invalid marks!")   
            
            
        
s1 = Student("Ali", 99)      
print(s1.marks)       # 99
print(s1.calc_grade)  # A
s1.marks = -10        # Invalid marks!
s1.marks = 70
print(s1.calc_grade)  #  

       
          
            