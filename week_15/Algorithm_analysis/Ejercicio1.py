# Big O Notation
# O(n) = lineal, depende de n
# O(1) = constante: no depende de n
# O(n²): cuadrático → depende de n²
# O(n³): cúbico → depende de n³
# O(log n): logarítmico → depende de log(n)


my_test_list = [18, -11, 68, 6, 32, 53, -2]

def bubble_sort(data):
    for lap in range(len(data) - 1):                    #O(n)
        for number in range(len(data) - 1 - lap):       #O(n) = O(n²)
            current = data[number + 1]                  #O(1)
            if data[number] > data[number + 1]:         #O(1)
                data[number + 1] = data[number]         #O(1)
                data[number] = current                  #O(1)
    return data                                         #O(1)


sorted_list = bubble_sort(my_test_list)

print(sorted_list)

# Big-O final: O(n²), debido a dos bucles anidados que dependen de n.