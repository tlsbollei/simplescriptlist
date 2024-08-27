import pyautogui
import time
import subprocess
import re

time.sleep(2)

pyautogui.hotkey("win", "r")
time.sleep(1)

pyautogui.write("cmd")
pyautogui.hotkey("enter")
time.sleep(1)
command = "ipconfig"
pyautogui.write(command)
pyautogui.press("enter")
output = subprocess.check_output("ipconfig", text=True)
match = re.search(r"Ethernet adapter Ethernet:([\s\S]*?)(?=\n\S|$)", output)

if match:
    ethernet_info = match.group(0)
else:
    ethernet_info = "Ethernet adapter Ethernet not found."


pyautogui.alert(ethernet_info, "Ethernet Adapter Information")

pyautogui.write("exit")
pyautogui.hotkey("enter")