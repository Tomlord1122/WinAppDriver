import os
import unittest
from windowStore import WindowsStoreUpdateTests
from windowsUpdate import windowsUpdate
from Edge import EdgeTests
import time
import threading


def create_test_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(EdgeTests))
    test_suite.addTest(unittest.makeSuite(WindowsStoreUpdateTests))
    test_suite.addTest(unittest.makeSuite(windowsUpdate))

    return test_suite


def run_winappdriver():
    time.sleep(2)
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Windows Application Driver"))
    os.system(".\WinAppDriver.exe")


def main():
    os.system('powershell -Command "Start-Process powershell -ArgumentList \'Set-ItemProperty -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\AppModelUnlock -Name AllowDevelopmentWithoutDevLicense -Value 1\' -Verb RunAs"')
    winappdriver_thread = threading.Thread(target=run_winappdriver)
    winappdriver_thread.start()
    time.sleep(2)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    suite = create_test_suite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    for i in range(10):
        print(f"Restarting computer in {10-i} seconds.")
        time.sleep(1)
    print("Restart computer.")
    os.system('powershell -Command "Start-Process powershell -ArgumentList \'Set-ItemProperty -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\AppModelUnlock -Name AllowDevelopmentWithoutDevLicense -Value 0\' -Verb RunAs"')
    time.sleep(2)
    os.system("shutdown /r /t 1")
    exit()
    


if __name__ == '__main__':
    main()
