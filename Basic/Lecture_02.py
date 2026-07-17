# escape sequence

str1 = "This is the string.Now here we'll add a new line.\nthis is the new line.\tthis will add tab space"
print(str1)

#concatanation
str2 = "Ammar"
str3 = "Saleem"

print(str2 + " " +  str3)

# length of function

print(len(str2))

#indexing

print(str3[4])

#slicing

name = "Ammar Saleem"
print(name[1 : 5]) # here it will print from index 1 to 4, as the last index is not included in slicing

print(name[ : 2]) # same as 0 to 2
print(name [ 0 : ]) # same as 0 to end of string

# negative indexing
print(name[-3 : -1])  # it will start from end of word. same rule first till second lat word include not last


# String functions
name = "all about me"

print(name.endswith("me")) # it will return true if the string ends with "me!" otherwise false

print(name.capitalize()) # it will capitalize the first letter of the string by creating a new string

# for capitalization of main string permanently
name = name.capitalize()    
print(name)

# replace function
print(name.replace("me", "you")) # it will replace the word "me" with "you" and create a new string
print(name) # it will print the original string as the replace function does not change the original string

name = name.find("All") # it will return the index of the first letter of the word "All" in the string
print(name)

# count function
name = "all about me"
print(name.count("a")) # it will return the number of times the letter "a"