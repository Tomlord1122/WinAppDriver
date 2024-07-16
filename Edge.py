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
        try:
            # Try to click the search button
            self.driver.find_element_by_accessibility_id("SearchButton").click()
            
            # Try to enter "Edge" in the search box
            self.driver.find_element_by_accessibility_id("SearchTextBox").send_keys("Edge")
            
            # Try to click the Microsoft Edge icon
            self.driver.find_element_by_accessibility_id("PPMicrosoft Edge").click()
        except NoSuchElementException as e:
            print(f"Can't find the element: {e.msg}")
            self.fail("Test failed: Can't find the element")
        finally:
            print(f"Function: {self.test_open_edge.__name__} finished")
            pass
    
    def test_update_edge(self):
        max_attempts = 240  # Set the maximum number of attempts to check the update status
        update_status = None
        self.driver.find_element_by_name("Settings and more (Alt+F)").click()
        self.driver.find_element_by_name("Settings").click()
        self.driver.find_element_by_name("About Microsoft Edge").click()
        
        for _ in range(max_attempts):
            try:
                if self.driver.find_element_by_name("Microsoft Edge is up to date.").is_displayed():
                    print("Microsoft Edge is up to date.")
                    update_status = "up_to_date"
                    break
                elif self.driver.find_element_by_name("Download and install").is_displayed():
                    self.driver.find_element_by_name("Download and install").click()
                    print("Downloading and installing the update...")
                elif self.driver.find_element_by_name("Restart").is_displayed():
                    self.driver.find_element_by_name("Restart").click()
                    print("Restarting to complete the update...")
                    update_status = "restarted"
                    break
            except NoSuchElementException as e:
                print(f"Can't find the element: {e.msg}, continue checking...")
            
            sleep(1)
        
        if update_status is None:
            self.fail("Update check timed out")
        
        self.assertIsNotNone(update_status, "Can't determine the update status of Edge")
        
   
