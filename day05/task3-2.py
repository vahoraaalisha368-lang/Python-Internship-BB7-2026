class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

f1 = Fraction(1, 2)
f2 = Fraction(1, 3)
f3 = f1 + f2  
print(f"{f1} + {f2} = {f3}")  