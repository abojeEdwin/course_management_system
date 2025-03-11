from src.course_management_system.student import Student
from src.course_management_system.course import Course
from src.course_management_system.facilitator import Facilitator
class Admin:
    def __init__(self):
        self.facilitators: list[Facilitator] = []
        self.courses: list[Course] = []
        self.students: list[Student] = []

    def add_facilitator(self, facilitator):
        self.facilitators.append(facilitator)
    def add_course(self, course):
        self.courses.append(course)
    def add_student(self, student):
        self.students.append(student)

    def get_facilitators(self):
        return self.facilitators
    def get_courses(self):
        return self.courses
    def get_students(self):
        return self.students

