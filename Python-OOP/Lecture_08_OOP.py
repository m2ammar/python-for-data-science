#OOP

class Student:
    college_name = "KSBL" # same college of everyone so it's a class attribute. same as static attributes but in python
    name = "Anonymous"
    
    def  __init__(self, id ,fullname):
        self.id = id
        self.name=fullname
        
        
    def hello(self): #self is essential  
        print("Hello ", self.name) # we can use self.name or just name  
    
    def getId(self):
        return self.id    
        
s1 = Student(1, "Ammar") # this name will be printed not anonymous since we passed the parameter
print(s1.id)
print(s1.name)  
s1.hello()
print(s1.getId())








      