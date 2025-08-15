"""
1- Cree una calculadora por linea de comando. Esta debe de tener un número actual,
y un menú para decidir qué operación hacer con otro número:
1. Suma
2. Resta
3. Multiplicación
4. División
5. Borrar resultado
Al seleccionar una opción, el usuario debe ingresar el nuevo número a
sumar, restar, multiplicar, o dividir por el actual.
El resultado debe pasar a ser el nuevo numero actual.
Debe de mostrar mensajes de error si el usuario selecciona una opción invalida,
o si ingresa un número invalido a la hora de hacer la operación.
"""
def show_menu(total):
    menu = (
        "\nMenu\n\n"  
        "[1] to add\n"
        "[2] to subtract\n"
        "[3] to multiply\n"
        "[4] to divide\n"
        "[5] to clear total\n"
        "[6] to exit\n\n"
        f"Current total:\n{total}\n"  
    )
    print(menu)

def add(total):
    try:
        print(f"\nCurrent total:\n{total}\n")  
        user_number = float(input("Enter a number to add: "))
        total += user_number
    except ValueError:
        print("\nError: Please enter a valid number.\n")
    return total

def subtract(total):
    try:
        print(f"\nCurrent total:\n{total}\n")
        user_number = float(input("Enter a number to subtract: "))
        total -= user_number
    except ValueError:
        print("\nError: Please enter a valid number.\n")
    return total

def multiply(total):
    try:
        print(f"\nCurrent total:\n{total}\n")
        user_number = float(input("Enter a number to multiply: "))
        total *= user_number
    except ValueError:
        print("\nError: Please enter a valid number.\n")
    return total

def divide(total):
    try:
        print(f"\nCurrent total:\n{total}\n")
        user_number = float(input("Enter a number to divide: "))
        total /= user_number
    except ValueError:
        print("\nError: Please enter a valid number.\n")
    except ZeroDivisionError:
        print("\nError: Cannot divide by zero.\n")
    return total

def clear_total():
    return 0.0

def main():
    total = 0.0
    running = True

    while running:
        print("\n~~~~~~~~~~~~~ NASA Calculator ~~~~~~~~~~~~~\n")
        show_menu(total)
        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("\nError: please enter a number between 1 and 6.\n")
            continue

        if choice == 1:
            total = add(total)
        elif choice == 2:
            total = subtract(total)
        elif choice == 3:
            total = multiply(total)
        elif choice == 4:
            total = divide(total)
        elif choice == 5:
            total = clear_total()
            print(f"\nTotal cleared. Current total:\n{total}\n")
        elif choice == 6:
            running = False
            print("\nThank you so much for using our humble calculator\n")
        else:
            print("\nInvalid option, please choose 1–6.\n")

if __name__ == "__main__":
    main()