"""
4. Cree un programa que elimine todos los números impares de una lista.
"""

size_list =  int(input("Enter the size of list: "))
number_list = []
counter = 1
for i in range (0,size_list):
    number_list.append(counter)
    counter += 1
    for i in range ( 0, len(number_list)):
        if number_list[i] % 2 != 0:
            number_list.pop(i)


print(number_list)