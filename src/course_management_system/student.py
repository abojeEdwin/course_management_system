import re
from os import write
import bcrypt

from src.course_management_system import course
from src.course_management_system.user import User
from src.course_management_system.course import Course

student_offered_courses = []
course = Course()

USER_DETAILS = 'user_details.txt'

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def save_to_file(email, password):
    with open( USER_DETAILS,'a') as file:
        file.write(f'{email}:{password.decode('utf-8')}\n')


def register():
    while True:
        full_name = input("Enter your first name :")
        if not validate_name(full_name):
            print("Please enter a valid name.")
            continue
        break
    while True:
        email = input("Enter your email :")
        if not validate_email(email):
            print("Please enter a valid email address {example@gmail.com}")
            continue
        break
    while True:
        password = input("Enter your password :")
        if not validate_password(password):
            print("Please enter a valid password {8 characters,Uppercase letters and Lowercase letters, At least one digit, No spaces , At least one character}.")
            continue
        break


def validate_password(password):
    pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#%^&*(),.?":{}|<>])[A-Za-z\d!@#$%^&(),.?"{}|<>{8,}$)'
    return re.match(pattern, password)


def validate_name(full_name):
    pattern = r"^[A-Za-z]+(?:[-] [A-Za-z]+)*$)"
    return re.match(pattern,full_name)


def validate_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,3}$'
        return re.match(pattern,email)

def validate_duplicate_user_email(email):
    with open(USER_DETAILS,'r') as file:
        details = file.read()
        for line in details.split("\n"):
            if line:
                stored_email,stored_password = line.split(':')
                if stored_email == email:
                    return False
    return True


def validate_user(email,password):
       with open(USER_DETAILS,'r') as file:
           details = file.read()
           for line in details.split("\n"):
               if line:
                   stored_email, stored_password = line.split(":")
                   if stored_email == email:
                       return bcrypt.checkpw(password.encode("utf-8"), stored_password.encode("utf-8"))
       return False

def login():
    email = input("Enter your email :")
    password = input("Enter your password :")
    if  validate_user(email,password):
        print("Login successfully")
    else:
        print("Invalid username or password")


def register_course():
    while True:
        course_name = input("Enter the course you want to register for : ")
        if course_name.casefold() == course.get_course_name():
            student_offered_courses.append(course_name)
        else:
            print("Your selected course has not been added ")
            continue
        break
    while True:
        email = input("Enter your email : ")
        if not validate_email(email):
            print("Please enter a valid email {example@gmail.com}")
        elif validate_duplicate_user_email(email):
            print("Your email already exist")
        else:
            print("Course registration successful")
            continue
        break

def view_courses():
    pass

class Student(User):
    def __init__(self, first_name, last_name, email, password):
        super().__init__(first_name, last_name, email, password)

