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
        self.driver.find_element_by_name("Library. Updates available").click()
        self.driver.find_element_by_name("Get updates").click()
        while True:
            sleep(10)
            try:
                update_status = self.driver.find_element_by_name("Your apps and games are up to date").is_displayed()
                print(update_status)
                if update_status:
                    break
            except NoSuchElementException:
                print("Update status element not found, continuing to check...")
                continue
       
