import time
import re
import time
import pyautogui as dk
import math
import string
import numpy as np
from PIL import ImageGrab
import cv2
import pytesseract

from collections import defaultdict
import string
_NoneType = type(None)

def keeper(keep):
    table = defaultdict(_NoneType)
    table.update({ord(c): c for c in keep})
    return table

digit_keeper = keeper('-+0123456789')

import string

class Del:
  def __init__(self, keep="0123456789-"):
    self.comp = dict((ord(c),c) for c in keep)
  def __getitem__(self, k):
    return self.comp.get(k)

def ajustaNumero(numero):
    retorno = ''
    for x in numero:
        if(x in('0','1','2','3','4','5','6','7','8','9','-')):
            retorno = retorno+x

    return retorno

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

posicao = dk.position()
#print(posicao)
#exit()


"""
x1 = 1320
y1 = 545
x2 = x1 + 35
y2 = y1 + 15

posicao = dk.position()
print(posicao)


while True:
    img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    doubleX = (x2 - x1) * 2
    doubleY = (y2 - y1) * 2
    img = img.resize((doubleX, doubleY))
    #img.show()
    img = np.array(img)
    img = ~img
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    result = pytesseract.image_to_string(img, config='--psm 7')
    #result = result.translate(Del())
    print("Resultado: "+result)



x1 = 259
y1 = 145
x2 = x1+52
y2 = y1+15

#while True:
    img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    #img.show()
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    result = pytesseract.image_to_string(img,config='--psm 7')
    result = result.translate(Del())
    print("Resultado: "+result)
"""


"""while True:
    Posx1 = 1320
    Posy1 = 545
    Posx2 = Posx1 + 35
    Posy2 = Posy1 + 15

    Posx1 = 716
    Posy1 = 428
    Posx2 = 803
    Posy2 = 511

    img = ImageGrab.grab(bbox=(Posx1, Posy1, Posx2, Posy2))
    #img.show()
    doubleX = (Posx2 - Posx1) * 1
    doubleY = (Posy2 - Posy1) * 1
    img = img.resize((doubleX, doubleY))
    img = np.array(img)
    #img = ~img
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    cv2.imwrite("D:\\posicao.png", img)
    posicaoMinha = pytesseract.image_to_string(img, config='--psm 7')
    #posicaoMinha.translate(digit_keeper)
    posicaoMinha.translate(Del())
    print("Posição: "+posicaoMinha)
"""
posicaoAnterior = -1000
posicaoMinha = 0
ultimaOper = time.time()
while True:
    try:
        f = open("C:\\Users\\Gilce\\AppData\\Roaming\\MetaQuotes\\Terminal\\D0E8209F77C8CF37AD8BF550E51FF075\\MQL5\\Files\\teste.txt", "r")
        valor = f.readline()
        f.close()
        posicaoMinha = (valor[2:10])
        posicaoMinha = ajustaNumero(posicaoMinha)
        #print(posicaoMinha)
    except:
        print("Deu erro posição:  "+str(posicaoMinha)+"  hora"+time.strftime("%H:%M:%S"))
        posicaoMinha = ''
        posicaoAnterior = -1000

    print("Pos:"+str(posicaoMinha))
    #exit()
    if(posicaoMinha == ''):
        continue

    Modalx1 = 355
    Modaly1 = 141
    Modalx2 = 428
    Modaly2 = 162

    img = ImageGrab.grab(bbox=(Modalx1, Modaly1, Modalx2, Modaly2))
    #img.show()
    #exit()
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    modal = pytesseract.image_to_string(img, config='--psm 7')
    #print("Modal Antes: "+modal)
    modal = ajustaNumero(modal)
    #modal = modal.translate(Del())
    #print("Modal: "+modal)

    #print("Modal:"+str(modal))
    #print("Posicao:"+str(posicaoMinha))

    try:
        modal = float(modal)
    except:
        print("Erro modal: "+modal+"hora"+time.strftime("%H:%M:%S"))
        continue

    objetivo = int(modal) /10
    if(objetivo>0):
        objetivo=objetivo+1
    else:
        objetivo=objetivo-1

    objetivo = math.trunc(objetivo)*-1

    posicaoMinha = int(posicaoMinha)

    if(posicaoMinha != objetivo):
        diferenca = objetivo - posicaoMinha

        #if(diferenca==posicaoMinha*2):
        print("Modal:"+str(modal))
        print("Posicao:"+str(posicaoMinha))
        print("Dif:"+str(diferenca))
        print("Objetivo:"+str(objetivo))
        print(str(posicaoAnterior))
        print(str(posicaoMinha))
        print(time.time()-ultimaOper)
        if(time.time() - ultimaOper < 2):
            if(posicaoAnterior == posicaoMinha):
                continue

        dk.moveTo(802,510)
        dk.doubleClick()
        dk.typewrite(str(diferenca))

        if(diferenca>0):
            #dk.moveTo(831, 172)
            dk.moveTo(876, 533)
            dk.click()
            posicaoAnterior = posicaoMinha
            ultimaOper = time.time()
        else:
            #dk.moveTo(731, 172)
            dk.moveTo(721, 533)
            dk.click()
            posicaoAnterior = posicaoMinha
            ultimaOper = time.time()

        #time.sleep(2)

    #print('Objetivo:' + str(objetivo))

