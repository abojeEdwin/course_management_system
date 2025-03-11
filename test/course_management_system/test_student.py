import unittest
from src.course_management_system.student import Student


class MyTestCase(unittest.TestCase):


    def test_that_student_can_register(self):
        student = Student()
        student.register("Edwin","Aboje","abojeedwin@gmail.com","Test123!")
        self.assertEqual("Edwin Aboje", student.get_name())

    def test_that_student_can_login(self):
        student = Student()
        student.register("Edwin", "Aboje", "abojeedwin@gmail.com", "Test123!")
        self.assertEqual("Login successfully",student.login("abojeedwin@gmail.com","Test123!"))

    def test_that_student_does_not_register_with_invalid_credentials(self):
       student = Student()
       self.assertRaises(TypeError,student.register,"Edwin", " ", "abojeedwingmail.com", "Test12")

    def test_that_student_can_register_course(self):
        student = Student()
        student.register("Edwin", "Aboje", "abojeedwin@gmail.com", "Test123!")
        student.login("abojeedwin@gmail.com", "Test123!")
        self.assertEqual("Your selected course has not been added ",student.register_course("Chemistry","abojeedwin@gmail.com"))

    def test_that_student_can_view_courses_enrolled_for(self):
        student = Student()
        student.register("Edwin", "Aboje", "abojeedwin@gmail.com", "Test123!")
        student.login("abojeedwin@gmail.com", "Test123!")
        student.register_course("Chemistry", "abojeedwin@gmail.com")
        self.assertEqual("Chemistry",student.view_courses("abojeedwin@gmail.com"))






if __name__ == '__main__':
    unittest.main()
