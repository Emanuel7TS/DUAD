"""
5. Cree un programa que le pida al usuario 10 números, y al final le muestre
todos los números que ingresó, seguido del numero ingresado más alto.
"""

number_list = []
greatest = 0

for i in range(0, 10):
    number_entered = int(input(f"Type number {i+1}: "))
    number_list.append(number_entered)
    if number_list[i] > greatest:
        greatest = number_list[i]

print(number_list)
print(f"The greatest number is: {greatest}")