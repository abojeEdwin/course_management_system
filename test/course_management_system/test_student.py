import unittest

from src.course_management_system.facilitator import Facilitator
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
        self.assertEqual("Your selected course has not been added ",student.register_course("ECO299","Economics","abojeedwin@gmail.com"))

    def test_that_student_can_view_courses_enrolled_for(self):
        student = Student()
        facilitator = Facilitator()
        facilitator.register("Mr Franco","franco@gmail.com","Test12t@")
        facilitator.create_course("Statistics","STA322","Evans")
        facilitator.create_course("Chemistry","CHEM322","Francis")
        student.register("Edwin", "Aboje", "abojeedwin@gmail.com", "Test123!")
        student.login("abojeedwin@gmail.com", "Test123!")
        student.register_course("CHEM322", "Chemistry","abojeedwin@gmail.com")
        student.register_course("STA322","Statistics","abojeedwin@gmail.com")
        self.assertEqual("CHEM322, STA322",student.view_courses("abojeedwin@gmail.com"))

    def test_that_student_can_view_course_facilitator(self):
        student = Student()
        facilitator = Facilitator()
        facilitator.register("Mr Franco", "franco@gmail.com", "Test12t@")
        facilitator.create_course("Statistics", "STA322", "Evans")
        student.register("Edwin", "Aboje", "abojeedwin@gmail.com", "Test123!")
        student.login("abojeedwin@gmail.com", "Test123!")
        student.register_course("STA322","Statistics","abojeedwin@gmail.com")
        self.assertEqual("Evans",student.view_course_instructor("Statistics"))



if __name__ == '__main__':
    unittest.main()
