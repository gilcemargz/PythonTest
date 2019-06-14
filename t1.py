import numpy as np
from numpy import *
from PIL import Image
from PIL import ImageGrab
import pytesseract
import cv2


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
src_path = "D:\\"

def get_region(box):
    #Grabs the region of the box coordinates
    im = ImageGrab.grab(box)
    #im.show()
    #Change size of image to 200% of the original size
    a, b, c, d = box
    doubleX = (c - a) * 2
    doubleY = (d - b) * 2
    im.resize((doubleX, doubleY)).save("D:\\test.png", 'PNG')

def get_string(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)
    # Convert to gray
    img = ~img
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )
    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    # Write image after removed noise
    cv2.imwrite(src_path + "removed_noise.png", img)
    #  Apply threshold to get image with only black and white
    #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    # Write the image after apply opencv to do some ...
    cv2.imwrite(src_path + "thres.png", img)
    # Recognize text with tesseract for python

    result = pytesseract.image_to_string(Image.open(src_path + "thres.png"),config='--psm 7')

    return result

def main():
    #Grab the region of the screenshot (box area)
    x1 = 826
    y1 = 535
    x2 = x1 + 35
    y2 = y1 + 15

    region = (x1,y1,x2,y2)
    get_region(region)

    #Output results
    print ("OCR Output: ")
    print (get_string("D:\\test.png"))


while True:
    main()

result = pytesseract.image_to_string(Image.open("D:\\thres.png"))
print('Resultado:'+result)

value = Image.open("D:\\thres.png")

text = pytesseract.image_to_string(value)
print('Text:'+text)

