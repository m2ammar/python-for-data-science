# sets
# collection = { 1, 2, 3, 4, "hi"} # order can be different. it is un ordered. duplicate values ignore hojati

# print(collection)
# print(type(collection))
# for empty set

# collection1 = set()
# print(type(collection1))
# # sets are mutable but their elements aren't

# collection1.add(5) # add 5
# collection1.add(4)# add 4
# collection1.add(3) # add 3
# collection1.add("hi") # add hi
# collection1.add((1,2,3,4)) # tup can be added not list
# print(collection1)

# collection1.remove(5) #remove 5
# print(collection1)

# collection1.clear() # clear all empty set
# print(collection1)

# collection1.pop() # random value will be deleted
# print(collection1)

# union and intersection

set1 = {1,2, 4, 5}
set2 = { 4 ,5, 6, 8}

print(set1.union(set2)) # combine both set and return values. won't combine permanently

print(set1.intersection(set2)) # combine common values and return them


