import pyscreenshot
import os
import time

"""
Coordinates assume a screen resolution of 1080p and 
game running in Chrome with zoom set to 100%
"""

X_PAD = 10
Y_PAD = 135
GAME_HEIGHT = 600
GAME_WIDTH = 800

def screenshot(target=None):
    img = pyscreenshot.grab(target)
    img.save(os.getcwd() + '/screenshot__' + str(int(time.time())) + '.png', 'PNG')

def screenshotGame():
    target = (X_PAD, Y_PAD, X_PAD + GAME_WIDTH, Y_PAD + GAME_HEIGHT)
    screenshot(target)

def main():
    screenshot()

if __name__ == '__main__':
    main()
