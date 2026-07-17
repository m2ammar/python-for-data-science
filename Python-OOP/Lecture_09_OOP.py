#Second part of OOP

# class Student:
    
    
#     def __init__(self, id , name):
#         self.id = id 
#         self.name = name
        
        
# s1 = Student(1, "Ammar")
# print(s1.id)
# print(s1.name)

# del s1.id        
# print(s1.id)

class Account:
    
    def __init__(self, acc_no, acc_pass):
        self.__acc_no = acc_no
        self.__acc_pass = acc_pass


a1 = Account(1234, "Ali12")
print(a1.__acc_pass)
# for making anything attributes or methods private use double underscore before it like __name
        
        

