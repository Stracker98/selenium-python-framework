from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import logging
from base.basepage import BasePage
import time

class NavigationPage(SeleniumDriver):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _all_courses = "All Courses"
    _my_courses = "My Courses"
    _practice = "practice"
    _user_settings_icon = "//*[@data-target='#navbar-inverse-collapse']"

    def navigateToAllCourses(self):
        self.ElementClick(locator=self._all_courses,locatorType="link")

    def navigateToMyCourses(self):
        self.ElementClick(locator=self._my_courses,locatorType="link")

    def navigateToPractice(self):
        self.ElementClick(locator=self._practice,locatorType="link")

    def navigateToUserSettings(self):
        userSettingsElement = self.waitForElement(locator=self._user_settings_icon,locatorType="xpath",pollFrequency =1)
        self.ElementClick(element=userSettingsElement)






