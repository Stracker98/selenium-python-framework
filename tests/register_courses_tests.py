import unittest
from pages.courses import register_courses_pages as RegisterCoursesPage
import pytest
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("oneTimeSetup","setUp")
class RegisterCourseTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self,oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.courses.enterCourseName("JavaScript")
        self.courses.selectCourseToEnroll("JavaScript for beginners")
        self.courses.enterCourse(num="10",exp="1220",cvv="10")
        result = self.courses.verifyEnrolledFailed
        self.ts.markFinal("test_invalidEnrollment",result,"Enrollment failed verification")
