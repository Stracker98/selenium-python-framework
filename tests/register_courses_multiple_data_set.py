import unittest
from pages.courses import register_courses_pages as RegisterCoursesPage
import pytest
from utilities.teststatus import TestStatus
from ddt import ddt,data,unpack


@pytest.mark.usefixtures("oneTimeSetup","setUp")
@ddt
class RegisterCourseTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self,oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners","10","1220","10"),("Learn Python 3  from scratch","20","1200","20"))
    @unpack
    def test_invalidEnrollment(self,courseName,ccNum,ccExp,ccCVV):
        self.courses.enterCourseName(courseName)
        self.courses.selectCourseToEnroll(courseName)
        self.courses.enterCourse(num=ccNum,exp=ccExp,cvv=ccCVV)
        result = self.courses.verifyEnrolledFailed
        self.ts.markFinal("test_invalidEnrollment",result,"Enrollment failed verification")
        self.driver.find_element_by_link_text("All Courses")
