import re
import bcrypt

from src.course_management_system.course import Course


class Facilitator:
    def __init__(self):
        self.name = None
        self.email_address = None
        self.password = None
        self.facilitators_courses: list[Course] = []


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

    def login(self, email_address, password):
        if self.validate_reg_details(email_address, password) is False:
            print("Invalid registration details.")
            return False
        else:
            print("Logged in successfully.")
            return True

    @staticmethod
    def hash_facilitator_password(password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    @staticmethod
    def save_registration_details_to_file(name, email_address, hashed_password):
        with open('facilitator_reg_details.txt', 'a') as reg_details_file:
            reg_details_file.write(f'{name}:{email_address}:{hashed_password.decode('utf-8')}\n')

        # if name and email_address:
        #     return "You've been registered successfully"
        # if name == "":
        #     raise TypeError("Name cannot be empty")
        # if email_address == "":
        #     raise TypeError("Email Address cannot be empty")

    @staticmethod
    def validate_reg_details(email_address, password):
        with open('facilitator_reg_details.txt', 'r') as reg_details_file:
            for line in reg_details_file:
                stored_name, stored_email_address, stored_password = line.strip().split(':')
                if stored_email_address == email_address:
                    return bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8'))
                else:
                    return False

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

    # def log_in(self,name,email_address):
    #     if name and email_address:
    #         return "You've been logged in"
    #     if name == "":
    #         raise TypeError("Name cannot be empty")
    #     if email_address == "":
    #         raise TypeError("Email Address cannot be empty")

    def score_student(self,student_name,score,course_name):
        if student_name and course_name:
            return score

    def create_course(self, course_title, course_code, course_facilitator):
        course = Course(course_title, course_code, course_facilitator)
        self.facilitators_courses.append(course)

        from src.course_management_system.admin import Admin
        admin = Admin()
        admin.add_course(course)

        return course


    def view_created_courses(self, course_facilitator):
        return self.facilitators_courses

    def find_course_by_facilitator(self, facilitator_name):
        for course in self.facilitators_courses:
            if course.get_course_facilitator() == facilitator_name:
                return course

        # courses = []
        # for course in self.courses:
        #     if course.get_course_instructor() == facilitator_name:
        #         courses.append(course)
        # return courses



