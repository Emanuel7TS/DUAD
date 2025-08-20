#functions

def get_valid_name():
    while True:
        name = input("\nEnter the student's name: ").strip()

        if name.replace(" ", "").isalpha():
            return name
        else:
            print("Invalid input. The name should only contain letters.")

def get_valid_section():
    while True:
        section = input("Enter the student's section: ").strip()

        if section == "":
            print("Section cannot be empty. Please try again.")
        else:
            return section


def get_all_valid_grades():
    subjects = ["Spanish", "English", "Social Studies", "Science"]
    grades = {}

    for subject in subjects:
        while True:
            try:
                grade = int(input(f"Enter the student's grade for {subject}: "))
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
            "id": student_counter,
            "name": name,
            "section": section,
            "grades": grades
        }

        students.append(student)
        print(f"\nStudent {name} was added successfully.\n")


        while True:
            add_more = input("Would you like to add another student? (yes/no): ").lower()
            if add_more in ["yes", "no"]:
                break
            print("Invalid choice. Please enter 'yes' or 'no'.")

        if add_more == "no":
            print("\n---------------- Returning to Main Menu ----------------\n")
            running = False
        else:
            student_counter += 1

def show_students_info(students):

    for student in students:
        print(f"ID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Section: {student['section']}")
        print("Grades:")
        for subject, grade in student['grades'].items():
            print(f"  {subject.capitalize()}: {grade}")
        print("\n" + "-" * 40 + "\n")

def get_average(students):
        students_average = []
        for student in students:
            total = 0
            average = 0
            grades = student["grades"].values()

            for grade in grades:
                total += grade
            average = total/(len(grades))

            student_average_info = {"Id":student["id"] ,
                                    "Name":student["name"],
                                    "Average":average
                                    }
            students_average.append(student_average_info)

        return students_average

def get_average_key(student):
    return student["Average"]

def get_top_3_average(students_average):
    top_students_average = students_average
    students_average.sort(key=get_average_key,reverse=True)

    if (len(top_students_average)) >= 3:
        for i in range(0,3):
            print(f"Top {i+1} = ID: {top_students_average[i]['Id']} Name: {top_students_average[i]['Name']} Average: {top_students_average[i]['Average']}")
    else:
        print("\nAt least 3 students are required to calculate the top 3 averages.\n ")

def get_general_average(students_average):
    if (len(students_average)) > 1:
        sum = 0
        for student in students_average:
            average = student["Average"]
            sum += average
        general_average = round((sum/(len(students_average))),2)
        print (f"The general average from {len(students_average)} es: {general_average} ")
    else: 
        print("Cannot calculate general average with fewer than 2 students.")
