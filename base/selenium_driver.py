import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from traceback import print_stack
import utilities.custom_logger as cl
import logging

class SeleniumDriver():
    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        self.driver  = driver

    def screenShot(self,resultMessage):
        fileName = resultMessage + "." +str(round(time.time()*1000))+".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory,relativeFileName)
        destinationDirectory = os.path.join(currentDirectory,screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory:"+destinationFile)
        except:
            self.log.error("### Exception Occurred")
            print_stack()

    def getTitle(self):
        return self.driver.title

    def getBytype(self,locatorType):
        locatorType = locatorType.lower()
        if locatorType =="id":
            return By.ID
        elif locatorType =="xpath":
            return By.XPATH
        elif locatorType =="css":
            return By.CSS_SELECTOR
        elif locatorType =="class":
            return By.CLASS_NAME
        elif locatorType =="link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type"+locatorType+"not corrected/supported")
            return False

    def geteElement(self,locator,locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType  = self.getBytype(locatorType)
            element = self.driver.find_element(byType,locator)
            self.log.info("element is found with locator:"+locator+"and locatorType:"+locatorType )
        except:
            self.log.info("element is not found with locator:"+"locator+and locatorType:"+locatorType)

        return element

    def ElementClick(self,locator="",locatorType="id",element=None):
        try:
            if locator:
                element = self.geteElement(locator,locatorType)
            element.click()
            self.log.info("click on element with locator"+locator+"locatorType"+locatorType)
        except:
            self.log.info("cannot click on the element with locator"+locator+"locatorType"+locatorType)
            return element

    def getElmentList(self,locator,locatorType='id'):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getBytype(locatorType)
            element = self.drievr.find_element(byType,locator)
            self.log.info("Elememt list found with locator:"+locator+"and locatorType"+locatorType)
        except:
            self.log.info("Element list not found with locator:"+locator+"and locatorType:"+locatorType)

        return element



    def sendkeys(self,data,locator,locatorType="id"):
        try:
            if locator:
                element = self.geteElement(locator,locatorType)
            element.send_keys(data)
            self.log.info("send on element with locator"+locator+"locatorType"+locatorType)
        except:
            self.log.info("cannot send on the element with locator"+locator+"locatorType"+locatorType)
            print_stack()

    def getText(self,locator="",locatorType="id",element=None,info=""):
        try:
            if locator:
                self.log.debug("In locator condition")
                element = self.geteElement(locator,locatorType)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After fiding element,size is:"+str(len(text)))
            if len(text) ==0:
                text = element.get_attribute("inner text")
            if len(text) !=0:
                self.log.info("Getting text7 on element::"+info)
                self.log.info("The text is ::"+text+"'")
                text = text.strip()
        except:
            self.log.error("Failed to get an element:"+info)
            print_stack()
            text = None
        return text

    def isElementpresent(self,locator,locatorType="id"):
        try:
               if locator:
                   element = self.geteElement(locator, locatorType)
               if element is not None:
                   self.log.info("Element present with locator" + locator + "locatorType" + locatorType)
                   return True
               else:
                   self.log.info("Element not presnt with locator" + locator + "locatorType" + locatorType)
                   return False
        except:
            print("Element not found")
            return False

    def isElementDisplayed(self,locator="",locatorType="id",element=None):
        isDisplayed = False
        try:
            if locator:
                element = self.geteElement(locator,locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element displayed with locator:"+locator+"locatorType"+locatorType)
            else:
                self.log.info("Element not displayed with locator"+locator+"locatorType"+locatorType)
            return isDisplayed
        except:
            print("Element not found")
            return False

    def elementPresentCheck(self,locator,bytype):
        try:
            elementList = self.driver.find_elements(bytype)
            if len(elementList)>0:
                self.log.info("element found")
                return True
            else:
                self.log.info("element is not found")
                return False
        except:
            self.log.info("element is not found")
            return False

    def WaitForElement(self, locator, locatorType="id", timeout=10, pollout=0.5):
        element = None
        try:

            byType = self.getBytype("locatorType")
            self.log.info("waiting for maximum::" + str(timeout) + "::seconds for element to be visible")
            wait = WebDriverWait(self.driver, timeout=timeout,poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Sign In']")))
            self.log.info("element appeared on the web page")

        except:
            self.log.info("element not appeared on the web page")
            print_stack()

        return element

    def webScroll(self,direction="up"):

        if direction == "up":
            self.driver.execute_scripts("window.scrollBy(0,-400);")

        if direction =="down":
            self.driver.execute_scripts("window.scrollBy(0,600)")










