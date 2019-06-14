import numpy as np
from PIL import ImageGrab
import cv2
import directKeys as dk
import time

x1 = 519
y1 = 500

clicou = False
for i in range(1000):
    time.sleep(0.1)
    #print(i)
    clicou = False
    im = ImageGrab.grab(bbox=(x1, y1, 823, 529))
    # im = ImageGrab.grab(bbox=(500, 160, 510, 170))
    screen = np.array(im)
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    y = 5
    x = len(screen[y]) - 1
    while not clicou:
        cor = screen[y][x]
        #print("Cor=" + str(cor) + " X=" + str(x) + " Y=" + str(y))
        if cor == 5:
            clicou = True
            xnovo = x1 + x
            ynovo = y1 + y
            dk.move(xnovo, ynovo)
            time.sleep(0.02)
            dk.hold()
            time.sleep(0.02)
            dk.release()
            #print("Clicou no 5")
        elif y == 0 and x == 0:
            break
        else:
            x -= 70
            if x < 0:
                x = 0
                break



