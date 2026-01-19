# Big O Notation
# O(n) = lineal, depende de n
# O(1) = constante: no depende de n
# O(n²): cuadrático → depende de n²
# O(n³): cúbico → depende de n³
# O(log n): logarítmico → depende de log(n)


def print_all_pairs(my_dict):
    for key1 in my_dict:                    # O(n)
        for key2 in my_dict:                # O(n) = O(n²)
            print(f"{key1}-{key2}")         # O(1)

# Big-O final: O(n²), debido a dos bucles anidados que dependen de n.


# - Preguntas:

# - ¿Cuál es la complejidad temporal?
# Big-O final: O(n²), debido a dos bucles anidados que dependen de n.

# - ¿Cuanto dura si hay `1` millón de claves?

# Con 1 millón de claves, el algoritmo realizaría aproximadamente 1 billón de operaciones, lo cual es inviable en la práctica.
# El tiempo de ejecución sería extremadamente alto y no usable.