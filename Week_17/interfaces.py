import FreeSimpleGUI as sg


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


def main_menu():

    layout = [
        [sg.Text("PETRAFI")],

        [sg.Button("Add Category"), sg.Button("?")],

        [sg.Button("Add Movement"), sg.Button("?")],

        [sg.Button("Show Balance"), sg.Button("?")],

        [sg.Button("Save Data"), sg.Button("?")],

        [sg.Button("Load Data"), sg.Button("?")],

        [sg.Button("Exit")],]

    window = sg.Window("Welcome", layout)

    while True:

        event, values = window.read()

