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

def import_valid_csv(students):
    if os.path.exists('students_info.csv'):
        with open('students_info.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                new_student = Student.from_dict(row)
                students.append(new_student)
                print(new_student)
    else:
        print("No CSV file found to import.")