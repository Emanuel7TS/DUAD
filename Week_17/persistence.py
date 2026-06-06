import csv
import os
from models import FinanceManager


def store_categories(categories):

    if not categories:
        raise ValueError("There are no categories to store")

    with open("categories.csv", "w", newline="", encoding="utf-8") as new_file:

        for category_name in categories.keys():
            new_file.write(f"{category_name}\n")


def store_movements(movements):

    if not movements:
        raise ValueError("There are no movements to store")

    with open("movements.csv", "w", newline="", encoding="utf-8") as new_file:

        for movement in movements:
            name = movement.name
            value = movement.value
            type = movement.type
            category = movement.category.name
            new_file.write(f"{movement.name},{movement.value},{movement.type},{movement.category.name}\n")


def load_categories(finance_manager):
    if os.path.exists('categories.csv'):
            
            with open('categories.csv', 'r') as csv_file:
                for row in csv_file:
                    category_key = row.strip()
                    if category_key in finance_manager.categories:
                        continue
                    finance_manager.add_category(row.strip())

    else:
        raise FileNotFoundError("No category CSV file found to import.")


def load_movements(finance_manager):
    if os.path.exists('movements.csv'):
        with open('movements.csv', 'r') as csv_file:
            for row in csv_file:
                parts = row.strip().split(",")
                name = parts[0]
                value = float(parts[1])
                type = parts[2]
                category = parts[3]
                finance_manager.add_movement(name,value,type,finance_manager.categories[category])
    else:
        raise FileNotFoundError("No Movement CSV file found to import.")