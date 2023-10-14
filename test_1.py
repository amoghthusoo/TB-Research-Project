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

def containsBlack(coordinates):
    cap = ImageGrab.grab(bbox = coordinates)
    cap = cv2.resize(nm.array(cap), None, fx=1.8, fy=1.8, interpolation=cv2.INTER_CUBIC)
    not_white_pixels = nm.sum(cap != 255)
    if (not_white_pixels == 0):
        return False
    else:
        return True
    
def containsWhite(coordinates):
    cap = ImageGrab.grab(bbox = coordinates)
    cap = cv2.resize(nm.array(cap), None, fx=1.8, fy=1.8, interpolation=cv2.INTER_CUBIC)
    not_black_pixels = nm.sum(cap != 1)
    if (not_black_pixels == 0):
        return False
    else:
        return True
    
# def containsWhite(coordinates):
#     cap = ImageGrab.grab(bbox = coordinates)
#     # cap = cv2.resize(nm.array(cap), None, fx=1.8, fy=1.8, interpolation=cv2.INTER_CUBIC)
#     cap = nm.array(cap)
#     for i in cap:
        
#         for j in i:
#             print(j, end=' ')
#         print()
	
        
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



# print(containsBlack([933, 606, 956, 628]))

# print(containsWhite([377, 259, 379, 261]))
# print(containsWhite([549, 99, 551, 101]))
# print(containsWhite([619, 313, 621, 315]))

# pag.hotkey("alt", "tab")