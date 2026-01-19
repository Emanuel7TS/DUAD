my_test_list = [18, -11, 68, 6, 32, 53, -2]

def bubble_sort(data):
    for lap in range(len(data) - 1):
        for number in range(len(data) - 1 - lap):
            current = data[number + 1]
            if data[number] > data[number + 1]:
                data[number + 1] = data[number]
                data[number] = current
    return data


sorted_list = bubble_sort(my_test_list)

print(sorted_list)