#Question 2
#A school system has three levels: a general Person with a name and age, 
#a Student who is a person but also has a grade, and a SchoolCaptain 
#who is a student but also has a term (how long they've been captain). 
#When you print a school captain's info, it should show all three levels of detail.

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name} ", f"Age: {self.age}")    
        
class Student(Person):
    
    def __init__(self, name, age, grade):
        super().__init__(name, age) 
        self.grade = grade
        
    def display_info(self):
        super().display_info()
        print(f"Grade: {self.grade}")      
        
class SchoolCaptain(Student):
    
    def __init__(self, name, age, grade, duration):
        super().__init__(name, age, grade)
        self.duration = duration
        
    def display_info(self):
        super().display_info()
        print(f"Duration: {self.duration}")                   
                        
s1 = SchoolCaptain("Ahmed", 44, "A", 55)   
s1.display_info()                     
                        
                        
                         