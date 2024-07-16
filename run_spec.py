import os
import sys
import unittest
from windowStore import WindowsStoreUpdateTests
from windowsUpdate import windowsUpdate
from Edge import EdgeTests

def create_test_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(WindowsStoreUpdateTests))
    test_suite.addTest(unittest.makeSuite(windowsUpdate))
    test_suite.addTest(unittest.makeSuite(EdgeTests))
    return test_suite

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    suite = create_test_suite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == '__main__':
    main()