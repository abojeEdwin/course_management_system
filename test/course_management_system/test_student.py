import unittest

class MyTestCase(unittest.TestCase):
    def test_that_student_can_register(self):
        from src.course_management_system.student import Student
        student = Student()
        student.register("Edwin","Aboje","abojeedwin@gmail.com","Test123!")
        self.assertEqual("Edwin Aboje", student.get_name())

    def test_that_student_uses_a_valid_email(self):
        from src.course_management_system.student import Student
        student = Student()
        student.login("abojeedwin@gmail.com","Test123!")
        self.assertEqual(True, student.validate_email("abojedwin@gmail.com"))

    def test_that_student_uses_a_invalid_password(self):
        from src.course_management_system.student import Student
        student = Student()
        student.login("abojeedwin@gmail.com", "Test123")
        self.assertEqual(False,student.validate_password("Test123"))







if __name__ == '__main__':
    unittest.main()
