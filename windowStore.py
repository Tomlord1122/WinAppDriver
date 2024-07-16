import unittest
from appium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException

class WindowsStoreUpdateTests(unittest.TestCase):
    @classmethod  
    def setUpClass(cls) -> None:
        # setup Appium driver
        desired_caps = dict()
        desired_caps["app"] = "Microsoft.WindowsStore_8wekyb3d8bbwe!App"
        cls.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities=desired_caps
        )
        cls.driver.implicitly_wait(3) # wait for 3 seconds

    @classmethod
    def tearDownClass(cls) -> None:
        # turn off Appium driver
        cls.driver.quit()
    
    def test_update_apps(self):
        max_attempts = 720 
        update_status = None
        self.driver.find_element_by_name("Library. Updates available").click()
        self.driver.find_element_by_name("Get updates").click()
        for _ in range(max_attempts): # 720 * 10 = 7200 seconds = 2 hours, Try updating for 2 hours
            sleep(10)
            try:
                update = self.driver.find_element_by_name("Your apps and games are up to date").is_displayed()
                update_status = "up_to_date."
                if update:
                    break
            except NoSuchElementException:
                print("Update status element not found, continuing to check...")
                continue
        if update_status is None:
            self.fail("Update check timed out")
        self.assertIsNotNone(update_status, "Can't determine the update status of Microsoft Store")
        
