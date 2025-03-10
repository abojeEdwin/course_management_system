
from src.course_management_system.student import Student
from src.course_management_system.user import User

class Course:
    def __init__(self):
        self.facilitator_name = None
        self.course_title = None
        self.course_unit = None
        self.students = []

    def set_course_name(self, course_name):
        self.course_name = course_name

    def get_course_name(self):
        return self.course_name

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

    def set_course_instructor(self, facilitator):
        self.facilitator = facilitator

    def get_course_instructor(self):
        return self.facilitator

    def find_student_by_full_name(self, student_name):
        for student_name in self.students:
            if student_name in self.students and student_name is not None:
                return True
            return False

    def add_student(self, student : Student):
        # from src.course_management_system.student import Student
        my_student = Student
        self.students.append(my_student.get_student_list(student))
        # name = student.get_student_list(Student())
        # for student_names in name:
        #     self.students.append(student_names)



    def set_course_title(self, course_title):
        self.course_title = course_title

    def get_course_title(self):
        return self.course_title

    def set_course_unit(self, course_unit):
        self.course_unit = course_unit

    def get_course_unit(self):
        return self.course_unit
