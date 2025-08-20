import csv
import os
from student import Student


def export_students_info(students):
    if not students:
        print("No students to export. Please add students first.")
        return

    with open('students_info.csv', 'w', newline='', encoding='utf-8') as new_file:
        fieldnames = [
            'Id', 'Name', 'Section',
            'Spanish Grade', 'English Grade',
            'Social Studies Grade', 'Science Grade'
        ]
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
        csv_writer.writeheader()

        for student in students:
            csv_writer.writerow(student.to_dict())

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
