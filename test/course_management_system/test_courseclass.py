import unittest
from unittest import TestCase
from src.course_management_system.course import Course
from src.course_management_system.student import Student
from src.course_management_system.facilitators import Facilitators

class TestCourse(TestCase):
    def setUp(self):
        self.course = Course()
        # self.student = Student()

    def test_that_course_name_can_be_retrieved_correctly(self):
        self.course.set_course_name("Biology")
        self.assertEqual("Biology", self.course.get_course_name())

    def test_that_course_grade_can_be_retrieved_correctly(self):
        self.course.set_course_grade(100)
        self.assertEqual("A", self.course.get_course_grade())

    def test_that_course_instructor_has_correct_name(self):
        self.course.set_course_instructor("Miss Africa")
        self.assertEqual("Miss Africa", self.course.get_course_instructor())

    def test_that_course_has_a_list_of_students_when_i_find_student_by_name_returns_student(self):
        from src.course_management_system.student import Student
        student = Student()
        student.register("Divine", "Favour", "divfav@gmail.com", "12ABcd@*")
        self.course.set_course_instructor("Miss Africa")
        self.course.set_course_name("Biology")
        self.course.add_student(student)
        self.assertEqual(True, self.course.find_student_by_full_name("Divine Favour"))

    def test_that_course_has_a_list_of_students_when_i_find_student_by_name_returns_student1(self):
        self.course.set_course_instructor("Miss Africa")
        self.course.set_course_name("Biology")
        student = Student()
        student.register("Divine", "Favour", "divfav@gmail.com", "12ABcd@*")
        print(student.view_courses("divfav@gmail.com"))
        facilitator = Facilitators("Chi Gozie", "chigozie@gmail.com")
        facilitator.register_facilitator("Chi Gozie", "chigozie@gmail.com")


