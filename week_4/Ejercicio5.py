"""
    #Ejercicio 4
    Cree un programa que le pida tres números al usuario y muestre el mayor.
"""

option1 = int(input("Type first number: "))
option2 = int(input("Type first number: "))
option3 = int(input("Type first number: "))

if option1 >= option2 and option1 >= option3:
    greatest = option1
elif option2 >= option1 and option2 >= option3:
    greatest = option2
else:
    greatest = option3

print(f"The greatest value is: {greatest}")