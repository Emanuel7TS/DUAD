"""
3- Cree un diagrama de flujo que pida 3 números al usuario. Si uno de esos números
es 30, o si los 3 sumados dan 30, mostrar “Correcto”. Sino, mostrar “incorrecto”.

"""

number1 = int(input("Type the first number: "))
number2 = int(input("Type the second number: "))
number3 = int(input("Type the third number: "))

if number1 == 30 or number2 == 30 or number3 == 30 or (number1 + number2 + number3) == 30:
    print("*Correct*")
else:
    print("*Incorrect*")