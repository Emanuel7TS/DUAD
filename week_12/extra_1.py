class Employee:
    def __init__(self,name,salary):
        self._name = name
        if salary < 0:
            raise ValueError("Salary can not be Negative")
        else:
            self._salary = salary

    def promote(self, percentage):

        increase = self._salary * percentage

        self._salary = self._salary + increase
        
        return self._salary

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Value can not be negative")
        else:
            self._salary = value

employee = Employee("Ana", 1000)

print(employee.name)     # Ana
print(employee.salary)   # 1000

employee.promote(0.1)
print(employee.salary)   # 1100

# Cambiar el salario directamente con el setter
employee.salary = 1500
print(employee.salary)   # 1500

# Intentar poner un salario negativo (esto dará error)
employee.salary = -500   # ValueError: Value can not be negative