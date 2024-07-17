import unittest
from appium import webdriver
from time import sleep
from concurrent.futures import ThreadPoolExecutor, as_completed
from selenium.common.exceptions import TimeoutException, NoSuchElementException



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

    def test_windows_update(self):
        update_status = None
        self.driver.find_element_by_accessibility_id("SearchButton").click()
        self.driver.find_element_by_accessibility_id("SearchTextBox").send_keys("Check for updates")
        self.driver.find_element_by_accessibility_id("STCheck for updates").click()
        sleep(2)
        max_attempts = 1440
        for _ in range(max_attempts):
            self.driver.find_element_by_accessibility_id("SystemSettings_MusUpdate_UpdateActionButton3_Button").click()
            print("Checking for updates......")
            sleep(10)

            def check_element(name):
                try:
                    return self.driver.find_element_by_name(name).is_displayed()
                except (TimeoutException, NoSuchElementException):
                    return False

            elements_to_check = ["Download & install all", "installing", "Restart now", "You're up to date"]
            results = {}

            with ThreadPoolExecutor(max_workers=4) as executor:
                future_to_element = {executor.submit(check_element, name): name for name in elements_to_check}
                for future in as_completed(future_to_element):
                    element_name = future_to_element[future]
                    try:
                        results[element_name] = future.result()
                    except Exception as exc:
                        results[element_name] = False

            download_status = results.get("Download & install all", False)
            installing_status = results.get("installing", False)
            restart_status = not installing_status and results.get("Restart now", False)
            up_to_date_status = results.get("You're up to date", False)

            if download_status:
                self.driver.find_element_by_name("Download & install all").click()
                print("Downloading and installing updates......")
            elif installing_status:
                print("Waiting for installing updates......")
            elif restart_status or up_to_date_status:
                print("Updates Complete")
                update_status = "Complete"
                break

        if update_status == "Complete":
            print("Updates Complete, please restart your computer")
        else:
            self.assertIsNone(update_status, "Updates Failed")
        self.driver.find_element_by_accessibility_id("Close").click()
        sleep(1)
        
   
