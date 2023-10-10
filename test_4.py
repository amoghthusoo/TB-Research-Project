import numpy as nm
import pytesseract
import cv2
from PIL import ImageGrab, Image
import pyautogui as pag
from time import sleep

delay =10

pag.hotkey("alt", "tab")
sleep(delay/10)

def imToString(coordinates):
	pytesseract.pytesseract.tesseract_cmd ='C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
	
	cap = ImageGrab.grab(bbox = coordinates)  # (x_min, y_min, x_max, y_max)
	cap = cv2.resize(nm.array(cap), None, fx=2.5, fy=2.5, interpolation=cv2.INTER_CUBIC)
	cap = cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY)
	cv2.imwrite("test.png", cap)
	tesstr = pytesseract.image_to_string(cap, lang ='eng')
	return tesstr

def deleteSpaces(string):
    return string.replace(" ", "")

try:
    patient_id = imToString([102, 192, 165, 210])
    patient_id = deleteSpaces(patient_id).split()[0]
    print(patient_id)
except:
   pass

pag.hotkey("alt", "tab")