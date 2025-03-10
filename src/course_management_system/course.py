from src.course_management_system.student import Student
from src.course_management_system.user import User

class Course:
    def __init__(self, course_title, course_code, course_facilitator):
        self.course_title = course_title
        self.course_code = course_code
        self.course_facilitator = course_facilitator
        self.students : list[Student] = []

    def set_course_title(self, course_title):
        self.course_title = course_title

    def get_course_title(self):
        return self.course_title

    def set_course_code(self, course_code):
        self.course_code = course_code
    def get_course_code(self):
        return self.course_code
    def set_course_facilitator(self, course_facilitator):
        self.course_facilitator = course_facilitator
    def get_course_facilitator(self):
        return self.course_facilitator

    def set_course_grade(self, course_score):
        if 70 <= course_score <= 100:
            self.course_grade = "A"
        elif 60 <= course_score <= 69:
            self.course_grade = "B"
        elif 50 <= course_score <= 59:
            self.course_grade = "C"
        elif 40 <= course_score <= 49:
            self.course_grade = "D"
        elif 30 <= course_score <= 39:
            self.course_grade = "E"
        elif 0 <= course_score <= 29:
            self.course_grade = "F"


    def get_course_grade(self):
        return self.course_grade

    def find_student_by_full_name(self, student_name):
        for student in self.students:
            if student.get_name() == student_name and student is not None:
                return student

    def add_student(self, student):
        self.students.append(student)

