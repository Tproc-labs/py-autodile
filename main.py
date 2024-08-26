#Open DesMuMe make sure you are on a 1080 1920x1080 monitor and maximised
#Or this will fail, code was made for me, not for you :)
# importing modules
import pyautogui
import pygetwindow as gw
import pyautogui as pos
import pydirectinput as py
import time

dile_pixel="x=972, y=295"
dile_default_color="(206, 66, 33)"

from mouseinfo import position
from pyscreeze import pixel

#Bring Des into focus
win = gw.getWindowsWithTitle('DesMuMe')[0]
win.activate()

Debug = False
if Debug:
    while True:
        shot=pyautogui.screenshot()
        px=shot.getpixel(pos.position())
        print("Position->",pos.position(), "Colour->",px)
        time.sleep(1)

while True:
    #Move to file tab and hover
    py.moveTo(10, 32, duration = 0)
    py.click()
    #Move to reset to restart the game
    py.moveTo(134, 540, duration = 0)
    #Click to restart
    py.click()
    #wait for reset
    time.sleep(7.4)
    #Skip movie
    py.press('Enter')
    #enter menu
    time.sleep(1.4) #there is a delay before input
    py.press('enter')
    #in main menu press A. (my keybind is X)
    time.sleep(2.9)
    py.press('x')
    #look at the pokeballs
    time.sleep(2.8)
    py.press('x')
    #turn to the dile!
    time.sleep(2.5)
    py.press('right')
    #chekc the dile
    #py.moveTo(970, 295, duration=0)
    #temp offset
    py.moveTo(970, 305, duration=0)
    time.sleep(0.5)
    screenshot = pyautogui.screenshot()
    pixelcheck = screenshot.getpixel(pos.position())
    pixstring = str(pixelcheck)
    print(pixstring, "(206, 66, 33) is default")
    if pixstring == "(206, 66, 33)":
        print("Default Dile")
    else:
        print("SHINY BREAK BREAK BREAK!!!!!")
        break
