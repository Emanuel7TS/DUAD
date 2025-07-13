# Ejercicios de Iterables y Listas  ✔

"""
1. Cree un programa que itere e imprima los valores de dos listas
del mismo tamaño al mismo tiempo.
"""

first_list = ["Hay", "en", "que", "iteracion", "indices", "muy"]
second_list = ["casos", "los", "la", "por", "es", "util"]

for index in range (0, len(first_list)):
    print(first_list[index])
    print(second_list[index])