import csv
import os

def export_students_info(students):
    if not students:
        print("you have not added students yet")

    else: 

        with open('students_info.csv', 'w', newline='', encoding='utf-8') as new_file:
            fieldnames = [
                'Id', 'Name', 'Section',
                'Spanish Grade', 'English Grade',
                'Social Studies Grade', 'Science Grade'
            ]

            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
            csv_writer.writeheader()

            for student in students:
                student_info = {
                    "Id": student["id"],
                    "Name": student["name"],
                    "Section": student["section"],
                    "Spanish Grade": student["grades"]["spanish"],
                    "English Grade": student["grades"]["english"],
                    "Social Studies Grade": student["grades"]["social_studies"],
                    "Science Grade": student["grades"]["science"],
                }
                csv_writer.writerow(student_info)
        print("\nStudent data exported successfully to 'students_info.csv'.\n")


def import_valid_csv(students):
    if os.path.exists('students_info.csv'):
        with open('students_info.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for student in csv_reader:
                student_info = {
                    "id": int(student["Id"]),
                    "name": student["Name"],
                    "section": student["Section"],
                    "grades": {
                        "spanish": int(student["Spanish Grade"]),
                        "english": int(student["English Grade"]),
                        "social_studies": int(student["Social Studies Grade"]),
                        "science": int(student["Science Grade"])
                    }
                }
                students.append(student_info)
                print(student_info, "\n")
    else:
        print("El archivo 'students_info.csv' no existe. No se puede importar.")
