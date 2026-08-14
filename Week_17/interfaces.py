import FreeSimpleGUI as sg
import main
import persistence




def show_login_window():

    layout = [
        [sg.Text("Enter your name to start:")],
        [sg.Input(key="name")],
        [sg.Button("Start"), sg.Button("Clear")],
    ]

    window = sg.Window("Personal Finance Tracker", layout)

    while True:

        event, values = window.read()

        if event == sg.WIN_CLOSED:
            window.close()
            return None

        if event == "Clear":
            window["name"].update("")

        if event == "Start":
            name = values["name"]
            if name == "":
                sg.popup("You must write a name")
                continue

            window.close()
            return name





def show_validation_window(name):

    layout = [
        [sg.Text(f"Do you want to continue as {name}?")],
        [sg.Button("Yes"), sg.Button("No")]
    ]

    window = sg.Window("Validation", layout)

    while True:

        event, values = window.read()

        if event in (sg.WIN_CLOSED, "No"):
            window.close()
            return False

        if event == "Yes":
            window.close()
            return True





def show_welcome_window(name):

    layout = [
        [sg.Text(
            f"Welcome {name} to PETRAFI Personal Finance System\n\n"
            "This system will help you manage your finances\n"
            "in a clear and organized way through a structured\n"
            "layer-based system, where you will be able to view\n"
            "all your monthly transactions and compare\n"
            "how your income and expenses move over time."
        )],

        [sg.Button("Continue")]
    ]

    window = sg.Window("Welcome", layout)

    while True:

        event, values = window.read()

        if event == sg.WIN_CLOSED:
            window.close()
            return False

        if event == "Continue":
            window.close()
            return True





def main_menu(fm, name):

    table_data = movements_table(fm)

    layout = [
        [sg.Text("PETRAFI")],
        
        [sg.Table(
            values = table_data,
            headings=["Name", "Value", "Type", "Category"],
            key="table")],


        [sg.Button("Add Category"), sg.Button("(i)",key="category_help")],

        [sg.Button("Add Movement"), sg.Button("(i)",key="movement_help")],

        [sg.Button("Show Balance"), sg.Button("(i)",key="balance_help")],

        [sg.Button("Save Data"), sg.Button("(i)",key="save_help")],

        [sg.Button("Load Data"), sg.Button("(i)",key="load_help")],

        [sg.Button("Exit")],]

    window = sg.Window("Menu", layout, enable_close_attempted_event=True)

    while True:

        event, values = window.read()

        if event == "Add Category":
            try:

                add_category(fm)

            except ValueError as e:
                sg.popup_error(str(e))

        if event == "category_help":
            sg.popup("Categories help organize your movements such as food, transport, salary or bills.",title="Category Help")

        if event == "Add Movement":

            if not fm.categories:
                sg.popup_error("You must create at least one category first.")
                continue

            movement = add_movement(fm)
            if movement:
                refresh_table(window, fm)

        if event == "movement_help":
            sg.popup("Create a new income or expense movement and assign it to a category.",title="Category Help")

        if event == "Show Balance":
            show_balance(fm)

        if event == "balance_help":
            sg.popup("Displays the difference between your total income and total expenses.",title="Category Help")

        if event == "Save Data":
            try:
                categories = fm.categories
                persistence.store_categories(categories)
                sg.popup("Category data was successfully exported to a CSV file.")
            except ValueError as e:
                sg.popup_error(str(e))
            try:
                movements = fm.movements
                persistence.store_movements(movements)
                sg.popup("Movement data was successfully exported to a CSV file.")
            except ValueError as e:
                sg.popup_error(str(e))

        if event == "save_help":
            sg.popup("Stores your current categories and movements into CSV files.",title="Category Help")
        
        if event == "Load Data":
                if fm.data_loaded == False:
                    try:
                        persistence.load_categories(fm)
                        sg.popup("Category data was successfully loaded.")
                    except FileNotFoundError as e:
                        sg.popup(str(e))
                    try:
                        persistence.load_movements(fm)
                        sg.popup("Movement data was successfully loaded.")
                    except FileNotFoundError as e:
                        sg.popup(str(e))
                    fm.data_loaded = True
                else:
                    sg.popup_error("Data has already been loaded.")

                refresh_table(window, fm)

        if event == "load_help":
            sg.popup("Loads previously saved financial data from your CSV files.",title="Category Help")


        if event == "Exit" or event is None:
            answer = confirm_exit()
            if answer == "Yes":
                try:
                    categories = fm.categories
                    persistence.store_categories(categories)
                    sg.popup("Category data was successfully exported to a CSV file.")
                except ValueError as e:
                    sg.popup_error(str(e))
                try:
                    movements = fm.movements
                    persistence.store_movements(movements)
                    sg.popup("Movement data was successfully exported to a CSV file.")
                except ValueError as e:
                    sg.popup_error(str(e))
                break

            if answer == "No":
                break
                
            if answer == "Cancel":
                continue





