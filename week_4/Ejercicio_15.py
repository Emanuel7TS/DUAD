# Ejercicios diagramas de flujo

"""
1- Cree un diagrama de flujo que le pida 5 números al usuario y muestre el mayor.
"""

max_number = int(input("Type number #1: "))

for i in range(1, 5):
    number = int(input(f"Type number #{i+1}: "))
    if number > max_number:
        max_number = number

print(f"The greatest number is: {max_number}")


"""
2- Cree un diagrama de flujo que le pida un numero al usuario y muestre “Fizz”
si es divisible entre 3, “Buzz” si es divisible entre 5, y
“FizzBuzz” si es divisible entre ambos.
"""

number = int(input("Type a number: "))

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(f"The number {number} is not divisible by 3 or 5.")