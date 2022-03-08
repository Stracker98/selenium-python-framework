from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest
from utilities.teststatus import TestStatus

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class LoginTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)


    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("stracker1998@gmail.com","mugil@1998")
        result1 = self.lp.verifiyLoginTitle()
        self.ts.mark(result1,"Title is verified")
        result2 = self.lp.verifyingLoginSuccessful()
        self.ts.markFinal("test_validLogin",result2,"login was successful")

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.logout()
        self.lp.login("stracker1998@gmail.com","mugil@1998")
        result = self.lp.verifyingLoginFailed()
        assert result == True

