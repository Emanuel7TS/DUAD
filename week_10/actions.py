#functions

def get_valid_name():
    while True:
        name = input("Type student name: ").strip()

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
             

def get_valid_grade():
    while True:
        try:
            grade = int(input("Type student grade: "))

            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

def add_student():
    students = []
    student = {}
    student_counter = 1
    running = True

    while running:
        "name" = get_valid_name()
        "section" = get_valid_section()
        "spanish" = get_valid_grade()
        "english" = get_valid_grade()
        "social_studies" = get_valid_grade()
        "science" = get_valid_grade()

        students.append(student)
    add_more = input("Do you want to add another student? (yes/no): ").lower()
    if add_more != "yes":
        running = False
    else:
        student_counter += 1
    return students

