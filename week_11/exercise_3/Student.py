class Student:
    def __init__(self, student_id, name, section):
        self.student_id = student_id
        self.name = name
        self.section = section
        self.grades = {
            "spanish": None,
            "english": None,
            "social_studies": None,
            "science": None
        }

    def add_grade(self, subject, grade):

        subject = subject.lower().replace(" ", "_")

        if subject not in self.grades:
            raise ValueError(f"Subject '{subject}' is not valid.")

        try:
            numeric_grade = float(grade)
        except ValueError:
            raise ValueError("Grade must be a number.")

        if not 0 <= numeric_grade <= 100:
            raise ValueError("Grade must be between 0 and 100.")

        self.grades[subject] = numeric_grade