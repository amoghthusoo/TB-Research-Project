from PIL import ImageGrab
import cv2
import numpy as nm
import pyautogui as pag
from time import sleep

delay = 9

def isWhiteOnly(coordinates):
    cap = ImageGrab.grab(bbox = coordinates)
    cap = cv2.resize(nm.array(cap), None, fx=1.8, fy=1.8, interpolation=cv2.INTER_CUBIC)
    not_white_pixels = nm.sum(cap != 255)
    if (not_white_pixels == 0):
        return False
    else:
        return True


coOrdDict = {
    "ULS_flag" : [639, 377, 665, 395],
    "URS_flag" : [1285, 377, 1307, 395],
    "MLS_flag" : [639, 452, 665, 468],
    "MRS_flag" : [1285, 452, 1307, 468],
    "LLS_flag" : [639, 525, 665, 540],
    "LRS_flag" : [1285, 525, 1307, 540]
}

pag.hotkey("alt", "tab")
sleep(delay/10)
print(isWhiteOnly(coOrdDict["ULS_flag"]))
print(isWhiteOnly(coOrdDict["URS_flag"]))
print(isWhiteOnly(coOrdDict["MLS_flag"]))
print(isWhiteOnly(coOrdDict["MRS_flag"]))
print(isWhiteOnly(coOrdDict["LLS_flag"]))
print(isWhiteOnly(coOrdDict["LRS_flag"]))
pag.hotkey("alt", "tab")
