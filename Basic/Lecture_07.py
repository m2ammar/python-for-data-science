#file I/O

# f = open("demo.txt", "r") # reading files. if the file isn't in the same folder then give the complete path here

# data = f.read(4) # it'll read the first 4 character
# print(data)
# print(type(data))
# f.close()

# f = open("demo.txt", "r") # reading files. if the file isn't in the same folder then give the complete path here

# line1 = f.readline() # it'll read line by line
# print(line1)
# print(type(line1))
# f.close()

# f2 = open("demo2.txt", "w")# it'll replace the text will new one

# f2.write("This will be written in the demo2 replacing the previous data. This is the work being done by w")
# f2.close()

# f2 = open("demo2.txt", "a")# it'll append the demo2 means will add these given line at the end of file

# f2.write("\nThis is gonna be add at the end of file becuase of a. a means appned. add at the end")
# f2.close()

# f3 = open("sample.txt", "w")# no such file exist so it'll create a file like this ot write. w and a both do this
# f3.close()


# with proper syntax

with open("demo.txt", "r") as f4: #with it'll automatically close the file
    d = f4.read()
    print(d)




