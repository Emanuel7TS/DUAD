from student import Student

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
        student = Student(student_counter, name, section)
        student.grades = grades
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
    if not students:
        print("No students registered yet.")
        return
    for student in students:
        print(student)
        print("\n" + "-" * 40 + "\n")

def get_average(students):
    students_average = []
    for student in students:
        students_average.append({
            "Id": student.student_id,
            "Name": student.name,
            "Average": student.average()
        })
    return students_average

def get_top_3_average(students):
    if len(students) < 3:
        print("\nAt least 3 students are required to calculate the top 3 averages.\n")
        return
    sorted_students = sorted(students, key=lambda s: s.average() or 0, reverse=True)
    for i, student in enumerate(sorted_students[:3], start=1):
        print(f"Top {i} = {student}")

def get_general_average(students):
    averages = [s.average() for s in students if s.average() is not None]
    if len(averages) > 1:
        general_average = round(sum(averages) / len(averages), 2)
        print(f"The general average from {len(averages)} students is: {general_average}")
    else:
        print("Cannot calculate general average with fewer than 2 students.")