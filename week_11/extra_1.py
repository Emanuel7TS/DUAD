class Rectangle:
    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("Width and height cannot be negative.")
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)


while True:
    try:
        height = int(input("Enter a height: "))
        width = int(input("Enter a width: "))
        
        if width < 0 or height < 0:
            print("Width and height cannot be negative.")
            continue

        rectangle1 = Rectangle(width, height)
        print("Area:", rectangle1.get_area())
        print("Perimeter:", rectangle1.get_perimeter())
        break

    except ValueError:
        print("Please enter a valid number.")