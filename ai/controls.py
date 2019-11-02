import pyautogui
import time

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = True

def moveMouse(x, y, duration=250):
    """
    Move a mouse to a given x, y coordinate
    """
    durationInSeconds = duration / 1000

    pyautogui.moveTo(x, y, durationInSeconds)

def click(x, y):
    return

def press(key, duration=None):
    """
    Presses key for an instant or for a duration in milliseconds if given
    """
    if duration == None or duration <= 0:
        pyautogui.click()
    else:
        durationInSeconds = duration / 1000

        pyautogui.keyDown(key)
        time.sleep(durationInSeconds)
        pyautogui.keyUp(key)

def main():
    moveMouse(325, 400)
    click(100, 200)
    press('left', 5000)

if __name__ == '__main__':
    main()
