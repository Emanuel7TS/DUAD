# Ejercicios de Diccionarios  ✔

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
