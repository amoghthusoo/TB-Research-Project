import numpy as nm
import pytesseract
import cv2
from PIL import ImageGrab, Image
import pyautogui as pag
from time import sleep

delay = 9

def imToString(coordinates):
	pytesseract.pytesseract.tesseract_cmd ='C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
	
	cap = ImageGrab.grab(bbox = coordinates)  # (x_min, y_min, x_max, y_max)
	cap = cv2.resize(nm.array(cap), None, fx=1.8, fy=1.8, interpolation=cv2.INTER_CUBIC)
	cv2.imwrite("test.png", cap)
	tesstr = pytesseract.image_to_string(
			cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),
			lang ='eng',
			config = "--psm 11")
	return tesstr

# pag.hotkey("alt", "tab")
# sleep(delay/10)

# pag.hotkey("ctrl", "f")
# sleep(delay/10)
# pag.write("upper left sextant")
# sleep(delay/10)
# pag.hotkey("ctrl", "a")
# sleep(delay/10)
# pag.press("backspace")
# sleep(delay/10)
# pag.press("esc")
# sleep(delay/10)


# sleep(3)
print(pag.position())
# print(imToString([639, 377, 665, 395]))
# print(imToString([1285, 377, 1307, 395]))




# img = Image.open("test.png")
# print(nm.array(img))


# img = cv2.imread("test.png")
# not_white_pixels = nm.sum(img != 255)
# print(not_white_pixels)

# pag.hotkey("alt", "tab")