import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def circumference(self):
        return 2 * math.pi * self.radius

c = Circle(5)
print(f"Radius: {c.radius}")
print(f"Area: {c.area:.2f}")
print(f"Circumference: {c.circumference:.2f}")