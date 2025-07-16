"""
5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”
"""

def letter_case_counter():
    upper_counter = 0
    lower_counter = 0

    text_entered = input("Enter text: ")
    

    for char in text_entered:
        if char.isupper():        
            upper_counter += 1
        elif char.islower():      
            lower_counter += 1

    print(
        f"There are {upper_counter} uppercase letters and "
        f"{lower_counter} lowercase letters in \"{text_entered}\"."
    )

    return upper_counter, lower_counter

letter_case_counter()