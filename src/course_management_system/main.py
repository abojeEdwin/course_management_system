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
                    pass

                case '3':
                    email = input("Enter your email : ")
                    password = input("Enter your password : ")
                    student = Student()
                    student.login(email, password)
                    student_menu()

                case '4':
                    email = input("Enter your email :")
                    password = input("Enter your password :")
                    pass
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
                student.register_course(course_name, email)
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












main()

