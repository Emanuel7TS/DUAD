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