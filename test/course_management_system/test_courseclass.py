import unittest
from unittest import TestCase

from src.course_management_system.course import Course
from src.course_management_system.student import Student
# from src.course_management_system.facilitator import Facilitator

class TestCourse(TestCase):

    def test_that_course_title_code_facilitator_are_required_to_create_course_correctly(self):
        from src.course_management_system.facilitator import Facilitator
        facilitator = Facilitator()
        facilitator.register("Miss Jennifer", "jenn@gmail.com", "Pass12@_")
        self.assertTrue(facilitator.is_registered())
        self.assertTrue(facilitator.login("jenn@gmail.com", "Pass12@_"))

        from src.course_management_system.courses import Courses
        courses = Courses()
        facilitator.create_course("Introduction to Java", "JAV 101", "Miss Jennifer")
        self.assertTrue(facilitator.is_course_created())
        self.assertEqual("Miss Jennifer", facilitator.find_course_by_facilitator("Miss Jennifer").get_course_facilitator())
        courses.add("Introduction to Java", "JAV 101", "Miss Jennifer")
        self.assertEqual("Miss Jennifer", courses.find_course_in_courses_by("Miss Jennifer").get_course_facilitator())

    def test_that_instructor_registers_first_before_course_is_created(self):
        from src.course_management_system.facilitator import Facilitator
        facilitator = Facilitator()
        self.assertTrue(facilitator.register("Miss Jennifer", "jenn@gmail.com", "Pass12@_"))
        from src.course_management_system.courses import Courses
        courses = Courses()
        courses.add("Introduction to Java", "JAV 101", "Miss Jennifer")
        self.assertTrue(facilitator.login("jenn@gmail.com", "Pass12@_"))

    def test_that_instructors_can_view_students_enrolled_in_their_course(self):
        from src.course_management_system.facilitator import Facilitator
        facilitator = Facilitator()
        facilitator.register("Miss Jennifer", "jenn@gmail.com", "Pass12@_")
        self.assertTrue(facilitator.is_registered())
        course = facilitator.create_course("Introduction to Java", "JAV 101", "Miss Jennifer")
        self.assertTrue(facilitator.is_course_created())

        from src.course_management_system.admin import Admin
        admin = Admin()
        admin.add_facilitator(facilitator)
        admin.add_course(course)
        print(admin.get_courses())
        print(admin.get_facilitators())
        # from src.course_management_system.courses import Courses
        # courses = Courses()
        # courses.add("Introduction to Java", "JAV 101", "Miss Jennifer")

        self.assertFalse(facilitator.login("jen@gmail.com", "Pass12@_"))
        self.assertTrue(facilitator.login("jenn@gmail.com", "Pass12@_"))

        from src.course_management_system.student import Student
        student = Student()
        student.register("John", "Doe", "jdoe@gmail.com", "passWO1@")
        # print(student.view_available_courses())





    # def test_that_course_grade_can_be_retrieved_correctly(self):
    #     self.course.set_course_grade(100)
    #     self.assertEqual("A", self.course.get_course_grade())
    #
    # def test_that_course_instructor_has_correct_name(self):
    #     self.course.set_course_instructor("Miss Africa")
    #     self.assertEqual("Miss Africa", self.course.get_course_instructor())
    #
    # def test_that_course_has_a_list_of_students_when_i_find_student_by_name_returns_student(self):
    #     self.course.set_course_instructor("Miss Africa")
    #     self.course.set_course_name("Biology")
    #     student = Student()
    #     self.course.add_student(student)
    #     self.assertEqual(student, self.course.find_student_by_full_name("Divine Favour"))
    #
    # def test_that_course_has_a_list_of_students_when_i_find_student_by_name_returns_student1(self):
    #     self.course.set_course_instructor("Miss Africa")
    #     self.course.set_course_name("Biology")
    #     student = Student()
    #     student.register("Divine", "Favour", "divfav@gmail.com", "12ABcd@*")
    #     print(student.view_courses("divfav@gmail.com"))
    #     facilitator = Facilitators("Chi Gozie", "chigozie@gmail.com")
    #     facilitator.register_facilitator("Chi Gozie", "chigozie@gmail.com")
    #
    #
