import numpy as nm
import pytesseract
import cv2
from PIL import ImageGrab
import pyautogui as pag
from time import sleep
import csv

coOrdDict = {
	
    "glucose" : [367, 618, 451, 639],
    "albumin" : [632, 619, 705, 642],
    "creatinine" : [788, 619, 874, 640]
}

def imToString(coordinates):
	pytesseract.pytesseract.tesseract_cmd ='C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
	
	cap = ImageGrab.grab(bbox = coordinates)  # (x_min, y_min, x_max, y_max)
	cap = cv2.resize(nm.array(cap), None, fx=2.2, fy=2.2, interpolation=cv2.INTER_CUBIC)
	cap = cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY)
	# cv2.imwrite("test.png", cap)
	tesstr = pytesseract.image_to_string(cap, lang ='eng')
	return tesstr



pag.hotkey("alt", "tab")
print(imToString(coOrdDict["glucose"]).split()[0])
print(imToString(coOrdDict["albumin"]).split()[0])
print(imToString(coOrdDict["creatinine"]).split()[0])
pag.hotkey("alt", "tab")