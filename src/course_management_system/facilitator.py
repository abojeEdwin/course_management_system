from src.course_management_system.course import Course


class Facilitator:
    def __init__(self):
        self.name = None
        self.email_address = None
        self.password = None

    def register_facilitator(self, name, email_address):
        if name and email_address:
            return "You've been registered successfully"
        if name == "":
            raise TypeError("Name cannot be empty")
        if email_address == "":
            raise TypeError("Email Address cannot be empty")

    def log_in(self,name,email_address):
        if name and email_address:
            return "You've been logged in"
        if name == "":
            raise TypeError("Name cannot be empty")
        if email_address == "":
            raise TypeError("Email Address cannot be empty")

    def score_student(self,student_name,score,course_name):
        if student_name and course_name:
            return score

    def create_course(self, course_title, course_code, course_facilitator):
        # from src.course_management_system.courses import Courses
        # courses = Courses()
        course = Course(course_title, course_code, course_facilitator)

        # courses.add(course_title, course_code, course_facilitator)
        return course

    # def find_course_by_facilitator(self, facilitator_name): -> Course:
    #     from src.course_management_system.courses import Courses
    #     courses = Courses()
    #     available_courses = courses.view_courses()
    #     for course in available_courses:
    #         if facilitator_name == course.get_course_facilitator():
    #             return course

        # courses = []
        # for course in self.courses:
        #     if course.get_course_instructor() == facilitator_name:
        #         courses.append(course)
        # return courses


