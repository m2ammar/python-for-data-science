#A program needs to manage rectangular boxes. Each box has a width and height. You should be able to:
#Add two boxes together (adds their widths and heights)
#Compare two boxes with > to see which has a larger area
#Print a box nicely without manually accessing its attributes

class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height
        
        
    def __add__(self, other):
        return     Rectangle(self.width + other.width, self.height + other.height)
    
    def __gt__(self, other):
        return (self.area > other.area)
    
    def __str__(self):
        return f"Rectangle's Width: {self.width} and Height: {self.height} "
        
r1 = Rectangle(4, 6)
r2 = Rectangle(2 , 7)
r1 > r2
r3 = r1 + r2
print(r3)
print(r1)
        
            