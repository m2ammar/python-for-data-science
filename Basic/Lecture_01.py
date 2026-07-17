# name = "Ammar"
# age = 20
# city = "Karachi"
# cgpa = 3.28
# student = True
# semester_remain = 8 - 2
# print("Name: ", name) , print("Age: ", age) 
# print("City: ", city) 
# print("CGPA: ", cgpa) 
# print("Student: ", student) 
# print("Semesters remaining: ", semester_remain)
# print(type(name))
# print(type(age))
# print(type(city))
# print(type(cgpa))
# print(type(student))
# print(type(semester_remain))


# a = 5
# b = 2
# print(a % b)
# print( a ** b) # a^b

# relational operators

# c = 50
# d = 20
# print(c < d)
# print(c > d)
# print(c == d)
# print(c != d)
# print(c <= d)
# print(c >= d)

# assignment operators

# num = 10
# num += 10

# print("Number: ", num)

# num = 10
# num *= 10
# print("Number: ", num)

# num = 10
# num /= 10
# print("Number: ", num)

# num = 10
# num //= 10
# print("Number: ", num)

# num = 10
# num %= 10
# print("Number: ", num)

# num = 10
# num **= 5 # 10^5
# print("Number: ", num)

# logical operators

print(not True) # not opposite of True is False
print(not False)

a = 5
b = 2
print( not (a < b) )

var1 = True
var2 = False
print("AND operator: ", var1 and var2) # both should be true to get true
print("OR operator: ", var1 or var2) # at least one should be true to get true

# Converson between data types

a , b = 2 , 5.5 # it will be done by python automatically, but we can also do it manually.

sum = a + b
print("Sum: ", sum)

a , b = "2" , 5 # this is type casting. doing it manually. we can not add string and integer together.
sum = float(a) + b
print("Sum: ", sum)

# inpurt() function is used to take input from user. it always returns a string. we can convert it to other data types if needed.
name = input("Enter your name: ")
print("Hello, ", name)

age = input("Enter your age: ")
print("Age: ", age)

marks = int(input("Enter your marks: "))
print("Marks: ", marks)