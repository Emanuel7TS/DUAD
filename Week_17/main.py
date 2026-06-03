import FreeSimpleGUI as sg
import interfaces
import models

def main():

    name = interfaces.show_login_window()

    if not name:
        return

    confirmed = interfaces.show_validation_window(name)

    if not confirmed:
        return

    fm = models.FinanceManager()

    interfaces.show_welcome_window(name)

    interfaces.main_menu(fm, name)

if __name__ == "__main__":
    main() 