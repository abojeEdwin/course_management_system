from src.course_management_system.facilitator import Facilitator
from src.course_management_system.student import Student
from src.course_management_system.course import Course
import sys


def main():
        message = """
                Welcome To Your Course Management System!
                1 -> Register As Student
                2 -> Register As Facilitator
                3 -> Login As Student
                4 -> Login As Facilitator
                5 -> Exit
        """
        while True:
            choice = input(message)
            match choice:
                case '1':
                    first_name = input("Enter your first name : ")
                    last_name =  input("Enter your last name : ")
                    email = input("Enter your email : ")
                    password = input("Enter your password : ")
                    student = Student()
                    student.register(first_name, last_name, email, password)
                    student.save_to_file(email, password)

                case '2':
                    name = input("Enter your name :")
                    email = input ("Enter your email :")
                    password = input("Enter your password : ")
                    facilitator = Facilitator()
                    facilitator.register(name,email,password)
                    facilitator.save_registration_details_to_file(name,email,password)

                case '3':
                    email = input("Enter your email : ")
                    password = input("Enter your password : ")
                    student = Student()
                    student.login(email, password)
                    student_menu()

                case '4':
                    email = input("Enter your email :")
                    password = input("Enter your password :")
                    facilitator = Facilitator()
                    facilitator.login(email,password)
                    student_menu()
                case '5':
                    sys.exit(0)


def student_menu():
    student_menu = """
            1 -> Register Course
            2 -> View Courses
            3 -> View Grades
            4 -> View Course Instructors
            5 -> Exit
        """
    while True:
        student_choice = input(student_menu)
        match student_choice:
            case '1':
                student = Student()
                course_name = input("Enter your course name : ")
                email = input("Enter your email : ")
                course_code = input("Enter your course code")
                student.register_course(course_code,course_name,email)
                student.save_course_reg_to_file(email,course_name)

            case '2':
                student = Student()
                email = input("Enter your email : ")
                student.view_courses(email)

            case '3':
                student = Student()
                email = input("Enter your email : ")
                student.view_grade(email)

            case '4':
                student = Student()
                pass


            case '5':
                sys.exit(0)


def facilitator_menu():
    facilitator_menu = """
               1 -> Create Course
               2 -> View Courses 
               3 -> Assign Grades
               4 -> View Course Instructors
               5 -> Exit
           """
    while True:
        facilitator_choice = input(facilitator_menu)
        match facilitator_choice:
            case '1':
                facilitator = Facilitator()
                course_title = input("Enter your course title : ")
                course_code = input("Enter your course code : ")
                course_facilitator = input("Enter the course facilitator : ")
                facilitator.create_course(course_title,course_code,course_facilitator)

            case '2':
                facilitator = Facilitator()
                facilitator.view_created_courses()

            case '3':
                facilitator = Facilitator()
                #facilitator.assign_grade()

            case '4':
                pass

            case '5':
                sys.exit(0)









main()

