import re
import bcrypt

from src.course_management_system.course import Course


class Facilitator:
    def __init__(self):
        self.name = None
        self.email_address = None
        self.password = None
        self.facilitators_courses: list[Course] = []
        self.is_facilitator_registered = False
        self.is_created = False


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
            self.is_facilitator_registered = True
            return True

    def login(self, email_address, password):
        if self.validate_reg_details(email_address, password) is False:
            print("Invalid registration details.")
            return False
        else:
            print("Logged in successfully.")
            return True


    def hash_facilitator_password(self,password):
        if isinstance(password, str):
            password = password.encode("utf-8")
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
        return hashed_password


    def save_registration_details_to_file(self,name, email_address, password):
        with open('facilitator_reg_details.txt', 'a') as file:
            file.write(f'{name}:{email_address}:{self.hash_facilitator_password(password).decode('utf-8')}\n')



    def validate_reg_details(self,email_address, password):
        with open('facilitator_reg_details.txt', 'r') as reg_details_file:
            for line in reg_details_file:
                stored_name, stored_email_address, stored_password = line.strip().split(':')
                if stored_email_address == email_address:
                    return bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8'))
                else:
                    return False


    def validate_facilitator_email(self,email_address):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,3}$'
        if re.fullmatch(pattern, email_address):
            return True
        else:
            return False


    def validate_facilitator_password(self,password):
        pattern = r'[A-Za-z1-9_!@]{8}'
        if re.fullmatch(pattern, password):
            return True
        else:
            return False


    def validate_facilitator_name(self,name):
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
        course = Course()
        course.set_course_title(course_title)
        course.set_course_code(course_code)
        course.set_course_facilitator(course_facilitator)
        self.facilitators_courses.append(course)
        self.is_created = True

        from src.course_management_system.admin import Admin
        admin = Admin()
        admin.add_course(course)

        return course


    def view_created_courses(self):
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

    def is_registered(self):
        if self.is_facilitator_registered is False:
            return False
        elif self.is_facilitator_registered is True:
            return True

    def is_course_created(self):
        if self.is_created is False:
            return False
        elif self.is_created is True:
            return True

    def assign_grade(self, course_code, score):
        from src.course_management_system.student import Student
        student = Student()
        for course in self.facilitators_courses:
            if student.get_offered_courses(course_code) == course.get_course_code():
                course.set_course_grade(score)
                return course.get_course_grade()
