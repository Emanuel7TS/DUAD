# Big O Notation
# O(n) = lineal, depende de n
# O(1) = constante: no depende de n
# O(n²): cuadrático → depende de n²
# O(n³): cúbico → depende de n³
# O(log n): logarítmico → depende de log(n)

# 1. Considere los siguientes dos algoritmos:


def linear_search(my_list, target):
    for item in my_list:                # O(n)
        if item == target:              # O(1)
            return True
    return False

# Big-O final: O(n) la busqueda depende de 'n'.



def binary_search(my_list, target):
    low = 0                                 # O(1)
    high = len(my_list) - 1                 # O(1)

    while low <= high:                      # O(1) a pesar de ser un ciclo solo recorre la mitad o menos 
        mid = (low + high) // 2             # O(1)
        if my_list[mid] == target:          # O(1)
            return True
        elif my_list[mid] < target:         # O(1)
            low = mid + 1                   # O(1)
        else:
            high = mid - 1                  # O(1)

    return False

# Big-O final: O(log n) entre mas grande sea la lista mas se va a ir acortando

# - Preguntas:

# - ¿Cuál es la complejidad de cada algoritmo?

# linear_search = Big-O final: O(n) la busqueda depende de 'n'.
# binary_search = Big-O final: O(log n) entre mas grande sea la lista mas se va a ir acortando

# - ¿En qué condiciones conviene usar cada uno?
# linear_search: es util cuando la lista esta desordenada
# binary_search: funciona solo si la lista esta ordenada

# - ¿Qué pasa si la lista no está ordenada?
# binary_search no funcionaria porque podriamos saltarnos el target