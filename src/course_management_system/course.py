#from src.course_management_system.student import Student

class Course:
    def __init__(self):
        self.course_name = None
        self.course_grade = None
        self.facilitator = None
        self.students : list[Student] = []

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
        for student in self.students:
            if student.get_full_name() == student_name and student is not None:
                return student

    def add_student(self, student):
        self.students.append(student)
