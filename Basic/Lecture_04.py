# dictionary

# info = {
#     "key" : "value",
#     "name" : "Ammar",
#     "age" : 20,
#     "marks" : 66.6,
#     "student" : [1, 3, 4, 5],
#     "tup" : ( 1, 4, 55, 2.6 , "Ali",)
# }

# print(info)
# print(type(info))

# print(info["name"])

# info["name"] = "Muhammad"
# info["surname"] = "Ammar"
# print(info)

# null_dict = {}
# print(null_dict)


#nested dictionary
student = {
    "name" : "Ali",
    "subjects" : {
        "phy" : 99,
        "chem" : 66,
        "math" : 100
    },
    
    "class" : 12
}

# print(student)
# print(student["subjects"])

# print(student["subjects"]["chem"])

# print(student.keys()) # return all key
# print(len(student)) # return length

# print(student.values()) # return all values

# print(student.items()) # return all pairs key + value

# both same but we prefer get. since in student[name] it will produce error and not letting run the program entirely
# meanwhile .get(name) will print none. letting execute the other programm. prefered.
# print(student["name"]) 
# print(student.get("name"))

student.update({"city" : "Karachi"}) # add ing city
print(student)

