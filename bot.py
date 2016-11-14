import pyautogui as pg
from time import sleep


def move(_pos, _now):
    if _pos == 'left' and _now == 'left':
        pg.typewrite(['left'])
        pg.typewrite(['left'])
    elif _pos == 'left' and _now == 'right':
        pg.typewrite(['right'])
        pg.typewrite(['right'])
    elif _pos == 'right' and _now == 'right':
        pg.typewrite(['right'])
        pg.typewrite(['right'])
    elif _pos == 'right' and _now == 'left':
        pg.typewrite(['left'])
        pg.typewrite(['left'])

width, height = pg.size()
width *= 0.5
pg.moveTo(333, 600)
pg.click()

posY = [360, 260, 160]
posX = [276, 398]

q = ['left', 'left', 'left']

im = pg.screenshot(region=(0, 0, width, height))
l0 = im.getpixel((posX[0], posY[0]))
l1 = im.getpixel((posX[0], posY[1]))
l2 = im.getpixel((posX[0], posY[2]))

r0 = im.getpixel((posX[1], posY[0]))
r1 = im.getpixel((posX[1], posY[1]))
r2 = im.getpixel((posX[1], posY[2]))

if l0[0] == 161 and l0[1] == 116 and l0[2] == 56:
    q[0] = 'right'
    pos = 'right'
else:
    pos = 'left'
if l1[0] == 161 and l1[1] == 116 and l1[2] == 56:
    q[1] = 'right'
if l2[0] == 161 and l2[1] == 116 and l2[2] == 56:
    q[2] = 'right'

qlen = 3

while True:
    if qlen == 3:
        now = q[0]
        move(pos, now)
        now = q[1]
        move(pos, now)
        now = q[2]
        move(pos, now)
        qlen = 0
    elif qlen == 0:
        im = pg.screenshot(region=(0, 0, width, height))
        l0 = im.getpixel((posX[0], posY[0]))
        l1 = im.getpixel((posX[0], posY[1]))
        l2 = im.getpixel((posX[0], posY[2]))

        r0 = im.getpixel((posX[1], posY[0]))
        r1 = im.getpixel((posX[1], posY[1]))
        r2 = im.getpixel((posX[1], posY[2]))

        if l0[0] == 161 and l0[1] == 116 and l0[2] == 56:
            q[0] = 'right'
        else:
            q[0] = 'left'
        if l1[0] == 161 and l1[1] == 116 and l1[2] == 56:
            q[1] = 'right'
        else:
            q[1] = 'left'
        if l2[0] == 161 and l2[1] == 116 and l2[2] == 56:
            q[2] = 'right'
        else:
            q[2] = 'left'

        now = q[0]
        move(pos, now)
        now = q[1]
        move(pos, now)
        now = q[2]
        move(pos, now)

    sleep(0.095)
