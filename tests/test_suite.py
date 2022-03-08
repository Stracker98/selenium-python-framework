import unittest
from tests.home.login_tests import LoginTests
from tests.register_courses_csv_data import RegisterCoursesPage

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesPage)

smokeTest =unittest.TestSuite(tc1,tc2)
unittest.TextTestRunner(verbosity=2).run(smokeTest)