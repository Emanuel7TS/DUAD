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