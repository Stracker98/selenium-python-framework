import os

from selenium import webdriver

class WebDriverFactory():
    def __init__(self,browser):
        """
        return:None
        """
        self.browser =browser
    """
        set chrome driver and iexplorer environment based on OS
        
        chromedriver = "c:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.chrome(chromedriver)
        PREFERRED: set path on the machine where browser wil be executed
    """
    def getWebDriverInstance(self):
       baseUrl = "https://courses.letskodeit.com/practice"
       if self.browser =="iexplorer":
            driver = webdriver.Ie()
       elif self.browser == "Chrome":
            driver = webdriver.Chrome()
       elif self.browser == "Firefox":
           chromedriver = "/Users/praga 98/Documents/workspace_personal/selenium/chromedriver"
           os.environ["webdriver.chrome.driver"] = chromedriver
           driver = webdriver.Firefox()
           driver.set_window_size(1366,768)
       else:
       driver.maximize_window()
       driver.implicitly_wait(3)
       driver.get(baseUrl)
       return driver


