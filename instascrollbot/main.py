import pyautogui
import time
pyautogui.FAILSAFE = True  # Move mouse to top-left to stop script

time.sleep(2)
pyautogui.moveTo(100, 100)