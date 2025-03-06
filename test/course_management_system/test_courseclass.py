import unittest
from unittest import TestCase


import courseManagementSystem.src.course_management_system.course
import courseManagementSystem.src.course_management_system.student

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
        self.course.set_course_instructor("Miss Africa")
        self.course.set_course_name("Biology")
        student = Student("Divine", "Favour", "divfav@gmail.com", "12ABcd@*")
        self.course.add_student(student)
        self.assertEqual(student, self.course.find_student_by_full_name("Divine Favour"))


