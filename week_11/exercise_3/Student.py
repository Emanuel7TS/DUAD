class StudentManager():
    def __init__(self, students):
        self.students = []
     
    def CalculateAverage(self.students):
        students_average = []
        for student in self.students:
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