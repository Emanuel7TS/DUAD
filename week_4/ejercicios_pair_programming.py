
"""
Dadas las horas trabajadas de una persona y su tarifa
por hora, calcular su salario minimo
"""
hours_worked = 0
hourly_rate = 0

hours_worked = int(input("Enter your hours worked: "))
hourly_rate = int(input("Enter your hourly rate: "))
salary = hours_worked * hourly_rate

print(f"Your salary is: {salary}")



2 Dado el nombre y apellido de un empleado, y el dominio .com
de una empresa, genere su
email usando el formato
<nombre>.<apellido>@<dominio_de_empresa>.com.


name = ""
last_name = ""
domain_name = ""

name = str(input("type your name: "))
last_name = str(input("type your last name: "))
domain_name = str(input("type your company's domain: "))

print("Your new email is " + name + last_name + "@" + domain_name + ".com")





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





"""
# Ejercicio 2
Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre
 si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.
"""

user_name =str(input("Type your name: "))
user_last_name =str(input("Type your last name: "))
user_age =int(input("Type your age: "))
user_category_list = ["Baby","Child","Pre-adolescent","Adolescent","Young","Adult","Older"]

if (user_age >0 and user_age <= 2):
    print("Hello", user_name, user_last_name + ", you are", user_age, 
      "years old, so you belong to the", user_category_list[0], "category.")
    
elif (user_age >=3 and user_age <= 9):
    print("Hello", user_name, user_last_name + ", you are", user_age, 
      "years old, so you belong to the", user_category_list[1], "category.")
    
elif (user_age >=10 and user_age <= 12):
    print("Hello", user_name, user_last_name + ", you are", user_age, 
      "years old, so you belong to the", user_category_list[2], "category.") 
    
elif (user_age >=13 and user_age <= 17):
    print("Hello", user_name, user_last_name + ", you are", user_age, 
      "years old, so you belong to the", user_category_list[3], "category.") 

elif (user_age >=18 and user_age <= 25):
    print("Hello", user_name, user_last_name + ", you are", user_age, 
      "years old, so you belong to the", user_category_list[4], "category.") 

elif (user_age >=26 and user_age <= 64):
    print("Hello", user_name, user_last_name + ", you are", user_age, 
      "years old, so you belong to the", user_category_list[5], "category.") 
    
else:
    print("Hello", user_name, user_last_name + ", you are", user_age, 
      "years old, so you belong to the", user_category_list[6], "category.") 





"""
    #Ejercicio 3 
    Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse
    hasta que el usuario adivine el numero.
"""

import random

random_number = random.randint(1,10)
User_number = int(input("Type a number to guess: "))

while User_number != random_number:
    print("*** Wrong number ***")
    User_number = int(input("Try another one: "))

print(f"Congrats!! You win {random_number} is the number.")





"""
    #Ejercicio 4
    Cree un programa que le pida tres números al usuario y muestre el mayor.
"""

option1 = int(input("Type first number: "))
option2 = int(input("Type first number: "))
option3 = int(input("Type first number: "))

if option1 >= option2 and option1 >= option3:
    greatest = option1
elif option2 >= option1 and option2 >= option3:
    greatest = option2
else:
    greatest = option3

print(f"The greatest value is: {greatest}")





"""
5. Dada `n` cantidad de notas de un estudiante, calcular:
    1. Cuantas notas tiene aprobadas (mayor a 70).
    2. Cuantas notas tiene desaprobadas (menor a 70).
    3. El promedio de todas.
    4. El promedio de las aprobadas.
    5. El promedio de las desaprobadas.
"""

print("***** Grades calculator *****" )
grades_amount = int(input("Type how many grades you want to calculate: "))

count_passing_grades = 0
count_failing_grades = 0
overall_average = 0
average_passing_grades = 0
average_failing_grades = 0
sum_of_passing_grades = 0
sum_of_failing_grades = 0

for i in range(1, grades_amount + 1):
    grade = float(input(f"Type grade number {i}: "))

    while grade <= 0 or grade > 100:
        print("You must enter a number between 1 and 100.")
        grade = float(input(f"Type grade number {i} again: "))

    if grade >= 70:
        count_passing_grades += 1
        sum_of_passing_grades += grade
    else:
        count_failing_grades += 1
        sum_of_failing_grades += grade


if count_passing_grades > 0:
    average_passing_grades = sum_of_passing_grades / count_passing_grades
else:
    average_passing_grades = 0

if count_failing_grades > 0:
    average_failing_grades = sum_of_failing_grades / count_failing_grades
else:
    average_failing_grades = 0

overall_average = (sum_of_passing_grades + sum_of_failing_grades) / grades_amount


print("\n------------- Summary of grades -------------")
print("")
print(f"Count passing grades: {count_passing_grades}")
print(f"Count failing grades: {count_failing_grades}\n")
print(f"Average of passing grades: {average_passing_grades:.2f}")
print(f"Average of failing grades: {average_failing_grades:.2f}")
print(f"Overall average: {overall_average:.2f}")





# Ejercicios Extra (Pseudocódigos y diagramas en python)

# Ejercicios (Pseudocódigo)

"""
1. Cree un pseudocódigo que le pida un `precio de producto
al usuario, calcule su descuento y muestre el precio final tomando en cuenta que:
    1. Si el precio es menor a 100, el descuento es del 2%.
    2. Si el precio es mayor o igual a 100, el descuento es del 10%.
"""

price = float(input("Enter the product price: "))
print("")

if price < 100:
    discount = 0.02
else:
     discount = 0.10

discount = price * discount
total = price - discount

