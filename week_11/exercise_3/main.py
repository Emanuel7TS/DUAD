import menu, actions, data

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
            general_average = actions.get_average(students)
            actions.get_general_average(general_average)
        elif selected_option == 5:
            data.export_students_info(students)
        elif selected_option == 6:
            data.import_valid_csv(students)
        elif selected_option == 7:
            print("Thank you for using the Student Information System. Goodbye!")
            break

if __name__ == "__main__":
    main()
