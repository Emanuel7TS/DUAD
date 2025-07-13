"""
1. Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.

1. string + string → ?
2. string + int → ?
3. int + string → ?
4. list + list → ?
5. string + list → ?
6. float + int → ?
7. bool + bool → ?
"""
# -1 string + string
first_name = "Emanuel"
last_name = "Hasbun"
print(first_name+ " " +last_name)
print("")


# -2
age = 25
print(f"{first_name} {last_name}, your age is: {age}")
print("")


#3. int + string
print(str(age) + " is your age: ")
print("")


# 4. list + list
my_list1 = ["Emanuel","Hasbun",25]
my_list2 = ["is","practicing",7,"exercises"]
print(my_list1 + my_list2)
print("")


# 5. string + list
print(first_name + str(my_list2))
print("")


# 6. float + int
number1 = 12.5
number2 = 18
result = number1 + number2
print(number1 + number2)
print(result)
print("")


# 7. bool + bool
car_working = True
without_gasoline = False
ride = car_working and without_gasoline
print("is your car working? ")
print(ride)