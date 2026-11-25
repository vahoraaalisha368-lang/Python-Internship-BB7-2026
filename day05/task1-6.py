class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.area() == other.area()

r1 = Rectangle(4, 5)
r2 = Rectangle(2, 10) 
r3 = Rectangle(3, 3)  

print(r1 == r2)  
print(r1 == r3)  
print(f"r1 area: {r1.area()}, r2 area: {r2.area()}")