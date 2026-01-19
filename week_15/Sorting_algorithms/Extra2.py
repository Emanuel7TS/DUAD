my_test_list = [18, -11, 68, 6, 32, 53, -2, 1]

def bubble_sort(data):
    iterations = 0
    swaps = 0

    n = len(data)

    for lap in range(n - 1):
        iterations += 1
        for number in range(n - 1 - lap):
            if data[number] > data[number + 1]:
                data[number], data[number + 1] = data[number + 1], data[number]
                swaps += 1

    return data, iterations, swaps

sorted_list, iterations, swaps = bubble_sort(my_test_list)

print(f"Lista ordenada: {sorted_list}")
print(f"Iteraciones: {iterations}")
print(f"Intercambios: {swaps}")