print(f"Original price: ${price:.2f}")
print("")
print(f"Final price after discount: ${total:.2f}")





"""
2- Cree un pseudocódigo que le pida un tiempo en segundos al usuario y calcule si es menor o mayor a 10 minutos.
Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos. Si es mayor, muestre “Mayor”.
Si es exactamente igual, muestre Igual.

"""

seconds_entered = int(input("Enter the number of seconds: "))
print()

if seconds_entered > 600:
    seconds_over = seconds_entered - 600
    print(f"You exceeded 10 minutes by {seconds_over} seconds.")
else:
    seconds_needed = 600 - seconds_entered
    print(f"You need {seconds_needed} more seconds to reach 10 minutes.")
    
    
    
    
    
"""
3. Cree un algoritmo que le pida un numero al usuario, y realice una suma de cada numero del 1
hasta ese número ingresado. Luego muestre el resultado de la suma.

"""

total = 0
user_number = int(input("Enter a number: "))

for i in range (user_number + 1):
    total += i

print(f"The total of that sum is {total}")





# Ejercicios Extra (Pseudocódigo)

"""
1- Cree un algoritmo que le pida 2 números al usuario, los guarde en dos variables distintas
(primero y segundo) y los ordene de menor a mayor en dichas variables.
"""


first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))


print("\nNumbers in ascending order:")

if first_number <= second_number:
    print(first_number)
    print(second_number)
else:
    print(second_number)
    print(first_number)





"""
2- Cree un algoritmo que le pida al usuario una velocidad en km/h y la convierta a m/s.
Recuerda que 1 km == 1000m y 1 hora == 60 minutos * 60 segundos.
"""

total_km = int(input("Type a km/h number: "))
meters_per_second = (total_km / 3.6)

print("")
print(f"The final convertion is: {meters_per_second:.2f}")





"""
3- Cree un algoritmo que le pregunte al usuario por el sexo de 6 personas,
ingresando 1 si es mujer o 2 si es hombre, y muestre al final el porcentaje de mujeres y hombres.
"""

student_gender = 0
male_count = 0
female_count = 0
average_male = 0.0
average_female = 0.0
counter = 0

print("          Average calculator\n\nType [1] to insert a female or [2] for male.")

for i in range(6):
    student_gender = int(input("Type a number [1] or [2]: "))
    while student_gender not in (1, 2):
        print("Wrong number, please type 1 or 2")
        student_gender = int(input("Type a number [1] or [2]: "))
    if student_gender == 1:
        female_count += 1
        counter += 1
    else:
        male_count += 1
        counter += 1

if counter > 0:
    average_female = (female_count / counter) * 100
    average_male   = (male_count   / counter) * 100

print(f"\nThe female average is: {average_female:.1f} %")
print(f"The male average is:   {average_male:.1f} %")

# Ejercicios diagramas de flujo

"""
 1- (todo el bloque de pseudocodigo anteriormente mostrado
"""

"""
2- Cree un diagrama de flujo que tenga un numero secreto del 1 al 10, y le pida al usuario
adivinar ese número. El algoritmo no debe terminar hasta que el usuario adivine el numero.

"""

import random

secret_number = random.randint(1, 10)
user_guess = 0

print("     Guess the Secret Number\n")
print("A secret number between 1 and 10 has been chosen.")
print("Keep guessing until you get it right!\n")

while user_guess != secret_number:
    user_guess = int(input("Type a number between 1 and 10: "))
    while user_guess < 1 or user_guess > 10:
        print("Wrong input, please type a number from 1 to 10")
        user_guess = int(input("Type a number between 1 and 10: "))
    if user_guess != secret_number:
        print("*** Wrong number ***\n")

print(f"\nCongrats!! You win, {secret_number} is the number.")





"""
3- Cree un diagrama de flujo que pida 3 números al usuario. Si uno de esos números
es 30, o si los 3 sumados dan 30, mostrar “Correcto”. Sino, mostrar “incorrecto”.

"""

number1 = int(input("Type the first number: "))
number2 = int(input("Type the second number: "))
number3 = int(input("Type the third number: "))

if number1 == 30 or number2 == 30 or number3 == 30 or (number1 + number2 + number3) == 30:
    print("*Correct*")
else:
    print("*Incorrect*")



# Ejercicios diagramas de flujo

"""
1- Cree un diagrama de flujo que le pida 5 números al usuario y muestre el mayor.

"""

max_number = int(input("Type number #1: "))

for i in range(1, 5):
    number = int(input(f"Type number #{i+1}: "))
    if number > max_number:
        max_number = number

print(f"The greatest number is: {max_number}")


"""
2- Cree un diagrama de flujo que le pida un numero al usuario y muestre “Fizz”
si es divisible entre 3, “Buzz” si es divisible entre 5, y
“FizzBuzz” si es divisible entre ambos.
"""

number = int(input("Type a number: "))

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(f"The number {number} is not divisible by 3 or 5.")
    

"""
3- Cree un diagrama de flujo que le pida 100 números al usuario y muestre la suma de todos.
"""

total = 0
for i in range(100):
    number = int(input(f"Type number #{i+1}: "))
    total += number

print(f"The total sum of all numbers is: {total}")

"""
4- Cree un diagrama de flujo que le pida 100 números al usuario y muestre el mayor de todos.
"""

max_number = int(input("Type number #1: "))

for i in range(1, 100):
    number = int(input(f"Type number #{i+1}: "))
    if number > max_number:
        max_number = number

print(f"The greatest number among the 100 entered is: {max_number}")


               # Brain-damage :(

               