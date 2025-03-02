from unittest import TestCase
from courseManagementSystem.src.course_management_system.course import Course

class TestCourse(TestCase):
    def setUp(self):
        self.course = Course()

    def test_that_course_name_can_be_retrieved_correctly(self):
        self.course.set_course_name("Biology")
        self.assertEqual("Biology", self.course.get_course_name())

    def test_that_course_grade_can_be_retrieved_correctly(self):
        self.course.set_course_grade(100)
        self.assertEqual("A", self.course.get_course_grade())

    def test_that_course_instructor_has_correct_name(self):
        self.course.set_course_instructor("Miss Africa")
        self.assertEqual("Miss Africa", self.course.get_course_instructor())