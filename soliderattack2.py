import numpy as np
from PIL import ImageGrab
import cv2
import directKeys as dk
import time


x1 = 269
y1 = 78
x2 = 882
y2 = 551

#x1 = 270
#y1 = 170
#x2 = 280
#y2 = 180

posicao = dk.getpos()
print(posicao)

clicou = False
for i in range(2):
    #print(i)
    clicou = False
    im = ImageGrab.grab(bbox=(x1, y1, x2, y2))

    screen = np.array(im)
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

#    im.show()
#    for i in screen:
#        print(i)
#    break

    y = len(screen)-1
    x = len(screen[y]) - 1
    while not clicou:
        cor = screen[y][x]
        #print("Y é " + str(y)+ "X é "+str(x))
        #print("Cor=" + str(cor) + " X=" + str(x) + " Y=" + str(y))

        if cor in (71, 86, 93, 94, 183):
            #clicou = True
            xnovo = x1 + x
            ynovo = y1 + y
            dk.move(xnovo, ynovo)
            time.sleep(0.1)
            dk.click()

        if x == 0 and y != 0:
            y -= 5
            if y < 0:
                y = 0
            x = len(screen[y])-1
        elif y == 0 and x == 0:
            break
        else:
            x -= 5
            if x < 0:
                x = 0
