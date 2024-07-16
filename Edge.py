import unittest
from appium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException

class EdgeTests(unittest.TestCase):
    @classmethod  
    def setUpClass(cls) -> None:
        desired_caps = dict()
        desired_caps["app"] = "Root"
        # desired_caps["platformName"] = "Windows"
        # desired_caps["deviceName"] = "WindowsPC"
        cls.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities=desired_caps
            )
        cls.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_open_edge(self):
        self.driver.find_element_by_accessibility_id("SearchButton").click()
        self.driver.find_element_by_accessibility_id("SearchTextBox").send_keys("Edge")
        self.driver.find_element_by_accessibility_id("PPMicrosoft Edge").click()
        # sleep(3)  
    
    def test_update_edge(self):
        self.driver.find_element_by_name("Settings and more (Alt+F)").click()
        self.driver.find_element_by_name("Settings").click()
        self.driver.find_element_by_name("About Microsoft Edge").click()
        while True:
            try:
                if self.driver.find_element_by_name("Microsoft Edge is up to date.").is_displayed():
                    print("Microsoft Edge is up to date.")
                    break
                elif self.driver.find_element_by_name("Download and install").is_displayed():
                    self.driver.find_element_by_name("Download and install").click()
                
                elif self.driver.find_element_by_name("Restart").is_displayed():
                    self.driver.find_element_by_name("Restart").click()
                    break
                else:
                    sleep(1)
            except NoSuchElementException:
                print("Element not found, continuing to check...")
                sleep(1)
    
   
