from src.course_management_system.course import Course
class Courses:
    def __init__(self):
        self.courses : list[Course] = []

    def add(self, course_title: str, course_code: str, course_facilitator: str) -> None:
        from src.course_management_system.facilitators import Facilitators
        facilitators = Facilitators()
        course : Course = facilitators.create_course(course_title, course_code, course_facilitator)
        self.courses.append(course)

    def find_course_in_courses_by(self, course_facilitator: str) -> Course:
        from src.course_management_system.facilitators import Facilitators
        facilitators = Facilitators()
        for course in self.courses:
            if course == facilitators.find_course_by_facilitator(course_facilitator):
                return course

    def remove_course_from_courses(self, course_code: str, course_facilitator: str) -> None:
        from src.course_management_system.facilitators import Facilitators
        facilitators = Facilitators()
        for course in self.courses:
            if course.get_course_code() == course_code and course == facilitators.find_course_by_facilitator(course_facilitator):
                self.courses.remove(course)

    def view_courses(self):
        return self.courses.__str__()