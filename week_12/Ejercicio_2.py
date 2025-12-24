from abc import ABC, abstractmethod
import math

class Shape(ABC):  
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return round(perimeter, 2)
    
    def calculate_area(self):
        area = math.pi * (self.radius ** 2)
        return round(area, 2)


class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def calculate_area(self):
        area = self.side * self.side
        return round(area, 2)
    
    def calculate_perimeter(self):
        perimeter = self.side * 4
        return round(perimeter, 2)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        perimeter = (self.width + self.height) * 2
        return round(perimeter, 2)
        
    def calculate_area(self):
        area = self.width * self.height
        return round(area, 2)


# Mixins para herencia múltiple
class ColorMixin:
    def __init__(self, shape_color):
        self.shape_color = shape_color

class PrintableMixin:
    def __init__(self, print_shape):
        self.print_shape = print_shape


class Triangle(Shape, ColorMixin, PrintableMixin):
    def __init__(self, base, height, side, shape_color, print_shape):
        self.base = base
        self.height = height
        self.side = side

        # inicializar mixins
        ColorMixin.__init__(self, shape_color)
        PrintableMixin.__init__(self, print_shape)

    def calculate_area(self):
        area = (self.base * self.height) / 2
        return round(area, 2)
    
    def calculate_perimeter(self):
        perimeter = 3 * self.side
        return round(perimeter, 2)


# --- Pruebas ---
c = Circle(5)
print("Circle area:", c.calculate_area())
print("Circle perimeter:", c.calculate_perimeter())

s = Square(4)
print("Square area:", s.calculate_area())
print("Square perimeter:", s.calculate_perimeter())

r = Rectangle(6, 3)
print("Rectangle area:", r.calculate_area())
print("Rectangle perimeter:", r.calculate_perimeter())

t = Triangle(10, 5, 7, "rojo", "Soy un triángulo")
print("Triangle area:", t.calculate_area())
print("Triangle perimeter:", t.calculate_perimeter())
print("Triangle color:", t.shape_color)
print("Triangle print:", t.print_shape)