import os
import time
os.system('powershell -Command "Start-Process powershell -ArgumentList \'Set-ItemProperty -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\AppModelUnlock -Name AllowDevelopmentWithoutDevLicense -Value 1\' -Verb RunAs"')
time.sleep(5)
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Windows Application Driver"))
os.system(".\WinAppDriver.exe")