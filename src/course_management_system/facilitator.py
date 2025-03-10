import re
import bcrypt

from src.course_management_system.course import Course


class Facilitator:
    def __init__(self):
        self.name = None
        self.email_address = None
        self.password = None


    def set_name(self, name):
        self.name = name
    def set_email_address(self, email_address):
        self.email_address = email_address
    def set_password(self, password):
        self.password = password
    def get_name(self):
        return self.name
    def get_email_address(self):
        return self.email_address
    def get_password(self):
        return self.password

    def register(self, name, email_address, password):
        from src.course_management_system.admin import Admin
        if self.validate_facilitator_email(email_address) is False:
            print("Invalid email address.")
        elif self.validate_facilitator_password(password) is False:
            print("Invalid password.")
        elif self.validate_facilitator_name(name) is False:
            print("Invalid name.")
            return False
        else:
            facilitator = Facilitator()
            facilitator.set_name(name)

            facilitator.set_email_address(email_address)
            facilitator.set_password(self.hash_facilitator_password(password))

            admin = Admin()

            admin.add_facilitator(facilitator)
            self.save_registration_details_to_file(name, email_address, self.hash_facilitator_password(password))
            print('Facilitator successfully registered')
            return True

    @staticmethod
    def hash_facilitator_password(password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    @staticmethod
    def save_registration_details_to_file(name, email_address, hashed_password):
        with open('reg_details.txt', 'a') as reg_details_file:
            reg_details_file.write(f'{name}:{email_address}:{hashed_password.decode('utf-8')}\n')

        # if name and email_address:
        #     return "You've been registered successfully"
        # if name == "":
        #     raise TypeError("Name cannot be empty")
        # if email_address == "":
        #     raise TypeError("Email Address cannot be empty")

    @staticmethod
    def validate_facilitator_email(email_address):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,3}$'
        if re.fullmatch(pattern, email_address):
            return True
        else:
            return False

    @staticmethod
    def validate_facilitator_password(password):
        pattern = r'[A-Za-z1-9_!@]{8}'
        if re.fullmatch(pattern, password):
            return True
        else:
            return False

    @staticmethod
    def validate_facilitator_name(name):
        pattern = r'[A-Za-z]+\s[A-Za-z]+'
        if re.fullmatch(pattern, name):
            return True
        else:
            return False

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



