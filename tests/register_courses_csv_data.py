import time
import unittest
from pages.courses import register_courses_pages as RegisterCoursesPage
import pytest
from utilities.teststatus import TestStatus
from ddt import ddt,data,unpack
from utilities.read_data import getCSVData
from pages.home.navigation_page import NavigationPage


@pytest.mark.usefixtures("oneTimeSetup","setUp")
@ddt
class RegisterCourseTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self,oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.naviGateToUserSettings()

    @pytest.mark.run(order=1)
    @data(*getCSVData("/Users/praga 98/workspace_python/letskodeit/testdata.csv"))
    @unpack
    def test_invalidEnrollment(self,courseName,ccNum,ccExp,ccCVV):
        self.courses.enterCourseName(courseName)
        time.sleep(1)
        self.courses.selectCourseToEnroll(courseName)
        time.sleep(1)
        self.courses.enterCourse(num=ccNum,exp=ccExp,cvv=ccCVV)
        time.sleep(1)
        result = self.courses.verifyEnrolledFailed
        self.ts.markFinal("test_invalidEnrollment",result,"Enrollment failed verification")
        self.driver.find_element_by_link_text("All Courses").click()
