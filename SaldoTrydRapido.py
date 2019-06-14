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
posicaoAnterior = 0
posicaoMinha = 0
ultimaOper = time.time()
while True:
    """    img = ImageGrab.grab(bbox=(799, 146, 922, 174))
    #img.show()
    #exit()
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    compras = ajustaNumero(pytesseract.image_to_string(img, config='--psm 7'))

    if(compras == ''):
        compras = 0

    img = ImageGrab.grab(bbox=(926, 145, 1035, 176))
    #img.show()
    #exit()
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    vendas = ajustaNumero(pytesseract.image_to_string(img, config='--psm 7'))

    if(vendas == ''):
        vendas = 0"""
    img = ImageGrab.grab(bbox=(698, 140, 790, 173))
    #img.show()
    #exit()
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
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

    img = ImageGrab.grab(bbox=(197, 142, 316, 173))
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
        objetivo=math.trunc((objetivo+1)*-1)
    else:
        objetivo=math.trunc((objetivo-1)*-1)


    posicaoMinha = int(posicaoMinha)

    print("Anterior:" + str(posicaoAnterior))
    print("Posicao:" + str(posicaoMinha))
    print("Modal:" + str(modal))
    print("Objetivo:" + str(objetivo))
    print("Diferenca:"+str(objetivo - posicaoMinha))

    
#    if(diferenca == 0):
#        dk.moveTo(1291,674)
#        dk.click()

    if(posicaoMinha != objetivo):

        if(time.time() - ultimaOper < 3):
            if(posicaoAnterior != posicaoMinha):
                continue

        diferenca = objetivo - posicaoMinha
        print(str(diferenca))
        dk.moveTo(1102,583)
        dk.doubleClick()
        dk.typewrite(str(diferenca))

        """dk.moveTo(1291,674)
        dk.click()"""

        """if(int(compras)+int(vendas) != 0):
            
            print('Compra'+str(compras))
            print('Venda'+str(vendas))
            print("Tem pendente")
            continue"""


        if(diferenca>0):
            dk.moveTo(1021, 642)
            #dk.moveTo(1197, 641)
            dk.click()
            posicaoAnterior = posicaoMinha+diferenca
            ultimaOper = time.time()
        else:
            dk.moveTo(1113, 639)
            #dk.moveTo(1290, 637)
            dk.click()
            posicaoAnterior = posicaoMinha+diferenca
            ultimaOper = time.time()
