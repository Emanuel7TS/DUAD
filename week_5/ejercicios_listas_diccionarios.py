Ejercicios de Iterables y Listas  ✔

"""
1. Cree un programa que itere e imprima los valores de dos listas
del mismo tamaño al mismo tiempo.
"""

first_list = ["Hay", "en", "que", "iteracion", "indices", "muy"]
second_list = ["casos", "los", "la", "por", "es", "util"]

for index in range (0, len(first_list)):
    print(first_list[index])
    print(second_list[index])
 
 
"""
 2. Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.
"""

my_string  = "Fullstack Developer"

for i in range(len(my_string) - 1, -1, -1):
    print(my_string[i])
    
""" 
3. Cree un programa que intercambie el primer y ultimo elemento de una lista.
Debe funcionar con listas de cualquier tamaño.
"""
words_list = []
written_word = ""

words_amount = int(input("How many words do you want to save? "))

for i in range(words_amount):
    written_word = input(f"Type word number {i + 1}: ")
    words_list.append(written_word)

first_word = words_list[0]
last_word = words_list[-1]

words_list[0] = last_word
words_list[-1] = first_word

print(words_list)


"""
4. Cree un programa que elimine todos los números impares de una lista.
"""

size_list =  int(input("Enter the size of list: "))
number_list = []
counter = 1
for i in range (0,size_list):
    number_list.append(counter)
    counter += 1
    for i in range ( 0, len(number_list)):
        if number_list[i] % 2 != 0:
            number_list.pop(i)


print(number_list)

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


Ejercicios de Diccionarios  ✔

"""
1. Cree un diccionario que guarde la siguiente información sobre un hotel:
    - `nombre`
    - `numero_de_estrellas`
    - `habitaciones`
- El value del key de `habitaciones` debe ser una lista, y cada habitación debe tener la siguiente información:
    - `numero`
    - `piso`
    - `precio_por_noche`
"""

dictionary_hotel = {
    "name": "Nate's Hotel",
    "star_rating": 5,
    "rooms": [
        {
            "number": 3070,
            "floor": 4,
            "price_per_night": 450.0
        },
        {
            "number": 4080,
            "floor": 4,
            "price_per_night": 700.0
        },
        {
            "number": 5090,
            "floor": 5,
            "price_per_night": 1200.0
        }
    ]
}

print(dictionary_hotel)





"""
2. Cree un programa que cree un diccionario usando dos listas del mismo tamaño,
usando una para sus keys, y la otra para sus values.
"""

pc_components = [
    "Processor",
    "RAM",
    "Storage",
    "Graphics Card",
    "Power Supply",
    "Motherboard"
]

pc_specs = [
    "Ryzen 7 5700X",
    "TRIDENT Z ROYAL DDR5",
    "KINGSTON NVME M.2 1TB",
    "NVIDIA 4090",
    "NZXT 850W GOLD",
    "ASROCK B550 STEEL LEGEND"
]

computer_build = {}

for i in range(len(pc_components)):
    computer_build[pc_components[i]] = pc_specs[i]

print(computer_build)





"""
3. Cree un programa que use una lista para eliminar keys de un diccionario.
"""

user_info = { 
"name": "Emanuel",
"Last name": "Hasbun",
"number" : "5012-4740",
"email": "EmanuelH@lyfter.DEV",
"position": "Student",
"status" : "available",
}

kill_list = ["number","email"]
data_deleted_list = []

for key in kill_list:
    if key in user_info:
        deleted_value = user_info.pop(key)  
        data_deleted_list.append((key, deleted_value))


print (user_info)
print("")
print(data_deleted_list)





Ejercicios Extra sobre Diccionarios  ✔



"""
1. Dada una lista de ventas con la siguiente información:
`date`
`customer_email`
`items`
Y cada item teniendo la siguiente información:
`name`
`upc`
`unit_price`
Cree un diccionario que guarde el total de ventas de cada UPC
"""

sales_list = [
    {
        "date": "2025-06-24",
        "customer_email": "emanuel@compra.com",
        "items": [
            {"name": "Ryzen 7 5700X", "upc": "1111", "unit_price": 250.0},
            {"name": "Kingston NVMe 1TB", "upc": "2222", "unit_price": 90.0}
        ]
    },
    {
        "date": "2025-06-24",
        "customer_email": "alek@compra.com",
        "items": [
            {"name": "Ryzen 7 5700X", "upc": "1111", "unit_price": 250.0},
            {"name": "ASUS B550M", "upc": "3333", "unit_price": 130.0}
        ]
    },
    {
        "date": "2025-06-24",
        "customer_email": "jeancarlo@compra.com",
        "items": [
            {"name": "NZXT 850W", "upc": "4444", "unit_price": 120.0},
            {"name": "Kingston NVMe 1TB", "upc": "2222", "unit_price": 90.0}
        ]
    }
]


total_sales_by_upc = {}

for sale in sales_list:
    for item in sale["items"]:
        upc = item["upc"]
        price = item["unit_price"]
        if upc in total_sales_by_upc:
            total_sales_by_upc[upc] += price
        else:
            total_sales_by_upc[upc] = price


for upc, total in total_sales_by_upc.items():
    print(f"UPC: {upc} → Total vendido: ${total:.2f}")

    