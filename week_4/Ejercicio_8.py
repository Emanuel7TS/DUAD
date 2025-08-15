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