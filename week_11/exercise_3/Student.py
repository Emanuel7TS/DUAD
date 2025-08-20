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
        normalized_subject = subject.lower().replace(" ", "_")
        if normalized_subject not in self.grades:
            raise ValueError(f"Subject '{subject}' is not valid.")

        try:
            numeric_grade = float(grade)
        except ValueError:
            raise ValueError("Grade must be a number.")

        if not 0 <= numeric_grade <= 100:
            raise ValueError("Grade must be between 0 and 100.")

        self.grades[normalized_subject] = numeric_grade

    def average(self):
        valid = [g for g in self.grades.values() if g is not None]
        if not valid:
            return None
        return round(sum(valid) / len(valid), 2)

    def __str__(self):
        grades_str = ", ".join(
            f"{subj.capitalize()}: {grade if grade is not None else '-'}"
            for subj, grade in self.grades.items()
        )
        return (
            f"ID: {self.student_id}, Name: {self.name}, Section: {self.section}, "
            f"Average: {self.average() if self.average() is not None else 'N/A'}\n"
            f"Grades -> {grades_str}"
        )

    def to_dict(self):
        return {
            "Id": self.student_id,
            "Name": self.name,
            "Section": self.section,
            "Spanish Grade": self.grades["spanish"],
            "English Grade": self.grades["english"],
            "Social Studies Grade": self.grades["social_studies"],
            "Science Grade": self.grades["science"]
        }

    @classmethod
    def from_dict(cls, data):
        new_student = cls(
            int(data["Id"]),
            data["Name"],
            data["Section"]
        )
        new_student.grades = {
            "spanish": int(data["Spanish Grade"]),
            "english": int(data["English Grade"]),
            "social_studies": int(data["Social Studies Grade"]),
            "science": int(data["Science Grade"])
        }
        return new_student