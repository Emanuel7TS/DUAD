"""
4. Cree una función que le de la vuelta a un string y lo retorne.
    1. Esto ya lo hicimos en iterables.
    2. “Hola mundo” → “odnum aloH”
    """

def string_reverse():
    reverse_word  = str(input("Enter a word to see in reverse: "))
    for i in range(len(reverse_word) - 1, -1, -1):
        print(reverse_word[i])
    return reverse_word

string_reverse()