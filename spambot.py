import time
import pyautogui

def VictorBot():
    time.sleep(5)

    text=open('SpamMessage.txt')
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press('enter')

VictorBot()