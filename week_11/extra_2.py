class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return self.sound

class Dog:
    def __init__(self, name):
        self.animal = Animal(name, "Guau")

    def speak(self):
        return self.animal.speak()

class Cat:
    def __init__(self, name):
        self.animal = Animal(name, "Miau")

    def speak(self):
        return self.animal.speak()


cat = Cat("Roberto")
dog = Dog("Juan")

print("El gato dice:", cat.speak())  # Miau
print("El perro dice:", dog.speak())  # Guau