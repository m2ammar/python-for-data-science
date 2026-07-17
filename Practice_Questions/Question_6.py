class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator

    def simplify(self):
        a, b = abs(self.numerator), abs(self.denominator)
        while b:
            a, b = b, a % b
        gcd = a if a != 0 else 1
        return Fraction(self.numerator // gcd, self.denominator // gcd)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


# TASK: Create a subclass MixedFraction that:
# - Takes whole, numerator, denominator in __init__ (e.g. MixedFraction(1, 3, 4) means 1 and 3/4)
#   and stores it internally using the parent's numerator/denominator representation
#   (hint: convert to an improper fraction before calling super().__init__)
# - Overrides __str__ to display as "whole numerator/denominator" format, e.g. "1 3/4"
#   (if the fraction part simplifies to 0, just show the whole number with no fraction)
# - Implements __add__ so that adding two MixedFraction objects returns a new MixedFraction
#   (result should be simplified, and if numerator >= denominator after adding, carry it into whole)
# - Implements __lt__ so MixedFraction objects can be compared with < (compare actual values, not just numerators)




class MixedFraction(Fraction):
    
    def __init__(self, whole ,numerator, denominator):
        num = whole * denominator + numerator
        super().__init__(num, denominator)
        self.whole = whole
        
    def __str__(self):
        f = self.simplify()

        whole = f.numerator // f.denominator
        remainder = f.numerator % f.denominator

        if remainder == 0:
            return str(whole)
        else:
            return f"{whole} {remainder}/{f.denominator}"
        
    def __add__(self, other):
        numerator = (self.numerator * other.denominator +
                     other.numerator * self.denominator)
        denominator = self.denominator * other.denominator

        temp = Fraction(numerator, denominator).simplify()

        whole = temp.numerator // temp.denominator
        remainder = temp.numerator % temp.denominator

        return MixedFraction(whole, remainder, temp.denominator)
    
    def __lt__(self, other):
        return (self.numerator * other.denominator <
                other.numerator * self.denominator)
        
            

# Expected behavior:
a = MixedFraction(1, 3, 4)   # 1 and 3/4
b = MixedFraction(2, 1, 2)   # 2 and 1/2
print(a)        
# Expected: 1 3/4

result = a + b
print(result)   
# Expected: 4 1/4

print(a < b)    
# Expected: True

c = MixedFraction(0, 4, 4)  # 0 and 4/4 → should simplify to just "1"
print(c)
# Expected: 1


        
    
        

    