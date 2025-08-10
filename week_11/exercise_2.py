"""2. cree una clase de `Bus` con:
    1. Un atributo de `max_passengers`.
    2. Un método para agregar pasajeros uno por uno (que acepte como parámetro una instancia de la clase `Person` vista en la lección).
    **Este solo debe agregar pasajeros si lleva menos de su máximo.** Sino, debe mostrar un mensaje de que el bus está lleno.
    3. Un método para bajar pasajeros uno por uno (en cualquier orden)."""

class Person:
    def __init__(self, id, name):
        self.id = id  
        self.name = name  

class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers  
        self.onboard_passengers = []  

    def board_person(self, person):
        if len(self.onboard_passengers) < self.max_passengers:
            self.onboard_passengers.append(person)  
            print(f"{person.name} has boarded the bus.")
        else:
            print("The bus is full!")

    def unboard_person(self, person):
        if person in self.onboard_passengers:
            self.onboard_passengers.remove(person)  
            print(f"{person.name} has left the bus.")
        else:
            print(f"{person.name} is not on the bus.")

school_bus = Bus(2)


person1 = Person(1, "Emanuel")
person2 = Person(2, "Kito")
person3 = Person(3, "Alek")


school_bus.board_person(person1) 
school_bus.board_person(person2)  
school_bus.board_person(person3)  

school_bus.unboard_person(person1)  