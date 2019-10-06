import pyscreenshot
import os
import time
import screen

"""
Coordinates assume a screen resolution of 1080p and 
game running in Chrome with zoom set to 100%
"""

GAME_HEIGHT = 600
GAME_WIDTH = 800

def screenshot(target=None):
    print("Screenshot: " + str(target))
    img = pyscreenshot.grab(target)
    img.save(os.getcwd() + '/screenshot__' + str(int(time.time())) + '.png', 'PNG')

def screenshotGame():
    target = (screen.X_PAD, screen.Y_PAD, screen.X_PAD + GAME_WIDTH, screen.Y_PAD + GAME_HEIGHT)
    screenshot(target)

def main():
    screenshotGame()

if __name__ == '__main__':
    main()
