import re
from os import write
import bcrypt

class Student:
    def __init__(self):
        self.__full_name = None
        self.__first_name = None
        self.__last_name =  None
        self.__email = None
        self.__password = None
        self.__student_offered_courses = []
        self.__courses = []
        self.__list_of_student = []
        self.__student_grades = {}
        self.USER_DETAILS = 'user_login_details.txt'
        self.USER_REG_DETAILS = 'user_reg_details.txt'

    def get_student_list(self):
        for students in self.__list_of_student:
            return students

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_name(self):
        return self.__first_name + " " + self.__last_name



    def hash_password(self,password):
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        return hashed_password

    def save_to_file(self,email, password):
        with open(self.USER_DETAILS,'a') as file:
            file.write(f'{email}:{password.decode("utf-8")}\n')

    def save_course_reg_to_file(self,email,course_name):
        with open(self.USER_REG_DETAILS,'a') as file:
            file.write(f'{email}:{course_name}\n')


    def validate_password(self,password):
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8}$'
        if not re.match(pattern,password):
            return False
        return True

    def validate_name(self,first_name,last_name):
        pattern = r"^([A-Za-z]+$)"
        if not re.match(pattern, first_name):
            return False
        if not re.match(pattern, last_name):
            return False
        return True

    def validate_email(self,email):
            pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,3}$'
            return re.match(pattern,email)

    def validate_duplicate_user_email(self,email):
        with open(self.USER_DETAILS,'r') as file:
            details = file.read()
            for line in details.split("\n"):
                if line:
                    stored_email,stored_password = line.split(':')
                    if stored_email == email:
                        return False
        return True


    def validate_user(self,email,password):
           with open(self.USER_DETAILS,'r') as file:
                details = file.read()
                for line in details.split("\n"):
                    if line:
                        stored_email, stored_password = line.split(":")
                        if stored_email == email:
                            return bcrypt.checkpw(password.encode("utf-8"), stored_password.encode("utf-8"))
                return False

    def login(self,email,password):
        if  self.validate_user(email,password):
            return "Login successfully"
        else:
            return "Invalid username or password"


    def register(self,first_name,last_name,email, password):
            if not self.validate_name(first_name,last_name):
                print ("Please enter a valid name.")

            if not self.validate_email(email):
                print("Please enter a valid email address {example@gmail.com}")

            if not self.validate_password(password):
                print("Please enter a valid password {8 characters,Uppercase letters and Lowercase letters, At least one digit, No spaces , At least one character}")
            else:
                self.save_to_file(email,self.hash_password(password))
                self.set_first_name(first_name)
                self.set_last_name(last_name)
                self.__list_of_student.append(self.__full_name)
                print ("Registration successful")


    def register_course(self,course_name,email):
        from src.course_management_system.course import Course
        course = Course()
        if course_name == course.get_course_name():
            self.__student_offered_courses.append(course_name)
        else:
            print("Your selected course has not been added ")
        self.validate_reg_email(email)


    def validate_reg_email(self,email):
        with open(self.USER_REG_DETAILS, 'r') as file:
            details = file.read()
            for line in details.split("\n"):
                if line:
                    stored_email, stored_course_name = line.split(":")
                    if stored_email == email:
                        if not self.validate_email(email):
                            print("Please enter a valid email {example@gmail.com}")
                        elif self.validate_duplicate_user_email(email):
                            print("Your email already exist")

    def view_courses(self,email):
        if not self.validate_email(email):
            print("Please enter a valid email {example@gmail.com}")
        else:
            for courses in self.__student_offered_courses:
                print(courses)

    def view_course_instructor(self):
        while True:
            course_instructor = input("Enter your course : ")


    def view_grade(self,email):
            if not self.validate_email(email):
                print("Please enter a valid email {example@gmail.com}")
            #for grades in


    def get_offered_courses(self,course_name):
        for courses in self.__student_offered_courses:
            if course_name == courses:
                return courses
            else:
                return False
