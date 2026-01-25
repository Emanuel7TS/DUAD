#                                                                                                       Ejercicio 1

# nota: algunas funciones se modificaron un poco para poder hacer mejores test

my_test_list = [18, -11, 68, 6, 32, 53, -2]

def bubble_sort(data):
    if not isinstance(data, list):
        raise TypeError("data must be a list")

    for lap in range(len(data) - 1):
        for number in range(len(data) - 1 - lap):
            if data[number] > data[number + 1]:
                data[number], data[number + 1] = data[number + 1], data[number]
    return data

sorted_list = bubble_sort(my_test_list)

print(sorted_list)


# ----------------------------------------------------------------------------------------------------------------------------------------------------------

#                                                                                                       Ejercicio 2

# Cree una función que retorne la suma de todos los números de una lista.

#  1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).

number_list = [4, 8, 15, 16, 23, 42, 7, 13, 29, 31]

def sum_number_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

result = sum_number_list(number_list)
print(f"The total sum is: {result}")




# ----------------------------------------------------------------------------------------------------------------------------------------------------------


# Cree una función que le de la vuelta a un string y lo retorne.
# 1. Esto ya lo hicimos en iterables.
# 2. “Hola mundo” → “odnum aloH”


def string_reverse(word):
    if not isinstance(word, str):
        raise TypeError("data must be a string type")
    reversed_word = ""
    for i in range(len(word) - 1, -1, -1):
        reversed_word += word[i]
    return reversed_word


# ----------------------------------------------------------------------------------------------------------------------------------------------------------



# Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
# 1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”

def letter_case_counter(sentence):
    upper_counter = 0
    lower_counter = 0

    for char in sentence:
        if char.isupper():        
            upper_counter += 1
        elif char.islower():      
            lower_counter += 1

    print(
        f"There are {upper_counter} uppercase letters and "
        f"{lower_counter} lowercase letters in \"{sentence}\"."
    )

    return upper_counter, lower_counter


# ----------------------------------------------------------------------------------------------------------------------------------------------------------



# Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
# 1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
# 2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

def sort_string(entered_string):
    if not isinstance(entered_string, str):
        raise TypeError("data must be a string")

    words_list = entered_string.split("-")
    words_list.sort()
    ordered_string = ""

    for i, word in enumerate(words_list):
        ordered_string += word
        if i < len(words_list) - 1:
            ordered_string += "-"

    return ordered_string


# ----------------------------------------------------------------------------------------------------------------------------------------------------------



# 7. Cree una función que acepte una lista de números
# y retorne una lista con los números primos de la misma.
# 1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]

import math

def is_prime(numbers):
    if not isinstance(numbers,(int,float)):
        raise TypeError("data must be numbers")
    if numbers <= 1:
        return False
    if numbers <= 3:
        return True
    if numbers % 2 == 0 or numbers % 3 == 0:
        return False
    limit = int(math.sqrt(numbers))
    i = 5
    while i <= limit:
        if numbers % i == 0 or numbers % (i + 2) == 0:
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


# ----------------------------------------------------------------------------------------------------------------------------------------------------------

#                                                                                         Ejercicio extra 1

def sum_numbers(a, b):
    return a + b


def calculate_average(a, b):
    return (a + b) / 2


def convert_to_list(a, b):
    return [a, b]


# ----------------------------------------------------------------------------------------------------------------------------------------------------------


#                                                                                         Ejercicio extra 2

def divide(number1, number2):
    if number2 == 0:
        raise ValueError("No se puede dividir por cero")
    return number1 / number2


# ----------------------------------------------------------------------------------------------------------------------------------------------------------


#                                                                                         Ejercicio extra 3

def read_lines(path):
    with open(path, 'r') as f:
        return f.readlines()


# ----------------------------------------------------------------------------------------------------------------------------------------------------------