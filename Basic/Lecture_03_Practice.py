#Q1: Create a = [1, 2, 3], set b = a, then append 4 to b.
# Predict what a will print — then fix it so a stays unaffected, using .copy().

#a = [1, 2, 3]
# b = a
# b.append(4)
# print(a)

# b = a.copy()
# b.append(4)
# print(a)

# Q2: Given fruits = ["apple", "banana", "apple", "cherry", "apple"], 
# remove only the first occurrence of "apple" and print the result. 
# Then, starting fresh from the original list, remove all occurrences 
# of "apple" (think about why looping with .remove() naively might skip one).

#fruits = ["apple", "banana", "apple", "cherry", "apple"]
# fruits.remove("apple")
# print(fruits)

# print(fruits.count("apple"))
# fruits.remove("apple")
# fruits.remove("apple")
# fruits.remove("apple")
# print(fruits)

# Q3 (last one): Create coords = (4, 8, 15, 16, 23, 4).
# Find the index of the first 4, and separately, 
# count how many times 4 appears in the tuple.

coords = (4, 8, 15, 16, 23, 4)
print(coords.index(4))
print(coords.count(4))






