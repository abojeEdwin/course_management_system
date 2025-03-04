import unittest
from src.course_management_system.student import Student


class MyTestCase(unittest.TestCase):
    def test_that_student_class_returns_correct_name(self):
        student = Student("Edwin","Aboje","abojeedwin@gmail.com","123456")
        actual = student.get_full_name()
        expected = "Edwin Aboje"
        self.assertEqual(actual, expected)

    def test_that_student_class_logins_in(self):
        self.student = Student("Edwin","Aboje","abojeedwin@gmail.com","123456")
        actual = self.student.register("Aboje Edwin","abojeedwin@gmail.com","12345")
        expected = "Registration Successful"
        self.assertEqual(actual, expected)



if __name__ == '__main__':
    unittest.main()
