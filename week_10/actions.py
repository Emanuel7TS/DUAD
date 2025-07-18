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

def add_student():
    students = []
    student_counter = 1
    running = True

    while running:
        name = get_valid_name()
        section = get_all_valid_grades()
        spanish = get_all_valid_grades()
        english = get_all_valid_grades()
        social_studies = get_all_valid_grades()
        science = get_all_valid_grades()

        student = {
            "name": name,
            "section": section,
            "spanish": spanish,
            "english": english,
            "social_studies": social_studies,
            "science": science
        }

        students.append(student)
        print("Student has been added succesfully")

        # Preguntar si quiere seguir
        while True:
            add_more = input("Do you want to add another student? (yes/no): ").lower()
            if add_more in ["yes", "no"]:
                break
            print("Invalid input. Please type 'yes' or 'no'.")

        if add_more == "no":
            running = False
        else:
            student_counter += 1

    return students