import screenshot
import controls
import pytesseract
import os
import time
import cv2
import numpy as np
import re

def calc_is_over(image):
    mean = np.mean(image, axis=0).mean(axis=0)

    if mean > 25:
        return True

    return False

def save_image(image):
    image.save(os.getcwd() + '/screenshot__' + str(int(time.time())) + '.png', 'PNG')

def process_image(image):
    image_array = np.array(image)
    processed_image = cv2.resize(image_array, (60, 45))
    processed_image = cv2.Canny(processed_image, threshold1=100, threshold2=200)

    return processed_image

class Game():
    def __init__(self, agent, game):
        self._agent = agent
        self._game = game

    def get_state(self):
        image = screenshot.grabGame().convert('L')
        score_image = image.crop((15, 25, 105, 50))

        # Get current score
        try:
            score_string = pytesseract.image_to_string(score_image)
            non_decimal = re.compile(r'[^\d]+')
            non_decimal.sub('', score_string)
            score = int(score_string)
        except ValueError:
            raise Exception("Cannot process score from screenshot")

        processed_image = process_image(image)

        reward = 0.1 * score / 10
        is_over = calc_is_over(processed_image)

        # if is crashed
        if False:
            is_over = True
            reward = -11/score

        return processed_image, reward, is_over

    def launch_game(self):
        """
        Open browser and visit cubefield
        """
        return

    def start_game(self):
        """
        Starts the game, expects to be on home screen
        """
        # needs to click on start button
        return

    def move_left(self):
        """
        Holds down left for given seconds
        """
        return

    def move_right(self):
        """
        Holds down right for given seconds
        """
        return

def main():
    game = Game(None, None)
    while True:
        time.sleep(0.25)
        print(game.get_state())

if __name__ == "__main__":
    main()
