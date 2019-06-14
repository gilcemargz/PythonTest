import numpy as np
from PIL import ImageGrab
import cv2
import directKeys as dk
import time

x1 = 463
y1 = 293
x2 = 885
y2 = 714

"""x1 = 463
y1 = 293
x2 = 500
y2 = 300"""

# branco 255
# azul claro 147

fotos = []

"""for i in range(4):
    time.sleep(0.1)
    im = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    screen = np.array(im)
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    #im.show()
    fotos.insert(i-1, screen)

for i in fotos:
    for y in range(len(i)):
        for x in range(len(i[y])):
            cor = i[y][x]
            if cor == 255:
                screen = i
                break"""

print("Uma passagem inicio")
im = ImageGrab.grab(bbox=(x1, y1, x2, y2))
screen = np.array(im)
screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
print("Uma passagem fim")

def procuraFoto():
    print("Procurando")
    #time.sleep(0.1)
    im = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    screen = np.array(im)
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    print(len(screen))

    for y in range(0, len(screen), 50):
        for x in range(0, len(screen[y]), 50):
            cor = screen[y][x]
            if cor == 255:
                print("Achou")
                time.sleep(5)
                clicar(screen)

    return False


def clicar(screen):
    print(len(screen))
    for y in range(0, len(screen), 10):
        for x in range(0, len(screen[y]), 10):
            cor = screen[y][x]
            if cor == 255:
                xNovo = x1 + x
                yNovo = y1 + y
                dk.move(xNovo, yNovo)
                dk.click()

primeira = True
while True:
    if primeira:
        time.sleep(0.1)
        primeira = False
    else:
        time.sleep(1)
    achou = False
    while not achou:
        print("Searchin")
        achou = procuraFoto()

