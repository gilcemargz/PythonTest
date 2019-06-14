import numpy as np
from PIL import ImageGrab
import cv2
import directKeys as dk
import time

x1 = 519
y1 = 500

clicou = False
for i in range(1000):
    time.sleep(0.3)
    #print(i)
    clicou = False
    im = ImageGrab.grab(bbox=(x1, y1, 823, 529))
    # im = ImageGrab.grab(bbox=(500, 160, 510, 170))
    screen = np.array(im)
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    x = len(screen) - 1
    y = len(screen[x]) - 1
    while not clicou:
        cor = screen[x][y]
        #print("Cor=" + str(cor) + " X=" + str(x) + " Y=" + str(y))
        if cor == 5:
            clicou = True
            dk.move(x1 + y, y1+x)
            #time.sleep(0.3)
            dk.click()
            #print("Clicou no 5")
        elif y == 0 and x != 0:
            x -= 100
            if x < 0:
                x = 0
            y = len(screen[x])-1
        elif y == 0 and x == 0:
            break
        else:
            y -= 100
            if y < 0:
                y = 0



