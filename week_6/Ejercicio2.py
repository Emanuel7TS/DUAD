"""
2. Experimente con el concepto de scope:
    1. Intente accesar a una variable definida dentro de una función desde afuera.
    2.  Intente accesar a una variable global desde una función y cambiar su valor.
"""

number1 = 10
number2 = 5

def sum_values():
    value1 = int(input("Enter value 1: "))
    value2 = int(input("Enter value 2: "))
    total = value1 + value2
    return total

total_result = sum_values()
print(f"The total sum is: {total_result}")


# 1. print(value1)  # NameError: name 'value1' is not defined

def division_values():
    global number1
    number1 = 20
    division = number1 / number2
    return division

# 2
print(f"Antes de modificar, number1 vale: {number1}")
division_result = division_values()
print(f"Después de modificar, number1 vale: {number1}")
print(f"The division result is: {division_result}")