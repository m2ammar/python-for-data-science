# write a program to take input and print it's length 

# name = input("Enter your name: ")

# print("The length of your name is:", len(name))

# print("The number of times this $ appears is : ", name.count("$"))

# WAP to take input and tell their grade

# grade = int(input("Enter your makrs: "))


# if (grade < 0 or grade > 100):
#     print("Invalid input")
# elif (grade >= 90):
#     print("Grade: A")
# elif (grade >= 80):
#     print("Grade: B")
# elif (grade >= 70):
#     print("Grade: C")
# elif (grade >= 60):
#     print("Grade: D")
# else:
#     print("Grade: F")
    
# WAP to check if input is even or odd

# number = int(input("Enter the number: "))

# if(number % 2 == 0):
#     print("Even number")
# else:
#     print("Odd number")
    
    
# greatest of of three numbers

# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# num3 = int(input("Enter number 3: "))

# if num1 > num2 and num1 > num3:
#     print(f"The bigger number is -> {num1}")
# elif num2 > num1 and num2 > num3:
#     print(f"The bigger number is -> {num2}")
# else:
#     print(f"The bigger number is -> {num3}")
    
# multiple of 13
# number2 = int(input("Enter number: "))

# if number2 % 13 == 0:
#      print("Multiple of 13")
# else:
#      print("Not multiple of 13")
     
#  Login System
save_us= "admin"
save_ps = "1234"

usname = input("Enter your name: ")
password = input("Enter your password: ")

if usname == save_us and password == save_ps:
    print("Login successfully!")
elif usname != save_us and password == save_ps:
    print("Invalid user name")
elif usname == save_us and password != save_ps:
    print("Invalid password")
else:
    print("Invalid credentials")
