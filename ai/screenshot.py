import os
import time
import screen
from PIL import ImageGrab

"""
Coordinates assume a screen resolution of 1080p and
game running in Chrome with zoom set to 100%
"""

GAME_HEIGHT = 600
GAME_WIDTH = 800
GAME_TARGET = (screen.X_PAD, screen.Y_PAD, screen.X_PAD + GAME_WIDTH, screen.Y_PAD + GAME_HEIGHT)

def screenshot(target=None):
    print("Screenshot: " + str(target))
    image = ImageGrab.grab(target)

    return image

def grabScreen(target=None):
    return screenshot(target)

def saveScreen(target=None):
    img = screenshot(target)
    img.save(os.getcwd() + '/screenshot__' + str(int(time.time())) + '.png', 'PNG')

def grabGame():
    return grabScreen(GAME_TARGET)

def saveGame():
    return saveScreen(GAME_TARGET)

def main():
    print(grabGame())

if __name__ == '__main__':
    main()
