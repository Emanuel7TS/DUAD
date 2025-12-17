class Person:
    def __init__(self,name,age):
        self.name = name
        self._age = age
    
    def greet(self):
        print(f"{self.name} ({self._age} years) is saying hello")

    def birthday(self,added_age):
        self._age += added_age
        self.greet()

person1 = Person("Emanuel",26)
person2 = Person("Kitos",28)

person1.birthday(1)
person1.greet()
person2.greet()