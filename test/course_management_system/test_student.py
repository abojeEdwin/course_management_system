import unittest
from src.course_management_system.student import Student


class MyTestCase(unittest.TestCase):
    def test_that_student_class_returns_correct_name(self):
        student = Student("Edwin","Aboje","abojeedwin@gmail.com","123456")
        actual = student.get_full_name()
        expected = "Edwin Aboje"
        self.assertEqual(actual, expected)

    def test_that_student_email_and_password_can_save_to_file(self):
        student = Student("Edwin","Aboje","abojeedwin@gmail.com","123456")
        actual = student.save_to_file("abojeedwin@gmail.com","123456")
        expected = "Edwin Aboje"
        self.assertEqual(actual,expected)



if __name__ == '__main__':
    unittest.main()
