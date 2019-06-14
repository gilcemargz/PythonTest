import numpy as np
from PIL import ImageGrab
import cv2
import directKeys as dk
import time

x1 = 366
y1 = 400
x2 = 717
y2 = 401

print(dk.getpos())

"""x1 = 555
y1 = 268
x2 = 556
y2 = 269"""

velocidade = 0
cliques = 1
clicou = False
while True:
    im = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    # im = ImageGrab.grab(bbox=(500, 160, 510, 170))
    screen = np.array(im)
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    y = 0
    x = len(screen[y]) - 1
    if cliques % 100 == 0:
        velocidade += 5
    clicou = False
    while not clicou:
        cor = screen[y][x]
        # print("Cor=" + str(cor) + " X=" + str(x) + " Y=" + str(y))
        if cor == 100:
            clicou = True
            dk.move(x1 + x, y1 + round(velocidade))
            dk.hold()
            time.sleep(0.01)
            dk.release()
            cliques += 1
            # print("Clicou no 5")
        elif y == 0 and x == 0:
            break
        else:
            x -= 86
            if x < 0:
                x = 0
                break



