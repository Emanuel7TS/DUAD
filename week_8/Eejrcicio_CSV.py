# Ejercicios sobre CSV

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