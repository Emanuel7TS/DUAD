"""
2- Cree un algoritmo que le pida al usuario una velocidad en km/h y la convierta a m/s.
Recuerda que 1 km == 1000m y 1 hora == 60 minutos * 60 segundos.
"""

total_km = int(input("Type a km/h number: "))
meters_per_second = (total_km / 3.6)

print("")
print(f"The final convertion is: {meters_per_second:.2f}")