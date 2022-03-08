import time
from pages.home.navigation_page import NavigationPage
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import logging
from base.basepage import BasePage

class LoginPage(SeleniumDriver):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    #locators
    _login_link = "//a[text()='Sign In']"
    _email_field = "email"
    _password_field = "password"
    _login_btn = "//input[@value='Login']"



    def clickloginLink(self):
        self.ElementClick(self._login_link,locatorType="xpath")

    def enterEmail(self,email):
        self.sendkeys(email,self._email_field)

    def enterPassword(self,password):
        self.sendkeys(password,self._password_field)

    def clickLoginBtn(self):
        self.ElementClick(self._login_btn,locatorType="xpath")

    def login(self,email="",password=""):
        self.clickloginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginBtn()

    def verifyingLoginSuccessful(self):
        result = self.isElementpresent("//*[@data-target='#navbar-inverse-collapse']",locatorType='xpath')
        return result

    def verifyingLoginSuccessful(self):
        result = self.isElementpresent("//span[@class='dynamic-text help-block']", locatorType='xpath')
        return result

    def verifiyLoginTitle(self):
        return self.verifyPageTitle("Let's Kode It")

    def logout(self):
        self.nav.navigateToUserSettings()
        logoutLinkElement = self.waitForElement(locator="//a[text()='Logout']",locatorType="xpath",pollFrequency = 1)
        self.ElementClick(logoutLinkElement)

