# menu functions

def show_welcome_message():
    welcome_message = print("Welcome to SIS\n\n" 
    "Student Information System (SIS)\n\n"
    "Note: This system allows you to manage students and their grades.\n"
    "It will also let you calculate their averages and offers other tools.\n\n")


def show_main_menu():
    menu_message = print(
        "----------- Main Menu -----------\n",
        "Please select one of the following options:\n\n"
        "1. Add students\n"
        "2. Show student's information\n"
        "3. Show top 3 students by average\n"
        "4. Show overall average of all students\n"
        "5. Export information to CSV\n"
        "6. Import information from an existing CSV\n"
        "7. Exit the program\n"
    )


def get_user_option():

        running = True
        while running:
            try:
                selected_option = int(input("Select an option from the menu: "))

            except ValueError:
                print("\nError: Please enter a number between 1 and 6.\n")
                continue

            if 1 <= selected_option <= 7:

                return selected_option

            else:
                print("Invalid choice. Please enter a number between 1 and 7.")