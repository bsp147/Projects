#from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


while keyboard.is_pressed('q')==False:
    if pyautogui.pixel(485,700)[0] == 0:
        click(485,700)
    if pyautogui.pixel(610,700)[0] == 0:
        click(610,700)
    if pyautogui.pixel(739,700)[0] == 0:
        click(739,700)
    if pyautogui.pixel(852,700)[0] == 0:
        click(852,700)