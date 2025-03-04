import unittest
from src.course_management_system.student import Student


class MyTestCase(unittest.TestCase):
    def test_that_student_can_register(self):
        student = Student()
        student.register("Edwin","Aboje","abojeedwin@gmail.com","Test123!")
        self.assertEqual("Edwin Aboje", student.get_name())




if __name__ == '__main__':
    unittest.main()
