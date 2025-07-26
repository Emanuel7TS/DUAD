import menu, actions

def main():
    students = []
    running = True
    menu.show_welcome_message()

    while running:
        menu.show_main_menu()
        selected_option = menu.get_user_option()

        if selected_option == 1:
            actions.add_student(students)
        elif selected_option == 2:
            actions.show_students_info(students)
        elif selected_option == 3:
            average = actions.get_average(students)
            actions.get_top_3_average(average) 
        elif selected_option == 4:
            print("Show overall average of all students")
        elif selected_option == 5:
            print("Export information to CSV")
        elif selected_option == 6:
            print("Import information from an existing CSV")
        elif selected_option == 7:
            print("Thanks for using this program!")
            break

if __name__ == "__main__":
    main()