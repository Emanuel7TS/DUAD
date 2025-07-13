"""
6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
    1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
    2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”
"""


def sort_string():
    
    entered_string = input("Enter text separated by hyphens: ")
    words_list = entered_string.split("-")
    words_list.sort()
    ordered_string = ""
    
    for i, word in enumerate(words_list):
        ordered_string += word
        if i < len(words_list) - 1:
            ordered_string += "-"
            
    return ordered_string

result = sort_string()
print(result)