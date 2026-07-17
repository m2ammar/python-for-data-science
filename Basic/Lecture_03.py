# list

# marks = [ 44, 66.8, 66, 88, 99.9]

# print(marks)
# print(type(marks))

# print(marks[0])
# print(marks[4])
# print(len(marks))

# # we can store multiple types of value in a single list

# student = ["Ammar", 99, 20,  "Karachi"]
# print(student)

# #in string you can't assign or change the value since strings are immutable.
# # while list are mutable. we can change the value

# student[0] = "Muhammad"
# print(student)

# # list slicing same rule as string.

# print(marks[ 1 : 4]) #last is not included
# print(marks[  : 4]) # start from 0 last not included
# print(marks[ 3 : ]) # 3 to end last not included. same for minus

# list method
# num = [ 1,2, 6,74, 3]
# num.append(55) # add at the end 55. retuen. None
# print(num)
# num.sort() # sort in ascending order in the main string will return None.
# print(num)
# num.sort(reverse= True) # desc order
# print(num)
# num.reverse() # reverse in the main list. no ascending no desc. if list is 23463 it will reverse 36432

# # insert(index, element)
# num.insert(0, 4) # it'll add not replace
# print(num)

# remove and pop
# list = [ 2, 3, 5, 1, 3, 4]
# list.remove(3) # it'll remove first three in the list
# print(list)

# list.pop(0) # it'll will remove element at 0
# print(list)

# tuples

tup = ( 1, 2, 3, 4, 5,)
print(tup)
print(type(tup))
print(tup[0]) # same as list but we can't do assignemnt. immutable

# empty tuple
tup1 = ()
print(tup1)
print(type(tup1))

tup2 = (1,) # for single value tuple alway end with ,. if not use , it'll not be tuple
print(tup2)
print(type(tup2))

# slicing same as list or string

tup3 = ( 1, 8, 3, 4, 8,)
print(tup3[1 : 2])

# methods
# find certain index with value do this:
print(tup3.index(8))
#count ow many times an element appears
print(tup3.count(8))