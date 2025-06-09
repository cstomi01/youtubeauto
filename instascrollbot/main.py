import pyautogui
import time

pyautogui.FAILSAFE = True  # Move mouse to top-left to stop the script

#how many times it should drag slider down:
dragcount = 250
#how many times it should wait between slide down.:
slidewait = 1.5

# Configurable delay to switch to Chrome
print("You have 5 seconds to switch to Chrome...")
time.sleep(5)

# Adjust these based on your screen resolution and browser layout
# This assumes scrollbar is on the right side
scrollbar_x = 1449  # Change if your screen width is different
scrollbar_y_top = 565
scrollbar_y_bottom = 580

# Scroll down multiple times
for i in range(dragcount):
    print(f"Scroll {i + 1}/{dragcount}")
    pyautogui.moveTo(scrollbar_x, scrollbar_y_top, duration=0.2)
    pyautogui.dragTo(scrollbar_x, scrollbar_y_bottom, duration=0.3)
    time.sleep(slidewait)  # Wait for new comments to load
