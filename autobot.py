import pyautogui
import time
from datetime import datetime
import psutil
import os
import subprocess

meetingid = ("89174401762")
pswd = ("3pgcRm")

PROCNAME = "Zoom.exe"
for proc in psutil.process_iter():
    if proc.name() == PROCNAME:
        proc.kill()

time.sleep(1)

confTime = ('00:47:30')

#while True:
#    now = datetime.now().strftime("%H:%M:%S")
#    if now == confTime:
#        break
#    time.sleep(1)
#    print("Ожидание времени активации...")

print("Zoom launch...")

subprocess.Popen(
    ["C:\\Users\\flawent\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"],
    creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.CREATE_BREAKAWAY_FROM_JOB
)
time.sleep(2)

print("Looking for conference enter button...")
time.sleep(1)
enter_button1 = pyautogui.locateCenterOnScreen("enter_button1.png")
pyautogui.moveTo(enter_button1)
pyautogui.click()

time.sleep(3)
print("Entering the conference code...")
pyautogui.typewrite(meetingid)

print("Looking for ticks...")
time.sleep(1)
tick = pyautogui.locateCenterOnScreen("tick.png")
pyautogui.moveTo(tick)
pyautogui.click()
time.sleep(0.3)
tick = pyautogui.locateCenterOnScreen("tick.png")
pyautogui.moveTo(tick)
pyautogui.click()

print("Looking for second conference enter button...")
time.sleep(1)
enter_button2 = pyautogui.locateCenterOnScreen("enter_button2.png")
pyautogui.moveTo(enter_button2)
pyautogui.click()

print("Entering password...")
time.sleep(2)
pyautogui.typewrite(pswd)

print("Looking for the last conference enter button...")
time.sleep(1)
enter_button3 = pyautogui.locateCenterOnScreen("enter_button3.png")
pyautogui.moveTo(enter_button3)
pyautogui.click()

time.sleep(1)

try:
    x = pyautogui.locateCenterOnScreen("failed.png")

except Exception:
    print("Succesfully entered the conference!")
    input("Press Enter to continue...")
else:
    print("Error entering the conference...")
    input("Press Enter to continue...")