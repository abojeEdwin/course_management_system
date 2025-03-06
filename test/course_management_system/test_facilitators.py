from unittest import TestCase

from src.course_management_system.course import Course
from src.course_management_system.facilitators import Facilitators
from src.course_management_system.student import Student


class TestFacilitators(TestCase):
    def test_that_facilitators_can_register(self):
        facilitators = Facilitators("name", "email")
        self.assertEqual("You've been registered successfully", facilitators.register_facilitator("name", "email"))

    def test_that_name_and_email_is_validated(self):
        facilitators = Facilitators("name", "email")
        facilitators.register_facilitator("name", "email")
        with self.assertRaises(TypeError):
            facilitators.register_facilitator("", 'email')

        with self.assertRaises(TypeError):
            facilitators.register_facilitator('name', '')

    def test_that_facilitators_can_login(self):
        facilitators = Facilitators("name", "email")
        self.assertEqual("You've been logged in", facilitators.log_in("name", "email"))

    def test_that_facilitators_inputs_is_correct_before_logging_in(self):
        facilitators = Facilitators("name", "email")
        facilitators.log_in("name", "email")
        with self.assertRaises(TypeError):
            facilitators.log_in("", 'email')

        with self.assertRaises(TypeError):
            facilitators.register_facilitator('name', '')

        with self.assertRaises(TypeError):
            facilitators.register_facilitator('', '')

        with self.assertRaises(TypeError):
            facilitators.register_facilitator('Tomi', '')

    #
    # def test_that_facilitators_can_create_courses(self):
    #     facilitators = Facilitators("name", "email")
    #     facilitators.log_in("name", "email")
    #
    #     courses = Course("name","chibuzor",1)
    #     self.assertEqual("chibuzor", courses.create_course("name","chibuzor",1))

    # def test_that_facilitators_can_score_course(self):
    #     facilitators = Facilitators("name", "email")
    #     facilitators.log_in("name", "email")
    #
    #     course = Course("name","chibuzor",1)
    #     course.create_course("name", "chibuzor", 1)
    #     self.assertEqual(56,course.score_student("name","chibuzor",56))
    #
    # def test_that_facilitators_can_view_students(self):
    #     facilitators = Facilitators("name", "email")
    #     facilitators.log_in("name", "email")
    #
    #     student = Students()
    #     self.assertEqual("student", student.view_student("name", "email"))



