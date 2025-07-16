# Ejercicios Extra (Pseudocódigo)

"""
1- Cree un algoritmo que le pida 2 números al usuario, los guarde en dos variables distintas
(primero y segundo) y los ordene de menor a mayor en dichas variables.
"""


first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))


print("\nNumbers in ascending order:")

if first_number <= second_number:
    print(first_number)
    print(second_number)
else:
    print(second_number)
    print(first_number)