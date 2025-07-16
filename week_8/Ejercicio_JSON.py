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