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