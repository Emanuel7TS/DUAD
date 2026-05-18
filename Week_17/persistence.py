import csv
import os
from models import FinanceManager


def store_categories(categories):

    if not categories:
        raise ValueError("There are no categories to store")

    with open("categories.csv", "w", newline="", encoding="utf-8") as new_file:

        for category_name in categories.keys():
            new_file.write(f"{category_name}\n")
    print("\nStudent data was successfully exported to 'students_info.csv'.\n")


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
    print("\nStudent data was successfully exported to 'students_info.csv'.\n")


def load_categories(manager_cat):
    if os.path.exists('categories.csv'):
        with open('categories.csv', 'r') as csv_file:
            for row in csv_file:
                manager_cat.add_category(row.strip())
    else:
        print("No CSV file found to import.")


def load_movements(manager_cat):
    if os.path.exists('movements.csv'):
        with open('categories.csv', 'r') as csv_file:
            for row in csv_file:
                parts = row.strip().split(",")
                name = parts[0]
                value = float(parts[1])
                type = parts[2]
                category = parts[3]
                manager_cat.add_movement(name,value,type,manager_cat.categories[category])
    else:
        print("No CSV file found to import.")