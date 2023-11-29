'''

import pyautogui
pyautogui.displayMousePosition()

'''

from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import win32api, win32con

time.sleep()

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event((win32con.MOUSEEVENTF_LEFTUP,0,0))

    click(200,500)

#check if the pixel in the coord is red
if pyautogui.pixel(818,1011) [0] == 232:
    click (818,1011)

    #if a specific button shows up
if pyautogui.locateOnScreen('ready_for_start.png', grayscale= True, confidence=0.8) != None:
    #found button
    click(200,100)