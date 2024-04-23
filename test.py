import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from config import *

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appActivity='.Settings',
    language='en',
    locale='US'
)

class TestAppium(unittest.TestCase):
    def function(self, first, second, action: str):
        if isinstance(first, list):
            for i in range(len(first)):
                self.driver.find_element(by=AppiumBy.XPATH, value=first[i]).click()
        else: self.driver.find_element(by=AppiumBy.XPATH, value=first).click()
        self.driver.find_element(by=AppiumBy.XPATH, value=action).click()

        if isinstance(second, list):
            for i in range(len(second)):
                self.driver.find_element(by=AppiumBy.XPATH, value=second[i]).click()
        else: self.driver.find_element(by=AppiumBy.XPATH, value=second).click()
        self.driver.find_element(by=AppiumBy.XPATH, value=equals).click()
    
    def clear(self):
        try:
            self.driver.find_element(by=AppiumBy.XPATH, value=clear).click()
        except:
            for _ in range(5):
                self.driver.find_element(by=AppiumBy.XPATH, value=delete).click()


    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_first(self):
        self.clear()
        self.function(number_1, number_4, plus)

    def test_second(self):
        self.clear()
        self.function([number_1, number_9, number_3], number_3, minus)
    
    def test_third(self):
        self.clear()
        self.function(number_9, [number_1, number_1], multiplication)

    def test_fourth(self):
        self.clear()
        self.function([number_1, number_4, number_4], number_7, division)

    def test_fifth(self):
        self.clear()
        self.function(number_2, number_0, division)
        
        
if __name__ == '__main__':
    unittest.main()