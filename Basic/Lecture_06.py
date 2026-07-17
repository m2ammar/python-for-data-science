# Functions

# def calc_sum(a, b):
#     return a + b

# print(calc_sum(1 ,3))

# def calc_sum(a, b=10): #default value if no argument passed
#     return a + b

# print(calc_sum(5))

# Temperature Converter
# def convert_temp(temp, unit):
#     # your code here
#     if unit == "C":
#        temp1 =  ( temp * 9/5) + 32
#        return temp1
#     elif unit == "F":
#         temp2 = (temp - 32) * 5/9 
#         return temp2
#     else:
#         print("Invalid input")
    
    

# print(convert_temp(100, "C"))
# print(convert_temp(32, "F"))


# def avg_num(a, b, c):
#     avg = (a + b + c) /3
#     print("average: ", avg)
    

# avg_num( 1, 2, 3)    

# def calc_fact(n):
#     fact = 1
#     for i in range(1 , n+1):
#         fact *= i
    
#     print(fact)    

# calc_fact(3)

def usd_pkr(e):
    
    temp = e * 278.15
    return temp

print(usd_pkr(2))


