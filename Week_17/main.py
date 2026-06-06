import FreeSimpleGUI as sg
import interfaces
import models

def main():

    while True:
        name = interfaces.show_login_window()
        if name is None:
            return
        confirmed = interfaces.show_validation_window(name)

        if confirmed:
            break

    fm = models.FinanceManager()

    interfaces.show_welcome_window(name)

    interfaces.main_menu(fm, name)

if __name__ == "__main__":
    main() 