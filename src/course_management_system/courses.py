from src.course_management_system.course import Course
class Courses:
    def __init__(self):
        self._courses : list[Course] = []

    def add(self, course_title: str, course_code: str, course_facilitator: str) -> None:
        self._courses.append(Course(course_title, course_code, course_facilitator))

    def find_course_in_courses_by(self, course_facilitator: str) -> Course:
        for course in self._courses:
            if course.get_course_facilitator() == course_facilitator:
                return course

    def remove_course_from_courses(self, course_code: str, course_facilitator: str) -> None:
        from src.course_management_system.facilitator import Facilitator
        facilitators = Facilitator()
        for course in self._courses:
            if course.get_course_code() == course_code and course == facilitators.find_course_by_facilitator(course_facilitator):
                self._courses.remove(course)

    def view_courses(self):
        return self._courses.__str__()