class Vehicle():
    def __init__(self,brand,year):
        self._brand = brand
        self._year = year

    def get_info(self):
        return f"This Vehicle is a {self._brand} from year {self._year}."

class Car(Vehicle):
    def __init__(self, brand, year, doors):
        self.doors = doors
        super().__init__(brand, year)

    def get_info(self):
        return f"This Vehicle is a {self._brand} from year {self._year}, and has {self.doors} doors."

class Motorcicle(Vehicle):
    def __init__(self, brand, year, type):
        self.type = type
        super().__init__(brand, year)

    def get_info(self):
        return f"This Vehicle is a {self._brand} from year {self._year}, and is a {self.type} model."
    

veh1 = Car("Toyota", 2020, 5)
print(veh1.get_info())

veh2 = Motorcicle("Husqvarna", 2023, "Special")
print(veh2.get_info())