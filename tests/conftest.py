import pytest
from selenium import webdriver
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage

@pytest.fixture()
def setUp():
    print("Running method level setup")
    yield
    print("Running method level teardown")
@pytest.fixture(scope='class')
def oneTimeSetUp(request,browser):
        print("Running one time setup")
        wdf = WebDriverFactory(browser)
        driver = wdf.getWebdriverInstance()
        lp = LoginPage(driver)
        lp.login("stracker@gmail.com","mugil@1998")

        if request.cls is not None:
            request.cls.driver = driver

        yield driver
       # driver.quit()
        print("Running one time teardown")



def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType",help="Type of operating system" )

@pytest.fixture(scope='module')
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope='session')
def Ostype(request):
    return request.config.getoption("--ostype")

