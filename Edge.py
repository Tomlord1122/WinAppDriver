import unittest
from appium import webdriver
from time import sleep
from concurrent.futures import ThreadPoolExecutor, as_completed
from selenium.common.exceptions import TimeoutException, NoSuchElementException


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
        sleep(3)
        self.driver.find_element_by_name("Settings and more (Alt+F)").click()
        sleep(0.5)
        self.driver.find_element_by_name("Settings").click()
        sleep(0.5)
        self.driver.find_element_by_name("About Microsoft Edge").click()
        sleep(0.5)
        for _ in range(max_attempts):

            def check_element(name):
                try:
                    return self.driver.find_element_by_name(name).is_displayed()
                except (TimeoutException, NoSuchElementException):
                    return False
            elements_to_check = ["Microsoft Edge is up to date.", "Download and install", "Restart"]
            results = {}
            
            with ThreadPoolExecutor(max_workers=3) as executor:
                future_to_element = {executor.submit(check_element, name): name for name in elements_to_check}
                for future in as_completed(future_to_element):
                    name = future_to_element[future]
                    try:
                        results[name] = future.result()
                    except Exception as exc:
                        results[name] = False
                        print(f"An exception occurred: {exc}")
            edge_update_status = results.get("Microsoft Edge is up to date.", False)
            download_status = results.get("Download and install", False)
            restart_status = results.get("Restart", False)

            if edge_update_status:
                print("Microsoft Edge is up to date.")
                update_status = "up_to_date"
                break
            elif download_status:
                self.driver.find_element_by_name("Download and install").click()
                print("Downloading and installing the update...")
            elif restart_status:
                self.driver.find_element_by_name("Restart").click()
                print("Restarting to complete the update...")
                update_status = "restarted"
                break
        
            sleep(10)
        
        if update_status is None:
            self.fail("Update check timed out")
        else:
            print(f"Update status: {update_status}")
        
        self.assertIsNotNone(update_status, "Can't determine the update status of Edge")
        sleep(1)
        
   
