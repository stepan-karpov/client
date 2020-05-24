# coding: utf-8
import pyautogui as p
import time
time.sleep(3)
while 1:
    print("IN")
    p.hotkey("ctrl", "s")
    p.hotkey("ctrl", 'a')
    p.hotkey('del')
    p.keyUp
    f = open('Listen.txt', mode='r', encoding='utf-8')
    content = f.read()
    if content != "":
        content = content.strip(' ')
        print(content)
    f.close()
    time.sleep(.5)