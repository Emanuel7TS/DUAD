def read_songs(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        
        songs = [line.strip() for line in file]
    return songs


def save_sorted_songs(songs, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        for song in songs:
            file.write(song + '\n'


def sort_songs(input_path, output_path):
    songs = read_songs(input_path)
    songs.sort()  
    save_sorted_songs(songs, output_path)
    print(f"Canciones ordenadas guardadas en {output_path}")


input_file = 'C:/Users/Emanuel/Desktop/Stuff/Ejercicios_Lyfter/Python/manejo_de_archivos/playlist_spotify.txt'
output_file = 'C:/Users/Emanuel/Desktop/Stuff/Ejercicios_Lyfter/Python/manejo_de_archivos/playlist_sorted.txt'

sort_songs(input_file, output_file)

# Función / Método	Qué hace (en palabras sencillas)

# open()	Sirve para abrir un archivo. Le dices el nombre del archivo y el modo
#(leer, escribir, etc.). Si lo abres con 'r' es para leer, con 'w' para escribir.

# close()	Cierra el archivo cuando ya no lo vas a usar. Si usas with, se cierra solo.

# read()	Lee todo el contenido del archivo de un solo tirón (como si copiaras todo).

# readline()	Lee solo una línea del archivo (como si agarraras solo la primera línea).

# readlines()	Lee todas las líneas y te las devuelve en una lista (cada línea es un elemento de la lista).

# write()	Sirve para escribir texto en el archivo (por ejemplo, meter canciones nuevas).

# writelines()	Sirve para escribir varias líneas de una sola vez, usando una lista (cada item es una línea).

# seek()	Mueve el "cursor" dentro del archivo a una posición que le dices (como saltar a cierto punto).

# tell()	Te dice en qué posición está el cursor del archivo en ese momento (como saber dónde vas).

# truncate()	Corta el archivo desde donde le dices, borra el resto (como recortar).

# flush()	Obliga a que todo lo que se ha escrito en memoria se guarde en el archivo de una vez (sin esperar).

# fileno()	Devuelve un número especial que usa el sistema para referirse al archivo (no se usa mucho en cosas básicas).

# isatty()	Devuelve True si el archivo es un dispositivo interactivo (como el teclado). Normalmente sale False en archivos normales.

# readable()	Te dice si el archivo se puede leer (True/False).

# writable()	Te dice si el archivo se puede escribir (True/False).

# seekable()	Te dice si puedes mover el cursor adentro del archivo (True/False).




Ejercicios sobre CSV

"""
Cree un programa que me permita ingresar información
de n cantidad de videojuegos y los guarde en un archivo csv.
"""

import csv

def main():
    games = []
    running = True
    game_counter = 1

    while running:
        game = {
            'name': input(f"Enter the name of game #{game_counter}: "),
            'genre': input(f"Enter the genre of game #{game_counter}: "),
            'developer': input(f"Enter the developer of game #{game_counter}: "),
            'rating': input(f"Enter the rating of game #{game_counter}: ")
        }
        games.append(game)
        print("")
        add_game = int(input("To add another game, type [1]; to finish, type [0]: "))
        if add_game != 1:
            running = False
        game_counter += 1

    with open('video_games.csv', mode='w', encoding='utf-8', newline="") as file:
        fieldnames = ['name', 'genre', 'developer', 'rating']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(games)

if __name__ == "__main__":
    main()
    
    
    


import csv

def main():
    games = []
    running = True
    game_counter = 1

    while running:
        game = {
            'name': input(f"Enter the name of game #{game_counter}: "),
            'genre': input(f"Enter the genre of game #{game_counter}: "),
            'developer': input(f"Enter the developer of game #{game_counter}: "),
            'rating': input(f"Enter the rating of game #{game_counter}: ")
        }
        games.append(game)
        print("")
        add_game = int(input("To add another game, type [1]; to finish, type [0]: "))
        if add_game != 1:
            running = False
        game_counter += 1


    fieldnames = ['name', 'genre', 'developer', 'rating']
    with open('video_games.csv', mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        writer.writerows(games)   

if __name__ == "__main__":
    main()





import json

file = "pokemones.json"
initial = [
    {
        "name": {"english": "Pikachu"},
        "type": ["Electric"],
        "base": {
            "HP": 35,
            "Attack": 55,
            "Defense": 40,
            "Sp. Attack": 50,
            "Sp. Defense": 50,
            "Speed": 90
        }
    },
    {
        "name": {"english": "Charmander"},
        "type": ["Fire"],
        "base": {
            "HP": 39,
            "Attack": 52,
            "Defense": 43,
            "Sp. Attack": 60,
            "Sp. Defense": 50,
            "Speed": 65
        }
    },
    {
        "name": {"english": "Squirtle"},
        "type": ["Water"],
        "base": {
            "HP": 44,
            "Attack": 48,
            "Defense": 65,
            "Sp. Attack": 50,
            "Sp. Defense": 64,
            "Speed": 43
        }
    }
]

def load_pokemons():
    try:
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(initial, f, ensure_ascii=False, indent=4)
        return initial.copy()

def save_pokemons(list_):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(list_, f, ensure_ascii=False, indent=4)

def ask_pokemon():
    print("Enter the new Pokémon's data:")
    name = input(" - Name (English): ").strip().capitalize()
    types = input(" - Type(s), separated by commas: ").strip()
    types_list = [t.strip().capitalize() for t in types.split(",") if t.strip()]
    
    def ask_stat(key):
        value = input(f"   * {key}: ").strip()
        try:
            return int(value)
        except ValueError:
            print(f"⚠️ Invalid value for {key}, setting it to 0.")
            return 0
    
    base = {
        "HP": ask_stat("HP"),
        "Attack": ask_stat("Attack"),
        "Defense": ask_stat("Defense"),
        "Sp. Attack": ask_stat("Sp. Attack"),
        "Sp. Defense": ask_stat("Sp. Defense"),
        "Speed": ask_stat("Speed")
    }
    return {"name": {"english": name}, "type": types_list, "base": base}

def main():
    pokemons = load_pokemons()
    print(f"📂 {len(pokemons)} Pokémon(s) loaded.\n")
    new_pokemon = ask_pokemon()
    pokemons.append(new_pokemon)
    save_pokemons(pokemons)
    print(f"\n✅ Pokémon \"{new_pokemon['name']['english']}\" added. Now there are {len(pokemons)} Pokémon(s).")

if __name__ == "__main__":
    main()