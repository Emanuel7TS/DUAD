# Ejercicios diagramas de flujo

"""
 1- (todo el bloque de pseudocodigo anteriormente mostrado
"""

"""
2- Cree un diagrama de flujo que tenga un numero secreto del 1 al 10, y le pida al usuario
adivinar ese número. El algoritmo no debe terminar hasta que el usuario adivine el numero.
"""

import random

secret_number = random.randint(1, 10)
user_guess = 0

print("     Guess the Secret Number\n")
print("A secret number between 1 and 10 has been chosen.")
print("Keep guessing until you get it right!\n")

while user_guess != secret_number:
    user_guess = int(input("Type a number between 1 and 10: "))
    while user_guess < 1 or user_guess > 10:
        print("Wrong input, please type a number from 1 to 10")
        user_guess = int(input("Type a number between 1 and 10: "))
    if user_guess != secret_number:
        print("*** Wrong number ***\n")

print(f"\nCongrats!! You win, {secret_number} is the number.")