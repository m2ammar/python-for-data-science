# recursion

# recursive function 
# def show(n):
#     if(n == 0): # base case
#         return
#     print(n)
#     show(n-1)
    
    

# show(9)    

# factorial through recursion
# def fact(a):
#     if a == 0 or a == 1:
#         return 1
#     else:
#         return fact(a-1) * a
    
    
# print(fact(4))

# sum of n natural numbers

# def sum_natural(b):
#     if b == 0:
#         return 0
#     else:
#         return sum_natural(b - 1) + b
        

# sum = sum_natural(6)
# print(sum)

# WAP to print list



def print_names(name, idx):
    if( idx == len(name)):
        return 
    else:
        print(name[idx])
        return print_names(name, idx + 1) 
   
names = ["ali", "ahmed", "raza", "ammar", "saad"]
print_names( names, 0)    
    
    