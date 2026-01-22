def bubble_sort(data):
    if len(data) == 0:
        raise ValueError("List cannot be empty")

    for item in data:
        if not isinstance(item, (int, float)):
            raise TypeError("All parameters must be numbers")

    for lap in range(len(data) - 1):
        for number in range(len(data) - 1 - lap):
            if data[number] > data[number + 1]:
                data[number], data[number + 1] = data[number + 1], data[number]

    return data

my_test_list = [18, -11, 68, 6, 32, 53, -2]
my_test_list_2 = [18, -11, "hola"]


try:
    sorted_list = bubble_sort(my_test_list)
    print("Sorted list:", sorted_list)

except TypeError as e:
    print("Type error:", e)

except ValueError as e:
    print("Value error:", e)

print("----")

try:
    sorted_list_2 = bubble_sort(my_test_list_2)
    print("Sorted list:", sorted_list_2)

except TypeError as e:
    print("Type error:", e)

except ValueError as e:
    print("Value error:", e)