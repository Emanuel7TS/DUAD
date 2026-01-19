my_test_list = [18, -11, 68, 6, 32, 53, -2]

def bubble_sort_backwards(number_list):
    for lap in range(len(number_list)-1):
        for number in range(len(number_list) - 1, lap, -1):
            current = number_list[number-1]
            if number_list[number] < number_list[number-1]:
                number_list[number-1] = number_list[number]
                number_list[number] = current

    return number_list

new_list = bubble_sort_backwards(my_test_list)

print(new_list)