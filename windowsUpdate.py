import unittest
from appium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException

class windowsUpdate(unittest.TestCase):
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
        self.driver.find_element_by_accessibility_id("SearchTextBox").send_keys("Check for updates")
        self.driver.find_element_by_accessibility_id("STCheck for updates").click()
        sleep(1)  
    
        # check for updates
        try:
            update_status = self.driver.find_element_by_name("Check for updates").is_displayed()
            if update_status:
                self.driver.find_element_by_name("Check for updates").click()
                while True:
                    sleep(1)
                    if self.driver.find_element_by_name("Download & install all").is_displayed():
                        self.driver.find_element_by_name("Download & install all").click()
                    elif self.driver.find_element_by_name("installing").is_displayed():
                        print("Wait for installing updates......")
                        break
        except NoSuchElementException:
            sleep(1)
            print("No updates found")
        finally:
            print("Close the update window")
            self.driver.find_element_by_accessibility_id("Close").click()

    
    
   
