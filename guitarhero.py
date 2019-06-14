import numpy as np
from PIL import ImageGrab
import cv2
import directKeys as dk
import time

xv1 = 424
yv1 = 400
xv2 = xv1+1
yv2 = yv1+1

xr1 = 533
yr1 = 400
xr2 = xr1+1
yr2 = yr1+1

xm1 = 664
ym1 = 438
xm2 = xm1+1
ym2 = ym1+1

xz1 = 790
yz1 = 445
xz2 = xz1+1
yz2 = yz1+1

imVer = ImageGrab.grab(bbox=(xv1, yv1, xv2, yv2))
imRed = ImageGrab.grab(bbox=(xr1, yr1, xr2, yr2))
imAma = ImageGrab.grab(bbox=(xm1, ym1, xm2, ym2))
imAzu = ImageGrab.grab(bbox=(xz1, yz1, xz2, yz2))
#im.show()

screenVer = cv2.cvtColor(np.array(imVer), cv2.COLOR_BGR2GRAY)
screenRed = cv2.cvtColor(np.array(imRed), cv2.COLOR_BGR2GRAY)
screenAma = cv2.cvtColor(np.array(imAma), cv2.COLOR_BGR2GRAY)
screenAzu = cv2.cvtColor(np.array(imAzu), cv2.COLOR_BGR2GRAY)

corVerdePadrao = screenVer[0][0]
corVermelhoPadrao = screenRed[0][0]
corAmareloPadrao = screenAma[0][0]
corAzulPadrao = screenAzu[0][0]

while True:
    dk.move(xv1,yv1)
    imVer = ImageGrab.grab(bbox=(xv1, yv1, xv2, yv2))
    imRed = ImageGrab.grab(bbox=(xr1, yr1, xr2, yr2))
#    imAma = ImageGrab.grab(bbox=(xm1, ym1, xm2, ym2))
#    imAzu = ImageGrab.grab(bbox=(xz1, yz1, xz2, yz2))
    #im.show()

    screenVer = cv2.cvtColor(np.array(imVer), cv2.COLOR_BGR2GRAY)
    screenRed = cv2.cvtColor(np.array(imRed), cv2.COLOR_BGR2GRAY)
#    screenAma = cv2.cvtColor(np.array(imAma), cv2.COLOR_BGR2GRAY)
#    screenAzu = cv2.cvtColor(np.array(imAzu), cv2.COLOR_BGR2GRAY)

    cor1 = screenVer[0][0]
    print(cor1)
    if cor1 != corVerdePadrao:
        print("Achou brano")
        dk.pressKey("a")
        time.sleep(0.1)

    cor2 = screenRed[0][0]
    print(cor2)
    if cor2 != corVermelhoPadrao:
        print("Achou brano")
        dk.pressKey("s")
        time.sleep(0.1)

    """cor3 = screenAma[0][0]
    print(cor3)
    if corAmareloPadrao == cor3:
        print("Achou brano")
        dk.pressKey("j")

    cor4 = screenAzu[0][0]
    print(cor4)
    if corAzulPadrao == cor4:
        print("Achou brano")
        dk.pressKey("k")"""



