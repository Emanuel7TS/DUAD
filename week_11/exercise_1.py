import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)


Circle1 = Circle(12)
print("El área del círculo es:", round(Circle1.get_area(), 2))