def movements_table(fm):

    data_table = []

    for movement in fm.movements:

        name = movement.name.title()
        movement_value = movement.value
        movement_type = movement.type.title()
        category = movement.category.name.title()
        movement_line = [name,movement_value,movement_type,category]

        data_table.append(movement_line)

    return data_table





def refresh_table(window, fm):
    window["table"].update(
        values=movements_table(fm))





def add_category(fm):

    layout = [
        [sg.Text(f"type category's name:?")],
        [sg.Input(key = "category_name")],\
        [sg.Button("Create"), sg.Button("Cancel")]
        ]

    window = sg.Window("Add Category", layout)

    while True:
        event, values = window.read()

        if event == "Create":
            try:
                name = values["category_name"]
                confirmation = sg.popup_ok_cancel(f"Do you want to save this category with this name: {name}")
    
                if confirmation == "OK":
                    category = fm.add_category(name)
                    sg.popup_ok("Category added successfully")

                    window.close()
                    return category
            except ValueError as e:
                sg.popup_error(str(e))

        if event == "Cancel":
            window.close()
            return None
        
        if event == sg.WIN_CLOSED:
            window.close()
            return None





def add_movement(fm):

    display_categories = [
    category.title()
    for category in fm.categories.keys()]

    display_types = [
    movement_type.title()
    for movement_type in fm.valid_types]
    layout = [

        [sg.Text("Movement name:")],
        [sg.Input(key="movement_name")],

        [sg.Text("Value:")],
        [sg.Input(key="movement_value")],

        [sg.Text("Type:")],
        [sg.Combo(
            values= display_types,
            key="movement_type"
        )],

        [sg.Text("Category:")],
        [sg.Combo(
            values=display_categories,
            key="movement_category")],

        [sg.Button("Create"), sg.Button("Cancel")]]
    
    window = sg.Window("Add Movement", layout)

    while True:
        event, values = window.read()

        if event == "Create":

            if not all([
                values["movement_name"],
                values["movement_value"],
                values["movement_type"],
                values["movement_category"]
            ]):
                sg.popup_error("All fields are required.")
                continue

            try:
                movement_name = values["movement_name"]
                movement_value = values["movement_value"]
                movement_type = values["movement_type"].lower()
                movement_category = values["movement_category"].lower()

                movement_category_object = fm.categories[movement_category]

                movement = fm.add_movement(
                    movement_name,
                    movement_value,
                    movement_type,
                    movement_category_object)

                sg.popup_ok("Movement added successfully")

                window.close()
                return movement

            except ValueError as e:
                sg.popup_error(str(e))

        if event == "Cancel":
            window.close()
            return None

        if event == sg.WIN_CLOSED:
            window.close()
            return None




def show_balance(fm):
    income_total = fm.get_total_by_type("income")
    expense_total = fm.get_total_by_type("expense")
    total = fm.get_balance()
    layout = [
        [sg.Text(f"Total Income: {income_total}")],
        [sg.Text(f"Total Expense: {expense_total}")],
        [sg.Text(f"Net Balance: {total}")],
        [sg.Button("Close")]
    ]
    window = sg.Window("Show Balance", layout)

    while True:

        event, values = window.read()
        if event == "Close":
            window.close()
            return None
        
        if event == sg.WIN_CLOSED:
            window.close()
            return None





def confirm_exit():
    layout = [
        [sg.Text("Do you want to save before exiting the program?")],
        [sg.Button("Yes"), sg.Button("No"), sg.Button("Cancel")]
    ]

    window = sg.Window("Save data", layout)

    while True:
        event, values = window.read()

        if event == "Yes":
            window.close()
            return "Yes"

        if event == "No":
            window.close()
            return "No"

        if event == "Cancel":
            window.close()
            return "Cancel"
        
        if event is None:
            window.close()
            return "Cancel" 