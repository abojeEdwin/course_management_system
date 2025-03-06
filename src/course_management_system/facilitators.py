from course_management_system.src.course_management_system.course import Course


class Facilitators:
    def __init__(self,name,email_address):
        self.courses = []
        self.name = name
        self.email_address = email_address

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

    def create_course(self, course_name, course_title, course_units, facilitator_name):
        course = Course()
        course.set_course_name(course_name)
        course.set_course_title(course_title)
        course.set_course_unit(course_units)
        course.set_course_instructor(facilitator_name)
        self.courses.append(course)
        return course

    def find_course_by_facilitator(self, facilitator_name):
        courses = []
        for course in self.courses:
            if course.get_course_instructor() == facilitator_name:
                courses.append(course)
        return courses


