"""
💪🏽 **Ejercicios**
1. Cree dos funciones que impriman dos cosas distintas,
 y haga que la primera llame la segunda.
"""

def print_message_1():
    print("Hello there")
    print_message_2()  

def print_message_2():
    print("I am tested functions")

print_message_1()





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





"""
3. Cree una función que retorne la suma de todos los números de una lista.
    1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
"""

number_list = [4, 8, 15, 16, 23, 42, 7, 13, 29, 31]

def sum_number_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

result = sum_number_list(number_list)
print(f"The total sum is: {result}")





"""
4. Cree una función que le de la vuelta a un string y lo retorne.
    1. Esto ya lo hicimos en iterables.
    2. “Hola mundo” → “odnum aloH”
    """
    
def string_reverse():
    reverse_word  = str(input("Enter a word to see in reverse: "))
    for i in range(len(reverse_word) - 1, -1, -1):
        print(reverse_word[i])
    return reverse_word

string_reverse()





"""
5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”
"""

def letter_case_counter():
    upper_counter = 0
    lower_counter = 0

    text_entered = input("Enter text: ")
    

    for char in text_entered:
        if char.isupper():        
            upper_counter += 1
        elif char.islower():      
            lower_counter += 1

    print(
        f"There are {upper_counter} uppercase letters and "
        f"{lower_counter} lowercase letters in \"{text_entered}\"."
    )

    return upper_counter, lower_counter

letter_case_counter()





"""
6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
    1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
    2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”
"""


def sort_string():
    
    entered_string = input("Enter text separated by hyphens: ")
    words_list = entered_string.split("-")
    words_list.sort()
    ordered_string = ""
    
    for i, word in enumerate(words_list):
        ordered_string += word
        if i < len(words_list) - 1:
            ordered_string += "-"
            
    return ordered_string

result = sort_string()
print(result)





"""
7. Cree una función que acepte una lista de números
y retorne una lista con los números primos de la misma.
1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = int(math.sqrt(n))
    i = 5
    while i <= limit:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def filter_primes(numbers):
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    return primes
    
result = filter_primes([1, 4, 6, 7, 13, 9, 67])
print(result)