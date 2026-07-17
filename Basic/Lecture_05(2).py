# Break

# i = 1

# while i <  10:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# continue
# y = 0

# while y <  10:
    
#     if y == 5:
#         y += 1
#         continue
#     print(y)    
#     y += 1

# For Loop
# nums = [ 1, 2, 3, 4, 5, 6, 7, 8]

# for i in nums:
#     print(i)

# tup = ("apple", "mango", "banana", "orange")

# for var in tup:
#     print(var)
    
# else: # print at the end of loop. not necessary to write
#     print("End")


# squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for i in squares:
#     print(i)
    
    
# search for numeber
# tup1 = ( 1, 4, 9, 16, 25, 36, 49, 64, 81, 100)  
# x = 81

# for val in tup1:
#     if val == x:        #for loop will give number and while will give index
#         print(val)
    


# range in for loop

# for i in range(10): # start from 0 to 9. last value not included.  range(stopvalue)
#     print(i)


# for i in range( 1, 10): # range(start, stop). 1 to 9
#     print(i)


# for i in range( 1, 10, 3): # range(start, stop, step). step means how much increment here we did increment of 3
#     print(i)

# 1 to 10 even numbers

for i in range(1 , 11): # or simpley start from 2 and increment of 2.
    if i % 2 == 0:
        print("Even numbers: ", i) 
        
        