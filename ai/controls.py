import pyautogui

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = True

def moveMouse(x, y, duration=0.25):
    pyautogui.moveTo(x, y, duration)

def click():
    pyautogui.click()

def press(key):
    pyautogui.press(key)

def main():
    moveMouse(325, 400)
    click()
    press('left')

if __name__ == '__main__':
    main()
