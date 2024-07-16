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
        update_status = None
        try:
            # Open the update window
            self.driver.find_element_by_accessibility_id("SearchButton").click()
            self.driver.find_element_by_accessibility_id("SearchTextBox").send_keys("Check for updates")
            self.driver.find_element_by_accessibility_id("STCheck for updates").click()
            sleep(2)

            # Check for updates
            max_attempts = 1440
            for _ in range(max_attempts):
                try:
                    if self.driver.find_element_by_name("Check for updates").is_displayed():
                        self.driver.find_element_by_name("Check for updates").click()
                        print("Checking for updates......")
                    elif self.driver.find_element_by_name("Download & install all").is_displayed():
                        self.driver.find_element_by_name("Download & install all").click()
                        print("Downloading and installing updates......")
                    elif self.driver.find_element_by_name("installing").is_displayed():
                        print("Waiting for installing updates......")
                    elif not self.driver.find_element_by_name("installing").is_displayed() and self.driver.find_element_by_name("Restart").is_displayed():
                        print("Updates Complete")
                        update_status = "Complete"
                        break
                except NoSuchElementException:
                    print("Waiting for updates status......")
                sleep(10)
            if update_status == "Complete":
                print("Updates Complete, please restart your computer")
            else:
                self.assertIsNone(update_status, "Updates Failed")
        except NoSuchElementException:
            print("No updates found")
        finally:
            self.driver.find_element_by_accessibility_id("Close").click()
            
            
   
