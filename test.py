import os
import time
# 設置 UserAccountControlSettings 為永不通知（Windows 11）
print("Already set UserAccountControlSettings to never notify")
time.sleep(2)  # 等待設置生效

os.system('powershell -Command "Start-Process powershell -ArgumentList \'Set-ItemProperty -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\AppModelUnlock -Name AllowDevelopmentWithoutDevLicense -Value 1\' -Verb RunAs"')
time.sleep(5)
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Windows Application Driver"))
os.system(".\WinAppDriver.exe")