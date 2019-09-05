import numpy as np
from PIL import ImageGrab
import cv2
import directKeys as dk
import time

# Verde monstro 1 é 183

x1 = 600
y1 = 490
x2 = 1070
y2 = 500

clicou = False
while True:
    #time.sleep(0.1)
    clicou = False
    im = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    #im.show()
    screen = np.array(im)
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    y = len(screen)-1
    x = len(screen[y]) - 1
    while not clicou:
        cor = screen[y][x]
        #print("Cor=" + str(cor) + " X=" + str(x) + " Y=" + str(y))
        if cor == 183:
            clicou = True
            xnovo = 1010
            ynovo = 547
            dk.move(xnovo, ynovo)
            #time.sleep(0.02)
            dk.hold()
            #time.sleep(0.02)
            dk.release()
            print("Clicou")
        elif y == 0 and x == 0:
            break
        else:
            x -= 1
            if x < 0:
                x = 0
                break