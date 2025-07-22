#functions

def get_valid_name():
    while True:
        name = input("\nType student name: ").strip()

        if name.replace(" ", "").isalpha():
            return name
        else:
            print("Name can only contain letters.")

def get_valid_section():
    while True:
        section = input("Type student section: ").strip()

        if section == "":
            print("Name cannot be empty. Please try again.")
        else:
            return section
             

def get_all_valid_grades():
    subjects = ["Spanish", "English", "Social Studies", "Science"]
    grades = {}

    for subject in subjects:
        while True:
            try:
                grade = int(input(f"Type student {subject} grade: "))
                if 0 <= grade <= 100:
                    grades[subject.lower().replace(" ", "_")] = grade
                    break
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")
    
    return grades

def add_student(students):
    student_counter = len(students) + 1
    running = True

    while running:
        name = get_valid_name()
        section = get_valid_section()
        grades = get_all_valid_grades()

        student = {
            "Id": student_counter,
            "name": name,
            "section": section,
            "grades": grades
        }

        students.append(student)
        print("\nStudent has been added successfully\n")

        while True:
            add_more = input("Do you want to add another student? (yes/no): ").lower()
            if add_more in ["yes", "no"]:
                break
            print("Invalid input. Please type 'yes' or 'no'.")

        if add_more == "no":
            print("\n-------------------------------------------------\n")
            running = False
        else:
            student_counter += 1

def show_students_info(students):
    for student in students:
        print(f"ID: {student['Id']}")
        print(f"Name: {student['name']}")
        print(f"Section: {student['section']}")
        print("Grades:")
        for subject, grade in student['grades'].items():
            print(f"  {subject.capitalize()}: {grade}")
        print("-" * 30)

def get_average(students):
    for student in students:
        sum = 0
        average = 0
        grades = student["grades"].values()
        for grade in grades:
            sum += grade
        average = sum/(len(grades))
        student["Average"] = average

def get_top_3_average(students):
    average_list = [] 
    for student in students:
        for average in student["average"]:
            list.append