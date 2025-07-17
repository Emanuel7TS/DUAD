import menu

def main():

    students = []
    running = True

    menu.show_welcome_message()
    menu.show_main_menu()
    menu.get_user_option()



    while running:
        
        selected_option = menu.get_user_option()

        if selected_option == 1:
            print("add student")
        elif selected_option == 2:
            print("Show student's information")
        elif selected_option == 3:
            print("Show top 3 students by average")
        elif selected_option == 4:
            print("Show overall average of all students")
        elif selected_option == 5:
            print("Export information to CSV")
        elif selected_option == 6:
            print("Import information from an existing CSV")
        elif selected_option == 7:
            print("Thanks for using this program!")
            print("Exit the program")
            break
            


    if __name__ == "__main__":
        main()