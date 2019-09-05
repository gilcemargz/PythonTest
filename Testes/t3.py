import time
import pyautogui as dk
import math
import cv2
import numpy as np
from PIL import ImageGrab
import pytesseract

def ajustaNumero(numero):
    retorno = ''
    for x in numero:
        if(x in('0','1','2','3','4','5','6','7','8','9','-')):
            retorno = retorno+x

    return retorno

posicao = dk.position()
#print(posicao)
#exit()

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
posicaoAnterior = -1000
posicaoMinha = 0
ultimaOper = time.time()
while True:

    img = ImageGrab.grab(bbox=(30, 81, 296, 91))
    img.show()
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    posicaoMinha = pytesseract.image_to_string(img, config='--psm 7')
    print(posicaoMinha)
    exit()
    posicaoMinha = ajustaNumero(pytesseract.image_to_string(img, config='--psm 7'))

    if(posicaoMinha == ''):
        posicaoMinha = 0

    """img = ImageGrab.grab(bbox=(941, 189, 943, 191))
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    for y in range(0, len(img), 50):
        for x in range(0, len(img[y]), 50):
            cor = img[y][x]
            if (cor == 22):
                posicaoMinha = int(posicaoMinha) * -1"""

    img = ImageGrab.grab(bbox=(197, 217, 319, 247))
    #img.show()
    #exit()
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    modal = ajustaNumero(pytesseract.image_to_string(img, config='--psm 7'))

    try:
        modal = float(modal)
    except:
        print("Erro modal: "+modal+"hora"+time.strftime("%H:%M:%S"))
        continue

    objetivo = int(modal) / 50

    if(objetivo>0):
        objetivo=math.trunc((objetivo+1))
    else:
        objetivo=math.trunc((objetivo-1))


    posicaoMinha = int(posicaoMinha)

    #print("Anterior:" + str(posicaoAnterior))
    print("Posicao:" + str(posicaoMinha))
    #print("Modal:" + str(modal))
    print("Objetivo:" + str(objetivo))
    print("Diferenca:"+str(objetivo - posicaoMinha))

    if(posicaoMinha != objetivo):
        diferenca = objetivo - posicaoMinha

        if(time.time() - ultimaOper < 5):
            if(posicaoAnterior == posicaoMinha):
                continue

        dk.moveTo(1102,583)
        dk.doubleClick()
        dk.typewrite(str(diferenca))

        if(diferenca>0):
            #dk.moveTo(831, 172)
            dk.moveTo(1021, 642)
            dk.click()
            posicaoAnterior = posicaoMinha
            ultimaOper = time.time()
        else:
            #dk.moveTo(731, 172)
            dk.moveTo(1113, 639)
            dk.click()
            posicaoAnterior = posicaoMinha
            ultimaOper = time.time()
