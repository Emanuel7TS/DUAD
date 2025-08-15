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