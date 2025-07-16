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