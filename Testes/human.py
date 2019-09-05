import numpy as np
from PIL import ImageGrab
import cv2
import directKeys as dk


x1 = 340
y1 = 154
x2 = 341
y2 = 155

# verde 169
# azul 147
# vermelho 62

#75 219 106

while True:
    im = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    screen = np.array(im)
    if 75 in screen:
        dk.click()

"""while True:
    im = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    screen = np.array(im)

    if cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)[0][0] == 169:
        dk.click()
"""