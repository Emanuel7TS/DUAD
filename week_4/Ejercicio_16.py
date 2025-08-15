"""
3- Cree un diagrama de flujo que le pida 100 números al usuario y muestre la suma de todos.
"""

total = 0
for i in range(100):
    number = int(input(f"Type number #{i+1}: "))
    total += number

print(f"The total sum of all numbers is: {total}")

"""
4- Cree un diagrama de flujo que le pida 100 números al usuario y muestre el mayor de todos.
"""

max_number = int(input("Type number #1: "))

for i in range(1, 100):
    number = int(input(f"Type number #{i+1}: "))
    if number > max_number:
        max_number = number

print(f"The greatest number among the 100 entered is: {max_number}")


# Brain-damage :(