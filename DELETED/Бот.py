import pyautogui as p
import time

# -------------MAIN----------------------------

p.click(220, 755)
p.click(100, 10)
p.click(200, 50)
p.hotkey("ctrl", "a")
p.hotkey("del")
p.typewrite("https://speechpad.ru/")
p.hotkey("enter")


p.click(170, 755)
time.sleep(.9)
p.click(170, 300)
line = r"cd C:\Users\stepa\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.7\Python\VoiceHelper"
p.typewrite(line)
p.hotkey("enter")
p.typewrite("notepad Listen.txt")
p.hotkey("enter")
time.sleep(.1)
p.click(100, 350)
p.click(375, 245)
p.click(300, 755)
p.click(300, 500)