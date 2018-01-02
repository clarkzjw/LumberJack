import time

import mss
import pyautogui as pg
from numpy import array, uint8
from pynput.keyboard import Key, Controller

keyboard = Controller()


def begin():
    pg.click(440, 900, 2)


TREE = uint8([56, 116, 161])

# from left to right
posY = [360, 460]
# from bottom to up
posX = [640, 540, 440, 340, 240, 140]


def is_tree(c1):
    if c1[0] == TREE[0] and c1[1] == TREE[1] and c1[2] == TREE[2]:
        return True
    else:
        return False


with mss.mss() as sct:
    screen = sct.monitors[1]
    screen["width"] = screen["width"] / 2.0
    begin()

    while True:
        img = array(sct.grab(screen))
        moves = list()
        left = [img[x, posY[0]] for x in posX]
        for i in range(6):
            if is_tree(left[i]):
                keyboard.press(Key.right)
                keyboard.release(Key.right)
                time.sleep(0.014)
                keyboard.press(Key.right)
                keyboard.release(Key.right)
            else:
                keyboard.press(Key.left)
                keyboard.release(Key.left)
                time.sleep(0.014)
                keyboard.press(Key.left)
                keyboard.release(Key.left)
        time.sleep(0.17)

