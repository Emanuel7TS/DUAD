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