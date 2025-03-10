import unittest
from unittest import TestCase


# from src.course_management_system.course import Course
# from src.course_management_system.student import Student
# from src.course_management_system.facilitator import Facilitator

class TestCourse(TestCase):

    def test_that_course_title_code_facilitator_are_required_to_create_course_correctly(self):
        from src.course_management_system.courses import Courses
        courses = Courses()
        courses.add("Introduction to Java", "JAV 101", "Miss Jennifer")
        self.assertEqual("Miss Jennifer", courses.find_course_in_courses_by("Miss Jennifer").get_course_facilitator())
        self.assertEqual("Introduction to Java", courses.find_course_in_courses_by("Miss Jennifer").get_course_title())


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
