"""
3. Cree un algoritmo que le pida un numero al usuario, y realice una suma de cada numero del 1
hasta ese número ingresado. Luego muestre el resultado de la suma.
"""

total = 0
user_number = int(input("Enter a number: "))

for i in range (user_number + 1):
    total += i

print(f"The total of that sum is {total}")