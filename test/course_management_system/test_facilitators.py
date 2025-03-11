from unittest import TestCase

from src.course_management_system.course import Course
from src.course_management_system.facilitators import Facilitators
from src.course_management_system.student import Student


class TestFacilitators(TestCase):
    def test_that_facilitators_can_register(self):
        facilitators = Facilitators("name", "email")
        self.assertEqual("You've been registered successfully", facilitators.register("name", "email"))

    def test_that_name_and_email_is_validated(self):
        facilitators = Facilitators("name", "email")
        facilitators.register("name", "email")
        with self.assertRaises(TypeError):
            facilitators.register("", 'email')

        with self.assertRaises(TypeError):
            facilitators.register('name', '')

    def test_that_facilitators_can_login(self):
        facilitators = Facilitators("name", "email")
        self.assertEqual("You've been logged in", facilitators.log_in("name", "email"))

    def test_that_facilitators_inputs_is_correct_before_logging_in(self):
        facilitators = Facilitators("name", "email")
        facilitators.log_in("name", "email")
        with self.assertRaises(TypeError):
            facilitators.log_in("", 'email')

        with self.assertRaises(TypeError):
            facilitators.register('name', '')

        with self.assertRaises(TypeError):
            facilitators.register('', '')

        with self.assertRaises(TypeError):
            facilitators.register('Tomi', '')


    # def test_that_facilitators_can_score_course(self):
    #     facilitators = Facilitators("name", "email")
    #     facilitators.log_in("name", "email")
    #
    #     course = Course()
    #     course.create_course("name", "chibuzor", 1)
    #     self.assertEqual(56,course.score_student("name","chibuzor",56))
    #
    # def test_that_facilitators_can_view_students(self):
    #     facilitators = Facilitators("name", "email")
    #     facilitators.log_in("name", "email")
    #
    #     student = Students()
    #     self.assertEqual("student", student.view_student("name", "email"))

    def test_that_facilitators_can_create_courses(self):
        facilitator = Facilitators("Chibuzo", "chibooze4real@gmail.com")
        facilitator.log_in("Chibuzo", "chibooze4real@gmail.com")
        created_course: Course = facilitator.create_course("EGL 101", "Introduction to English Language", 3, "Chibuzo")
        self.assertEqual("EGL 101", created_course.get_course_name())
        self.assertEqual("Chibuzo", created_course.get_course_instructor())

    def test_that_any_course_can_be_found_in_of_an_instructor(self):
        facilitator = Facilitators("Chibuzo", "chibooze4real@gmail.com")
        facilitator.log_in("Chibuzo", "chibooze4real@gmail.com")
        egl_1: Course = facilitator.create_course("EGL 101", "Introduction to English Language", 3, "Chibuzo")
        egl_2: Course = facilitator.create_course("EGL 201", "Advanced English Language", 4, "Chibuzo")
        courses: list[Course] = [egl_1, egl_2]
        self.assertEqual("EGL 101", egl_1.get_course_name())
        self.assertEqual("Chibuzo", egl_1.get_course_instructor())
        self.assertEqual(courses, facilitator.find_course_by_facilitator("Chibuzo"))
        print(courses)

