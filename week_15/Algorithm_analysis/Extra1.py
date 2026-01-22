# Big O Notation
# O(n) = lineal, depende de n
# O(1) = constante: no depende de n
# O(n²): cuadrático → depende de n²
# O(n³): cúbico → depende de n³
# O(log n): logarítmico → depende de log(n)



# Versión 1:
def manual_add(number):
    result = 0                          # O(1)
    for i in range(1, number + 1):      # O(n)
        result += i                     # O(1)
    return result

# Big-O final: O(n), depende del tamaño del number



# Versión 2:
def add_formula(number):
    return number * (number + 1) //  2   # O(1)

# Big-O final: O(1), no importa el tamaño del numero solo hace un paso.



# - Preguntas:

# - ¿Cuál es la complejidad de cada versión?

# Versión 1:    Big-O final: O(n), depende del tamaño del number.

# Versión 2:    Big-O final: O(1), no importa el tamaño del numero solo hace un paso.


# - ¿Qué versión usaría si `number = 1 000 000 000`? ¿Por qué?

# Versión 2:    Big-O final: O(1), no importa el tamaño del numero solo hace un paso.