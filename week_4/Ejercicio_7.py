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