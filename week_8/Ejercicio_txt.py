def read_songs(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        
        songs = [line.strip() for line in file]
    return songs


def save_sorted_songs(songs, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        for song in songs:
            file.write(song + '\n')


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