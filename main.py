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
import sys

time.sleep(0.2)

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event((win32con.MOUSEEVENTF_LEFTUP,0,0))

print("Press Enter to continue or press Esc to exit: ")
while True:
    try:
        if keyboard.is_pressed('ENTER'):
            break
        if keyboard.is_pressed('Esc'):
            print("\nyou pressed Esc, so exiting...")
            sys.exit(0)
    except:
        break



print("\nPress 1 to search for a known prompt \nPress 2 to write a new prompt")
while True:
    try:
        if keyboard.is_pressed('1'):
            # Open the file in read mode
            file = open('prompts.txt', 'r')
            # Set the read position to the desired location (e.g., 10th character)
            file.seek(10)
            # Read the content from the new position
            content = file.read()
            # Print the content
            print("Content:", content)
            # Close the file
            file.close()
            break
        #if keyboard.is_pressed('2'):
    except:
        break


'''
#check if key is pressed
while keyboard.is_pressed('Esc') == False:




    pyautogui.keyDown('1')
    time.sleep(0.1)
    pyautogui.keyUp('1')
    #check if the pixel in the coord is red
    if pyautogui.pixel(818,1011) [0] == 232:
        click (818,1011)

    #if a specific button shows up
    if pyautogui.locateOnScreen('ready_for_start.png', grayscale= True, confidence=0.8) != None:
        #found button
        click(200,100)
'''