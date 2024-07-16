import os
import unittest
from windowStore import WindowsStoreUpdateTests
from windowsUpdate import windowsUpdate
from Edge import EdgeTests
import time
def create_test_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(EdgeTests))
    test_suite.addTest(unittest.makeSuite(WindowsStoreUpdateTests))
    test_suite.addTest(unittest.makeSuite(windowsUpdate))
    return test_suite

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    suite = create_test_suite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    time.sleep(3)
    for i in range(3):
        print(f"Restarting computer in {3-i} seconds.")
        time.sleep(1)
    print("Restarting computer.")
    os.system("shutdown /r /t 1")
    

if __name__ == '__main__':
    main()
    
    