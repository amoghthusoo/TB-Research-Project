import numpy as nm
import pytesseract
import cv2
from PIL import ImageGrab
import pyautogui as pag
from time import sleep
import csv

delay = 15
offsetMode = True
offsetValue = 9
newFile = False
includeImage = True

if (not offsetMode):
	offsetValue = 1
if (newFile):
	appendMOde = "w+"
else:
	appendMOde = "a+"

fields = [
	"patient_id",
	"country",
	"dst_profile",
	"age",
	"bmi",
	
	"glucose",
	"albumin",
	"creatinine",
	
	"ULS_small_cavities",
	"ULS_medium_cavities",
	"ULS_large_cavities",
	
	"URS_small_cavities",
	"URS_medium_cavities",
	"URS_large_cavities",
	
	"ULS_small_nodules",
	"ULS_medium_nodules",
	"ULS_large_nodules",
	"ULS_huge_nodules",
	"ULS_calcified_nodules",
	"ULS_non_calcified_nodules",
	"ULS_clustered_nodules",
	"ULS_multiple_nodules",
	"ULS_low_density",
	"ULS_medium_density",
	"ULS_large_density",
	
	"URS_small_nodules",
	"URS_medium_nodules",
	"URS_large_nodules",
	"URS_huge_nodules",
	"URS_calcified_nodules",
	"URS_non_calcified_nodules",
	"URS_clustered_nodules",
	"URS_multiple_nodules",
	"URS_low_density",
	"URS_medium_density",
	"URS_large_density",

	"MLS_small_cavities",
	"MLS_medium_cavities",
	"MLS_large_cavities",

	"MRS_small_cavities",
	"MRS_medium_cavities",
	"MRS_large_cavities",

	"MLS_small_nodules",
	"MLS_medium_nodules",
	"MLS_large_nodules",
	"MLS_huge_nodules",
	"MLS_calcified_nodules",
	"MLS_non_calcified_nodules",
	"MLS_clustered_nodules",
	"MLS_multiple_nodules",
	"MLS_low_density",
	"MLS_medium_density",
	"MLS_large_density",

	"MRS_small_nodules",
	"MRS_medium_nodules",
	"MRS_large_nodules",
	"MRS_huge_nodules",
	"MRS_calcified_nodules",
	"MRS_non_calcified_nodules",
	"MRS_clustered_nodules",
	"MRS_multiple_nodules",
	"MRS_low_density",
	"MRS_medium_density",
	"MRS_large_density",

	"LLS_small_cavities",
	"LLS_medium_cavities",
	"LLS_large_cavities",
	
	"LRS_small_cavities",
	"LRS_medium_cavities",
	"LRS_large_cavities",

	"LLS_small_nodules",
	"LLS_medium_nodules",
	"LLS_large_nodules",
	"LLS_huge_nodules",
	"LLS_calcified_nodules",
	"LLS_non_calcified_nodules",
	"LLS_clustered_nodules",
	"LLS_multiple_nodules",
	"LLS_low_density",
	"LLS_medium_density",
	"LLS_large_density",

	"LRS_small_nodules",
	"LRS_medium_nodules",
	"LRS_large_nodules",
	"LRS_huge_nodules",
	"LRS_calcified_nodules",
	"LRS_non_calcified_nodules",
	"LRS_clustered_nodules",
	"LRS_multiple_nodules",
	"LRS_low_density",
	"LRS_medium_density",
	"LRS_large_density",

	"abnormal_volume",
	"pleural_effusion",
	"pleural_effusion_bilateral",
	"timika_score",

	"ULS_flag",
	"URS_flag",
	"MLS_flag",
	"MRS_flag",
	"LLS_flag",
	"LRS_flag"

]
csvfile = open("record.csv", appendMOde, newline = "")
writer = csv.writer(csvfile)

if (newFile):
	writer.writerow(fields)

attributes = []
flags = []

def imToString(coordinates):
	pytesseract.pytesseract.tesseract_cmd ='C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
	
	cap = ImageGrab.grab(bbox = coordinates)  # (x_min, y_min, x_max, y_max)
	cap = cv2.resize(nm.array(cap), None, fx=2.5, fy=2.5, interpolation=cv2.INTER_CUBIC)
	cap = cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY)
	# cv2.imwrite("test.png", cap)
	tesstr = pytesseract.image_to_string(cap, lang ='eng')
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

def deleteSpaces(string):
    return string.replace(" ", "")

coOrdDict = {
	            "patient_id" : [102, 192, 165, 210],
                "country" : [715, 263, 776, 281],
                "age" : [458, 482, 506, 499],
                "bmi" : [458, 587, 523, 608],
                "glucose" : [367, 618, 451, 639],
                "albumin" : [632, 619, 705, 642],
                "creatinine" : [788, 619, 874, 640],
                "dst_profile" : [30, 477, 190, 500],
				
				"modality1" : [256, 562, 296, 584],
				"modality2" : [256, 606, 296, 628],
				"modality3" : [256, 651, 296, 672],
				"modality4" : [256, 695, 296, 716],
				"modality5" : [256, 739, 296, 760],

				"hasReport1" : [933, 562, 956, 584],
				"hasReport2" : [933, 606, 956, 628],
				"hasReport3" : [933, 651, 956, 672],
				"hasReport4" : [933, 695, 956, 716],
				"hasReport5" : [933, 739, 956, 760],
				
				"ULS_small_cavities" : [78, 511, 148, 530],
				"ULS_medium_cavities" : [78, 567, 148, 586],
				"ULS_large_cavities" : [78, 626, 148, 644],
				
				"URS_small_cavities" : [723, 511, 793, 530],
				"URS_medium_cavities" : [723, 567, 793, 586],
				"URS_large_cavities" : [723, 626, 793, 644],
				
				"ULS_small_nodules" : [78, 130, 148, 150],
				"ULS_medium_nodules" : [78, 187, 148, 208],
				"ULS_large_nodules" : [78, 246, 148, 266],
				"ULS_huge_nodules" : [78, 304, 148, 322],
				"ULS_calcified_nodules" : [78, 362, 148, 381],
				"ULS_non_calcified_nodules" : [78, 420, 148, 440],
				"ULS_clustered_nodules" : [78, 476, 148, 496],
				"ULS_multiple_nodules" : [78, 535, 148, 554],
				"ULS_low_density" : [78, 593, 133, 613],
				"ULS_medium_density" : [78, 651, 133, 673],
				"ULS_large_density" : [78, 710, 133, 731],

				"URS_small_nodules" : [720, 130, 787, 150],
				"URS_medium_nodules" : [720, 187, 787, 208],
				"URS_large_nodules" : [720, 246, 787, 266],
				"URS_huge_nodules" : [720, 304, 787, 322],
				"URS_calcified_nodules" : [720, 362, 787, 381],
				"URS_non_calcified_nodules" : [720, 420, 787, 440],
				"URS_clustered_nodules" : [720, 476, 787, 496],
				"URS_multiple_nodules" : [720, 535, 787, 554],
				"URS_low_density" : [720, 593, 787, 613],
				"URS_medium_density" : [720, 651, 787, 673],
				"URS_large_density" : [720, 710, 787, 731],

				"MLS_small_cavities" : [78, 511, 148, 530],
				"MLS_medium_cavities" : [78, 567, 148, 586],
				"MLS_large_cavities" : [78, 626, 148, 644],
				
				"MRS_small_cavities" : [723, 511, 793, 530],
				"MRS_medium_cavities" : [723, 567, 793, 586],
				"MRS_large_cavities" : [723, 626, 793, 644],

				"MLS_small_nodules" : [78, 130, 148, 150],
				"MLS_medium_nodules" : [78, 187, 148, 208],
				"MLS_large_nodules" : [78, 246, 148, 266],
				"MLS_huge_nodules" : [78, 304, 148, 322],
				"MLS_calcified_nodules" : [78, 362, 148, 381],
				"MLS_non_calcified_nodules" : [78, 420, 148, 440],
				"MLS_clustered_nodules" : [78, 476, 148, 496],
				"MLS_multiple_nodules" : [78, 535, 148, 554],
				"MLS_low_density" : [78, 593, 133, 613],
				"MLS_medium_density" : [78, 651, 133, 673],
				"MLS_large_density" : [78, 710, 133, 731],
				
				"MRS_small_nodules" : [720, 130, 787, 150],
				"MRS_medium_nodules" : [720, 187, 787, 208],
				"MRS_large_nodules" : [720, 246, 787, 266],
				"MRS_huge_nodules" : [720, 304, 787, 322],
				"MRS_calcified_nodules" : [720, 362, 787, 381],
				"MRS_non_calcified_nodules" : [720, 420, 787, 440],
				"MRS_clustered_nodules" : [720, 476, 787, 496],
				"MRS_multiple_nodules" : [720, 535, 787, 554],
				"MRS_low_density" : [720, 593, 787, 613],
				"MRS_medium_density" : [720, 651, 787, 673],
				"MRS_large_density" : [720, 710, 787, 731],

				"LLS_small_cavities" : [78, 511, 148, 530],
				"LLS_medium_cavities" : [78, 567, 148, 586],
				"LLS_large_cavities" : [78, 626, 148, 644],
			
				"LRS_small_cavities" : [723, 511, 793, 530],
				"LRS_medium_cavities" : [723, 567, 793, 586],
				"LRS_large_cavities" : [723, 626, 793, 644],

				"LLS_small_nodules" : [78, 130, 148, 150],
				"LLS_medium_nodules" : [78, 187, 148, 208],
				"LLS_large_nodules" : [78, 246, 148, 266],
				"LLS_huge_nodules" : [78, 304, 148, 322],
				"LLS_calcified_nodules" : [78, 362, 148, 381],
				"LLS_non_calcified_nodules" : [78, 420, 148, 440],
				"LLS_clustered_nodules" : [78, 476, 148, 496],
				"LLS_multiple_nodules" : [78, 535, 148, 554],
				"LLS_low_density" : [78, 593, 133, 613],
				"LLS_medium_density" : [78, 651, 133, 673],
				"LLS_large_density" : [78, 710, 133, 731],
				
				"LRS_small_nodules" : [720, 130, 787, 150],
				"LRS_medium_nodules" : [720, 187, 787, 208],
				"LRS_large_nodules" : [720, 246, 787, 266],
				"LRS_huge_nodules" : [720, 304, 787, 322],
				"LRS_calcified_nodules" : [720, 362, 787, 381],
				"LRS_non_calcified_nodules" : [720, 420, 787, 440],
				"LRS_clustered_nodules" : [720, 476, 787, 496],
				"LRS_multiple_nodules" : [720, 535, 787, 554],
				"LRS_low_density" : [720, 593, 787, 613],
				"LRS_medium_density" : [720, 651, 787, 673],
				"LRS_large_density" : [720, 710, 787, 731],

				"abnormal_volume" : [54, 446, 128, 465],
				"pleural_effusion" : [54, 502, 128, 524],
				"pleural_effusion_bilateral" : [54, 561, 128, 579],
				"timika_score" : [54, 603, 128, 623],

				"ULS_flag" : [639, 377, 665, 395],
				"URS_flag" : [1285, 377, 1307, 395],
				"MLS_flag" : [639, 452, 665, 468],
				"MRS_flag" : [1285, 452, 1307, 468],
				"LLS_flag" : [639, 525, 665, 540],
				"LRS_flag" : [1285, 525, 1307, 540],

				"checkRec1" : [668, 255, 680, 575],
				"checkRec2" : [853, 255, 865, 575],
				
		    }


pag.hotkey("alt", "tab")
sleep(delay/10)

def imaging_study(hasReport = True):

	global attributes, flags

	if(not hasReport):

		if(includeImage):
		
			# pag.press("up", presses = 130)
			# sleep(delay * 2)
			sleep(delay/10)

			while True:

				if(	containsWhite(coOrdDict["checkRec1"]) and 
					containsWhite(coOrdDict["checkRec2"]) 
					):
					break
				sleep(1)
				

			pag.moveTo(773, 401)
			sleep(delay/10)
			pag.rightClick()
			sleep(delay/10)
			pag.moveTo(794, 415)
			sleep(delay/10)
			pag.leftClick()
			sleep(delay/2)
			pag.write(str(attributes[0]))
			sleep(delay/10)
			pag.press("enter")
			sleep(delay/10)
			pag.press("left")
			sleep(delay/10)
			pag.press("enter")
			sleep(delay/10)
	
		
		for i in range(8, 96):
			attributes.append("null")
		for i in range(96, 102):
			flags.append(False)
		
		for i in range(2):
			pag.hotkey("alt", "left")
			sleep(delay/10)

		sleep(delay/10)
		return

	# sleep(delay * 2)
	sleep(delay)
	
	pag.hotkey("ctrl", "f")
	sleep(delay/10)
	pag.write("upper left sextant")
	sleep(delay/10)
	pag.hotkey("ctrl", "a")
	sleep(delay/10)
	pag.press("backspace")
	sleep(delay/10)
	pag.press("esc")
	sleep(delay/10)
	
	flags.append(containsBlack(coOrdDict["ULS_flag"]))
	flags.append(containsBlack(coOrdDict["URS_flag"]))
	flags.append(containsBlack(coOrdDict["MLS_flag"]))
	flags.append(containsBlack(coOrdDict["MRS_flag"]))
	flags.append(containsBlack(coOrdDict["LLS_flag"]))
	flags.append(containsBlack(coOrdDict["LRS_flag"]))
	
	pag.moveTo(652, 386)
	sleep(delay/10)
	pag.leftClick()
	sleep(delay/10)
	pag.moveTo(1296, 386)
	sleep(delay/10)
	pag.leftClick()
	sleep(delay/10)

	pag.moveTo(369, 386)
	pag.leftClick()
	sleep(delay/10)

	try:
		ULS_small_cavities = imToString(coOrdDict["ULS_small_cavities"]).split()[0][0:-1]
		attributes.append(ULS_small_cavities)
	except:
		attributes.append("null")

	try:
		ULS_medium_cavities = imToString(coOrdDict["ULS_medium_cavities"]).split()[0][0:-1]
		attributes.append(ULS_medium_cavities)
	except:
		attributes.append("null")

	try:
		ULS_large_cavities = imToString(coOrdDict["ULS_large_cavities"]).split()[0][0:-1]
		attributes.append(ULS_large_cavities)
	except:
		attributes.append("null")
	

	try:
		URS_small_cavities = imToString(coOrdDict["URS_small_cavities"]).split()[0][0:-1]
		attributes.append(URS_small_cavities)
	except:
		attributes.append("null")

	try:
		URS_medium_cavities = imToString(coOrdDict["URS_medium_cavities"]).split()[0][0:-1]
		attributes.append(URS_medium_cavities)
	except:
		attributes.append("null")

	try:
		URS_large_cavities = imToString(coOrdDict["URS_large_cavities"]).split()[0][0:-1]
		attributes.append(URS_large_cavities)
	except:
		attributes.append("null")

	
	pag.hotkey("ctrl", "f")
	sleep(delay/10)
	pag.write("nodules")
	sleep(delay/10)
	pag.hotkey("ctrl", "a")
	sleep(delay/10)
	pag.press("backspace")
	sleep(delay/10)
	pag.press("esc")
	sleep(delay/10)
	pag.press("down", presses = 8)
	sleep(delay/10)

	try:
		ULS_small_nodules = imToString(coOrdDict["ULS_small_nodules"]).split()[0][0:-1]
		attributes.append(ULS_small_nodules)
	except:
		attributes.append("null")
	
	try:
		ULS_medium_nodules = imToString(coOrdDict["ULS_medium_nodules"]).split()[0][0:-1]
		attributes.append(ULS_medium_nodules)
	except:
		attributes.append("null")
	
	try:
		ULS_large_nodules = imToString(coOrdDict["ULS_large_nodules"]).split()[0][0:-1]
		attributes.append(ULS_large_nodules)
	except:
		attributes.append("null")

	try:
		ULS_huge_nodules = imToString(coOrdDict["ULS_huge_nodules"]).split()[0][0:-1]
		attributes.append(ULS_huge_nodules)
	except:
		attributes.append("null")
	
	try:
		ULS_calcified_nodules = imToString(coOrdDict["ULS_calcified_nodules"]).split()[0]
		attributes.append(ULS_calcified_nodules)
	except:
		attributes.append("null")
	
	try:
		ULS_non_calcified_nodules = imToString(coOrdDict["ULS_non_calcified_nodules"]).split()[0]
		attributes.append(ULS_non_calcified_nodules)
	except:
		attributes.append("null")
	
	try:
		ULS_clustered_nodules = imToString(coOrdDict["ULS_clustered_nodules"]).split()[0]
		attributes.append(ULS_clustered_nodules)
	except:
		attributes.append("null")
	
	try:
		ULS_multiple_nodules = imToString(coOrdDict["ULS_multiple_nodules"]).split()[0]
		attributes.append(ULS_multiple_nodules)
	except:
		attributes.append("null")
	
	try:
		ULS_low_density = imToString(coOrdDict["ULS_low_density"]).split()[0][0:-1]
		attributes.append(ULS_low_density)
	except:
		attributes.append("null")
	
	try:
		ULS_medium_density = imToString(coOrdDict["ULS_medium_density"]).split()[0][0:-1]
		attributes.append(ULS_medium_density)
	except:
		attributes.append("null")
	
	try:
		ULS_large_density = imToString(coOrdDict["ULS_large_density"]).split()[0][0:-1]
		attributes.append(ULS_large_density)
	except:
		attributes.append("null")
	
	



	try:
		URS_small_nodules = imToString(coOrdDict["URS_small_nodules"]).split()[0][0:-1]
		attributes.append(URS_small_nodules)
	except:
		attributes.append("null")
	
	try:
		URS_medium_nodules = imToString(coOrdDict["URS_medium_nodules"]).split()[0][0:-1]
		attributes.append(URS_medium_nodules)
	except:
		attributes.append("null")
	
	try:
		URS_large_nodules = imToString(coOrdDict["URS_large_nodules"]).split()[0][0:-1]
		attributes.append(URS_large_nodules)
	except:
		attributes.append("null")

	try:
		URS_huge_nodules = imToString(coOrdDict["URS_huge_nodules"]).split()[0][0:-1]
		attributes.append(URS_huge_nodules)
	except:
		attributes.append("null")
	
	try:
		URS_calcified_nodules = imToString(coOrdDict["URS_calcified_nodules"]).split()[0]
		attributes.append(URS_calcified_nodules)
	except:
		attributes.append("null")
	
	try:
		URS_non_calcified_nodules = imToString(coOrdDict["URS_non_calcified_nodules"]).split()[0]
		attributes.append(URS_non_calcified_nodules)
	except:
		attributes.append("null")
	
	try:
		URS_clustered_nodules = imToString(coOrdDict["URS_clustered_nodules"]).split()[0]
		attributes.append(URS_clustered_nodules)
	except:
		attributes.append("null")
	
	try:
		URS_multiple_nodules = imToString(coOrdDict["URS_multiple_nodules"]).split()[0]
		attributes.append(URS_multiple_nodules)
	except:
		attributes.append("null")
	
	try:
		URS_low_density = imToString(coOrdDict["URS_low_density"]).split()[0][0:-1]
		attributes.append(URS_low_density)
	except:
		attributes.append("null")
	
	try:
		URS_medium_density = imToString(coOrdDict["URS_medium_density"]).split()[0][0:-1]
		attributes.append(URS_medium_density)
	except:
		attributes.append("null")
	
	try:
		URS_large_density = imToString(coOrdDict["URS_large_density"]).split()[0][0:-1]
		attributes.append(URS_large_density)
	except:
		attributes.append("null")

	pag.hotkey("ctrl", "f")
	sleep(delay/10)
	pag.write("middle left sextant")
	sleep(delay/10)
	pag.hotkey("ctrl", "a")
	sleep(delay/10)
	pag.press("backspace")
	sleep(delay/10)
	pag.press("esc")
	sleep(delay/10)
	
	pag.moveTo(652, 385)
	sleep(delay/10)
	pag.leftClick()
	sleep(delay/10)
	pag.moveTo(1296, 386)
	sleep(delay/10)
	pag.leftClick()
	sleep(delay/10)

	pag.moveTo(369, 386)
	pag.leftClick()
	sleep(delay/10)

	try:
		MLS_small_cavities = imToString(coOrdDict["MLS_small_cavities"]).split()[0][0:-1]
		attributes.append(MLS_small_cavities)
	except:
		attributes.append("null")

	try:
		MLS_medium_cavities = imToString(coOrdDict["MLS_medium_cavities"]).split()[0][0:-1]
		attributes.append(MLS_medium_cavities)
	except:
		attributes.append("null")

	try:
		MLS_large_cavities = imToString(coOrdDict["MLS_large_cavities"]).split()[0][0:-1]
		attributes.append(MLS_large_cavities)
	except:
		attributes.append("null")
	

	try:
		MRS_small_cavities = imToString(coOrdDict["MRS_small_cavities"]).split()[0][0:-1]
		attributes.append(MRS_small_cavities)
	except:
		attributes.append("null")

	try:
		MRS_medium_cavities = imToString(coOrdDict["MRS_medium_cavities"]).split()[0][0:-1]
		attributes.append(MRS_medium_cavities)
	except:
		attributes.append("null")

	try:
		MRS_large_cavities = imToString(coOrdDict["MRS_large_cavities"]).split()[0][0:-1]
		attributes.append(MRS_large_cavities)
	except:
		attributes.append("null")

	

	pag.hotkey("ctrl", "f")
	sleep(delay/10)
	pag.write("nodules")
	sleep(delay/10)
	pag.hotkey("ctrl", "a")
	sleep(delay/10)
	pag.press("backspace")
	sleep(delay/10)
	pag.press("esc")
	sleep(delay/10)
	pag.press("down", presses = 8)
	sleep(delay/10)

	try:
		MLS_small_nodules = imToString(coOrdDict["MLS_small_nodules"]).split()[0][0:-1]
		attributes.append(MLS_small_nodules)
	except:
		attributes.append("null")
	
	try:
		MLS_medium_nodules = imToString(coOrdDict["MLS_medium_nodules"]).split()[0][0:-1]
		attributes.append(MLS_medium_nodules)
	except:
		attributes.append("null")
	
	try:
		MLS_large_nodules = imToString(coOrdDict["MLS_large_nodules"]).split()[0][0:-1]
		attributes.append(MLS_large_nodules)
	except:
		attributes.append("null")

	try:
		MLS_huge_nodules = imToString(coOrdDict["MLS_huge_nodules"]).split()[0][0:-1]
		attributes.append(MLS_huge_nodules)
	except:
		attributes.append("null")
	
	try:
		MLS_calcified_nodules = imToString(coOrdDict["MLS_calcified_nodules"]).split()[0]
		attributes.append(MLS_calcified_nodules)
	except:
		attributes.append("null")
	
	try:
		MLS_non_calcified_nodules = imToString(coOrdDict["MLS_non_calcified_nodules"]).split()[0]
		attributes.append(MLS_non_calcified_nodules)
	except:
		attributes.append("null")
	
	try:
		MLS_clustered_nodules = imToString(coOrdDict["MLS_clustered_nodules"]).split()[0]
		attributes.append(MLS_clustered_nodules)
	except:
		attributes.append("null")
	
	try:
		MLS_multiple_nodules = imToString(coOrdDict["MLS_multiple_nodules"]).split()[0]
		attributes.append(MLS_multiple_nodules)
	except:
		attributes.append("null")
	
	try:
		MLS_low_density = imToString(coOrdDict["MLS_low_density"]).split()[0][0:-1]
		attributes.append(MLS_low_density)
	except:
		attributes.append("null")
	
	try:
		MLS_medium_density = imToString(coOrdDict["MLS_medium_density"]).split()[0][0:-1]
		attributes.append(MLS_medium_density)
	except:
		attributes.append("null")
	
	try:
		MLS_large_density = imToString(coOrdDict["MLS_large_density"]).split()[0][0:-1]
		attributes.append(MLS_large_density)
	except:
		attributes.append("null")
	
	



	try:
		MRS_small_nodules = imToString(coOrdDict["MRS_small_nodules"]).split()[0][0:-1]
		attributes.append(MRS_small_nodules)
	except:
		attributes.append("null")
	
	try:
		MRS_medium_nodules = imToString(coOrdDict["MRS_medium_nodules"]).split()[0][0:-1]
		attributes.append(MRS_medium_nodules)
	except:
		attributes.append("null")
	
	try:
		MRS_large_nodules = imToString(coOrdDict["MRS_large_nodules"]).split()[0][0:-1]
		attributes.append(MRS_large_nodules)
	except:
		attributes.append("null")

	try:
		MRS_huge_nodules = imToString(coOrdDict["MRS_huge_nodules"]).split()[0][0:-1]
		attributes.append(MRS_huge_nodules)
	except:
		attributes.append("null")
	
	try:
		MRS_calcified_nodules = imToString(coOrdDict["MRS_calcified_nodules"]).split()[0]
		attributes.append(MRS_calcified_nodules)
	except:
		attributes.append("null")
	
	try:
		MRS_non_calcified_nodules = imToString(coOrdDict["MRS_non_calcified_nodules"]).split()[0]
		attributes.append(MRS_non_calcified_nodules)
	except:
		attributes.append("null")
	
	try:
		MRS_clustered_nodules = imToString(coOrdDict["MRS_clustered_nodules"]).split()[0]
		attributes.append(MRS_clustered_nodules)
	except:
		attributes.append("null")
	
	try:
		MRS_multiple_nodules = imToString(coOrdDict["MRS_multiple_nodules"]).split()[0]
		attributes.append(MRS_multiple_nodules)
	except:
		attributes.append("null")
	
	try:
		MRS_low_density = imToString(coOrdDict["MRS_low_density"]).split()[0][0:-1]
		attributes.append(MRS_low_density)
	except:
		attributes.append("null")
	
	try:
		MRS_medium_density = imToString(coOrdDict["MRS_medium_density"]).split()[0][0:-1]
		attributes.append(MRS_medium_density)
	except:
		attributes.append("null")
	
	try:
		MRS_large_density = imToString(coOrdDict["MRS_large_density"]).split()[0][0:-1]
		attributes.append(MRS_large_density)
	except:
		attributes.append("null")


	pag.hotkey("ctrl", "f")
	sleep(delay/10)
	pag.write("lower left sextant")
	sleep(delay/10)
	pag.hotkey("ctrl", "a")
	sleep(delay/10)
	pag.press("backspace")
	sleep(delay/10)
	pag.press("esc")
	sleep(delay/10)
	
	pag.moveTo(652, 385)
	sleep(delay/10)
	pag.leftClick()
	sleep(delay/10)
	pag.moveTo(1296, 386)
	sleep(delay/10)
	pag.leftClick()
	sleep(delay/10)

	pag.moveTo(369, 386)
	pag.leftClick()
	sleep(delay/10)

	try:
		LLS_small_cavities = imToString(coOrdDict["LLS_small_cavities"]).split()[0][0:-1]
		attributes.append(LLS_small_cavities)
	except:
		attributes.append("null")

	try:
		LLS_medium_cavities = imToString(coOrdDict["LLS_medium_cavities"]).split()[0][0:-1]
		attributes.append(LLS_medium_cavities)
	except:
		attributes.append("null")

	try:
		LLS_large_cavities = imToString(coOrdDict["LLS_large_cavities"]).split()[0][0:-1]
		attributes.append(LLS_large_cavities)
	except:
		attributes.append("null")
	

	try:
		LRS_small_cavities = imToString(coOrdDict["LRS_small_cavities"]).split()[0][0:-1]
		attributes.append(LRS_small_cavities)
	except:
		attributes.append("null")

	try:
		LRS_medium_cavities = imToString(coOrdDict["LRS_medium_cavities"]).split()[0][0:-1]
		attributes.append(LRS_medium_cavities)
	except:
		attributes.append("null")

	try:
		LRS_large_cavities = imToString(coOrdDict["LRS_large_cavities"]).split()[0][0:-1]
		attributes.append(LRS_large_cavities)
	except:
		attributes.append("null")


	pag.hotkey("ctrl", "f")
	sleep(delay/10)
	pag.write("nodules")
	sleep(delay/10)
	pag.hotkey("ctrl", "a")
	sleep(delay/10)
	pag.press("backspace")
	sleep(delay/10)
	pag.press("esc")
	sleep(delay/10)
	pag.press("down", presses = 8)
	sleep(delay/10)

	try:
		LLS_small_nodules = imToString(coOrdDict["LLS_small_nodules"]).split()[0][0:-1]
		attributes.append(LLS_small_nodules)
	except:
		attributes.append("null")
	
	try:
		LLS_medium_nodules = imToString(coOrdDict["LLS_medium_nodules"]).split()[0][0:-1]
		attributes.append(LLS_medium_nodules)
	except:
		attributes.append("null")
	
	try:
		LLS_large_nodules = imToString(coOrdDict["LLS_large_nodules"]).split()[0][0:-1]
		attributes.append(LLS_large_nodules)
	except:
		attributes.append("null")

	try:
		LLS_huge_nodules = imToString(coOrdDict["LLS_huge_nodules"]).split()[0][0:-1]
		attributes.append(LLS_huge_nodules)
	except:
		attributes.append("null")
	
	try:
		LLS_calcified_nodules = imToString(coOrdDict["LLS_calcified_nodules"]).split()[0]
		attributes.append(LLS_calcified_nodules)
	except:
		attributes.append("null")
	
	try:
		LLS_non_calcified_nodules = imToString(coOrdDict["LLS_non_calcified_nodules"]).split()[0]
		attributes.append(LLS_non_calcified_nodules)
	except:
		attributes.append("null")
	
	try:
		LLS_clustered_nodules = imToString(coOrdDict["LLS_clustered_nodules"]).split()[0]
		attributes.append(LLS_clustered_nodules)
	except:
		attributes.append("null")
	
	try:
		LLS_multiple_nodules = imToString(coOrdDict["LLS_multiple_nodules"]).split()[0]
		attributes.append(LLS_multiple_nodules)
	except:
		attributes.append("null")
	
	try:
		LLS_low_density = imToString(coOrdDict["LLS_low_density"]).split()[0][0:-1]
		attributes.append(LLS_low_density)
	except:
		attributes.append("null")
	
	try:
		LLS_medium_density = imToString(coOrdDict["LLS_medium_density"]).split()[0][0:-1]
		attributes.append(LLS_medium_density)
	except:
		attributes.append("null")
	
	try:
		LLS_large_density = imToString(coOrdDict["LLS_large_density"]).split()[0][0:-1]
		attributes.append(LLS_large_density)
	except:
		attributes.append("null")
	
	



	try:
		LRS_small_nodules = imToString(coOrdDict["LRS_small_nodules"]).split()[0][0:-1]
		attributes.append(LRS_small_nodules)
	except:
		attributes.append("null")
	
	try:
		LRS_medium_nodules = imToString(coOrdDict["LRS_medium_nodules"]).split()[0][0:-1]
		attributes.append(LRS_medium_nodules)
	except:
		attributes.append("null")
	
	try:
		LRS_large_nodules = imToString(coOrdDict["LRS_large_nodules"]).split()[0][0:-1]
		attributes.append(LRS_large_nodules)
	except:
		attributes.append("null")

	try:
		LRS_huge_nodules = imToString(coOrdDict["LRS_huge_nodules"]).split()[0][0:-1]
		attributes.append(LRS_huge_nodules)
	except:
		attributes.append("null")
	
	try:
		LRS_calcified_nodules = imToString(coOrdDict["LRS_calcified_nodules"]).split()[0]
		attributes.append(LRS_calcified_nodules)
	except:
		attributes.append("null")
	
	try:
		LRS_non_calcified_nodules = imToString(coOrdDict["LRS_non_calcified_nodules"]).split()[0]
		attributes.append(LRS_non_calcified_nodules)
	except:
		attributes.append("null")
	
	try:
		LRS_clustered_nodules = imToString(coOrdDict["LRS_clustered_nodules"]).split()[0]
		attributes.append(LRS_clustered_nodules)
	except:
		attributes.append("null")
	
	try:
		LRS_multiple_nodules = imToString(coOrdDict["LRS_multiple_nodules"]).split()[0]
		attributes.append(LRS_multiple_nodules)
	except:
		attributes.append("null")
	
	try:
		LRS_low_density = imToString(coOrdDict["LRS_low_density"]).split()[0][0:-1]
		attributes.append(LRS_low_density)
	except:
		attributes.append("null")
	
	try:
		LRS_medium_density = imToString(coOrdDict["LRS_medium_density"]).split()[0][0:-1]
		attributes.append(LRS_medium_density)
	except:
		attributes.append("null")
	
	try:
		LRS_large_density = imToString(coOrdDict["LRS_large_density"]).split()[0][0:-1]
		attributes.append(LRS_large_density)
	except:
		attributes.append("null")


	pag.hotkey("ctrl", "f")
	sleep(delay/10)
	pag.write("overall characteristics")
	sleep(delay/10)
	pag.hotkey("ctrl", "a")
	sleep(delay/10)
	pag.press("backspace")
	sleep(delay/10)
	pag.press("esc")
	sleep(delay/10)

	try:
		abnormal_volume = imToString(coOrdDict["abnormal_volume"]).split()[0][0:-1]
		attributes.append(abnormal_volume)
	except:
		attributes.append("null")

	try:
		pleural_effusion = imToString(coOrdDict["pleural_effusion"]).split()[0][0:-1]
		attributes.append(pleural_effusion)
	except:
		attributes.append("null")

	try:
		pleural_effusion_bilateral = imToString(coOrdDict["pleural_effusion_bilateral"]).split()[0]
		attributes.append(pleural_effusion_bilateral)
	except:
		attributes.append("null")

	try:
		timika_score = imToString(coOrdDict["timika_score"]).split()[0]
		attributes.append(timika_score)
	except:
		attributes.append("null")

	
	if(includeImage):
		pag.press("up", presses = 130)
		# sleep(delay * 2)
		sleep(delay/10)


		while True:

			if(	containsWhite(coOrdDict["checkRec1"]) and 
				containsWhite(coOrdDict["checkRec2"]) 
				):
				break
			sleep(1)
			

		pag.moveTo(773, 401)
		sleep(delay/10)
		pag.rightClick()
		sleep(delay/10)
		pag.moveTo(794, 415)
		sleep(delay/10)
		pag.leftClick()
		sleep(delay/2)
		pag.write(str(attributes[0]))
		sleep(delay/10)
		pag.press("enter")
		sleep(delay/10)
		pag.press("left")
		sleep(delay/10)
		pag.press("enter")
		sleep(delay/10)
	
	for i in range(2):
		pag.hotkey("alt", "left")
		sleep(delay/10)
	
	sleep(delay/10)

# imaging_study()

def case_details():

	global attributes, offsetMode, offsetValue, flags

	while True:

		if (not offsetMode):
			pag.hotkey("ctrl", "f")
			sleep(delay/10)
			pag.write("registration date")
			sleep(delay/10)
			pag.hotkey("ctrl", "a")
			sleep(delay/10)
			pag.press("backspace")
			sleep(delay/10)
			pag.press("esc")
			sleep(delay/10)
			pag.press("tab", presses = 2)
			sleep(delay/10)
			pag.press("enter")
			sleep(delay/10)
			sleep(delay)
		else:
			pag.hotkey("ctrl", "f")
			sleep(delay/10)
			pag.write("registration date")
			sleep(delay/10)
			pag.hotkey("ctrl", "a")
			sleep(delay/10)
			pag.press("backspace")
			sleep(delay/10)
			pag.press("esc")
			sleep(delay/10)
			pag.press("tab", presses = 2 + 3 * (offsetValue - 1))
			sleep(delay/10)
			pag.press("enter")
			sleep(delay/10)
			sleep(delay)


		for j in range(offsetValue,22):

			try:
				patient_id = imToString(coOrdDict["patient_id"])
				patient_id = deleteSpaces(patient_id).split()[0]
				attributes.append(patient_id)
			except:
				attributes.append("null")
			
			try:
				country = imToString(coOrdDict["country"]).split()[0]
				attributes.append(country)
			except:
				attributes.append("null")
			
			try:
				dst_proile = imToString(coOrdDict["dst_profile"])[0:11]
				attributes.append(dst_proile)
			except:
				attributes.append("null")

			try:
				age = imToString(coOrdDict["age"]).split()[0]
				attributes.append(age)
			except:
				attributes.append("null")

			try:
				bmi = imToString(coOrdDict["bmi"]).split()[0]
				attributes.append(bmi)
			except:
				attributes.append("null")

			pag.hotkey("ctrl", "f")
			sleep(delay/10)
			pag.write("biochemistry results")
			sleep(delay/10)
			pag.hotkey("ctrl", "a")
			sleep(delay/10)
			pag.press("backspace")
			sleep(delay/10)
			pag.press("enter")
			sleep(delay/10)
			pag.press("esc")
			sleep(delay/10)

			try:
				glucose = imToString(coOrdDict["glucose"]).split()[0]
				attributes.append(glucose)
			except:
				attributes.append("null")

			try:
				albumin = imToString(coOrdDict["albumin"]).split()[0]
				attributes.append(albumin)
			except:
				attributes.append("null")

			try:
				creatinine = imToString(coOrdDict["creatinine"]).split()[0]
				attributes.append(creatinine)
			except:
				attributes.append("null")

			pag.hotkey("ctrl", "f")
			sleep(delay/10)
			pag.write("imaging studies")
			sleep(delay/10)
			pag.hotkey("ctrl", "a")
			sleep(delay/10)
			pag.press("backspace")
			sleep(delay/10)
			pag.press("enter")
			sleep(delay/10)
			pag.press("esc")
			sleep(delay/10)
			
			# try:
			# 	print(imToString(coOrdDict["modality1"]).split()[0])
			# except:
			# 	pass
			# try:
			# 	print(imToString(coOrdDict["modality2"]).split()[0])
			# except:
			# 	pass
			# try:
			# 	print(imToString(coOrdDict["modality3"]).split()[0])
			# except:
			# 	pass
			
			if (	("CR" in imToString(coOrdDict["modality1"]) or 
	   				"XC" in imToString(coOrdDict["modality1"])) and 
					containsBlack(coOrdDict["hasReport1"])):
				pag.press("tab", presses = 13)
				sleep(delay/10)
				pag.press("enter")
				sleep(delay/10)
				sleep(delay)
				# sleep(delay * 3)
				imaging_study()

				# print("Breakpoint1")

				if (j != 21):
					pag.hotkey("ctrl", "f")
					sleep(delay/10)
					pag.write("registration date")
					sleep(delay/10)
					pag.hotkey("ctrl", "a")
					sleep(delay/10)
					pag.press("backspace")
					sleep(delay/10)
					pag.press("enter")
					sleep(delay/10)
					pag.press("esc")
					sleep(delay/10)
					
					pag.press("tab", presses = 2 + 3 * j)
					sleep(delay/10)
					pag.press("enter")
					sleep(delay/10)
					sleep(delay)

			elif (	("CR" in imToString(coOrdDict["modality2"]) or 
		 			"XC" in imToString(coOrdDict["modality2"])) and 
					containsBlack(coOrdDict["hasReport2"])):
				pag.press("tab", presses = 14)
				sleep(delay/10)
				pag.press("enter")
				sleep(delay/10)
				sleep(delay)
				# sleep(delay * 3)
				imaging_study()

				if (j != 21):
					pag.hotkey("ctrl", "f")
					sleep(delay/10)
					pag.write("registration date")
					sleep(delay/10)
					pag.hotkey("ctrl", "a")
					sleep(delay/10)
					pag.press("backspace")
					sleep(delay/10)
					pag.press("enter")
					sleep(delay/10)
					pag.press("esc")
					sleep(delay/10)
					
					pag.press("tab", presses = 2 + 3 * j)
					sleep(delay/10)
					pag.press("enter")
					sleep(delay/10)
					sleep(delay)

			elif (	("CR" in imToString(coOrdDict["modality3"]) or
		 			"XC" in imToString(coOrdDict["modality3"])) and 
		 			containsBlack(coOrdDict["hasReport3"])):
				pag.press("tab", presses = 15)
				sleep(delay/10)
				pag.press("enter")
				sleep(delay/10)
				sleep(delay)
				# sleep(delay * 3)
				imaging_study()

				if (j != 21):
					pag.hotkey("ctrl", "f")
					sleep(delay/10)
					pag.write("registration date")
					sleep(delay/10)
					pag.hotkey("ctrl", "a")
					sleep(delay/10)
					pag.press("backspace")
					sleep(delay/10)
					pag.press("enter")
					sleep(delay/10)
					pag.press("esc")
					sleep(delay/10)
					
					pag.press("tab", presses = 2 + 3 * j)
					sleep(delay/10)
					pag.press("enter")
					sleep(delay/10)
					sleep(delay)
			
			elif (	("CR" in imToString(coOrdDict["modality4"])  or
		 			"XC" in imToString(coOrdDict["modality4"])) and 
					containsBlack(coOrdDict["hasReport4"])):
				pag.press("tab", presses = 16)
				sleep(delay/10)
				pag.press("enter")
				sleep(delay/10)
				sleep(delay)
				# sleep(delay * 3)
				imaging_study()

				if (j != 21):
					pag.hotkey("ctrl", "f")
					sleep(delay/10)
					pag.write("registration date")
					sleep(delay/10)
					pag.hotkey("ctrl", "a")
					sleep(delay/10)
					pag.press("backspace")
					sleep(delay/10)
					pag.press("enter")
					sleep(delay/10)
					pag.press("esc")
					sleep(delay/10)
					
					pag.press("tab", presses = 2 + 3 * j)
					sleep(delay/10)
					pag.press("enter")
					sleep(delay/10)
					sleep(delay)
			
			elif (	("CR" in imToString(coOrdDict["modality5"]) or
		 			"XC" in imToString(coOrdDict["modality5"])) and 
					containsBlack(coOrdDict["hasReport5"])):
				pag.press("tab", presses = 17)
				sleep(delay/10)
				pag.press("enter")
				sleep(delay/10)
				sleep(delay)
				# sleep(delay * 3)
				imaging_study()

				if (j != 21):
					pag.hotkey("ctrl", "f")
					sleep(delay/10)
					pag.write("registration date")
					sleep(delay/10)
					pag.hotkey("ctrl", "a")
					sleep(delay/10)
					pag.press("backspace")
					sleep(delay/10)
					pag.press("enter")
					sleep(delay/10)
					pag.press("esc")
					sleep(delay/10)
					
					pag.press("tab", presses = 2 + 3 * j)
					sleep(delay/10)
					pag.press("enter")
					sleep(delay/10)
					sleep(delay)

			elif (	"CR" in imToString(coOrdDict["modality1"]) or 
		 			"XC" in imToString(coOrdDict["modality1"])):
				pag.press("tab", presses = 13)
				sleep(delay/10)
				pag.press("enter")
				sleep(delay/10)
				sleep(delay)
				# sleep(delay * 3)
				imaging_study(False)

				# print("Breakpoint1")

				if (j != 21):
					pag.hotkey("ctrl", "f")
					sleep(delay/10)
					pag.write("registration date")
					sleep(delay/10)
					pag.hotkey("ctrl", "a")
					sleep(delay/10)
					pag.press("backspace")
					sleep(delay/10)
					pag.press("enter")
					sleep(delay/10)
					pag.press("esc")
					sleep(delay/10)
					
					pag.press("tab", presses = 2 + 3 * j)
					sleep(delay/10)
					pag.press("enter")
					sleep(delay/10)
					sleep(delay)

			elif (	"CR" in imToString(coOrdDict["modality2"]) or 
		 			"XC" in imToString(coOrdDict["modality2"])):
				pag.press("tab", presses = 14)
				sleep(delay/10)
				pag.press("enter")
				sleep(delay/10)
				sleep(delay)
				# sleep(delay * 3)
				imaging_study(False)

				if (j != 21):
					pag.hotkey("ctrl", "f")
					sleep(delay/10)
					pag.write("registration date")
					sleep(delay/10)
					pag.hotkey("ctrl", "a")
					sleep(delay/10)
					pag.press("backspace")
					sleep(delay/10)
					pag.press("enter")
					sleep(delay/10)
					pag.press("esc")
					sleep(delay/10)
					
					pag.press("tab", presses = 2 + 3 * j)
					sleep(delay/10)
					pag.press("enter")
					sleep(delay/10)
					sleep(delay)

			elif (	"CR" in imToString(coOrdDict["modality3"]) or
					"XC" in imToString(coOrdDict["modality3"])):
				pag.press("tab", presses = 15)
				sleep(delay/10)
				pag.press("enter")
				sleep(delay/10)
				sleep(delay)
				# sleep(delay * 3)
				imaging_study(False)

				if (j != 21):
					pag.hotkey("ctrl", "f")
					sleep(delay/10)
					pag.write("registration date")
					sleep(delay/10)
					pag.hotkey("ctrl", "a")
					sleep(delay/10)
					pag.press("backspace")
					sleep(delay/10)
					pag.press("enter")
					sleep(delay/10)
					pag.press("esc")
					sleep(delay/10)
					
					pag.press("tab", presses = 2 + 3 * j)
					sleep(delay/10)
					pag.press("enter")
					sleep(delay/10)
					sleep(delay)
			
			elif (	"CR" in imToString(coOrdDict["modality4"]) or 
		 			"XC" in imToString(coOrdDict["modality4"])):
				pag.press("tab", presses = 16)
				sleep(delay/10)
				pag.press("enter")
				sleep(delay/10)
				sleep(delay)
				# sleep(delay * 3)
				imaging_study(False)

				if (j != 21):
					pag.hotkey("ctrl", "f")
					sleep(delay/10)
					pag.write("registration date")
					sleep(delay/10)
					pag.hotkey("ctrl", "a")
					sleep(delay/10)
					pag.press("backspace")
					sleep(delay/10)
					pag.press("enter")
					sleep(delay/10)
					pag.press("esc")
					sleep(delay/10)
					
					pag.press("tab", presses = 2 + 3 * j)
					sleep(delay/10)
					pag.press("enter")
					sleep(delay/10)
					sleep(delay)

			elif (	"CR" in imToString(coOrdDict["modality5"]) or 
		 			"XC" in imToString(coOrdDict["modality5"])):
				pag.press("tab", presses = 17)
				sleep(delay/10)
				pag.press("enter")
				sleep(delay/10)
				sleep(delay)
				# sleep(delay * 3)
				imaging_study(False)

				if (j != 21):
					pag.hotkey("ctrl", "f")
					sleep(delay/10)
					pag.write("registration date")
					sleep(delay/10)
					pag.hotkey("ctrl", "a")
					sleep(delay/10)
					pag.press("backspace")
					sleep(delay/10)
					pag.press("enter")
					sleep(delay/10)
					pag.press("esc")
					sleep(delay/10)
					
					pag.press("tab", presses = 2 + 3 * j)
					sleep(delay/10)
					pag.press("enter")
					sleep(delay/10)
					sleep(delay)

			else:

				for i in range(8, 96):
					attributes.append("null")
				for i in range(96, 102):
					flags.append(False)
				
				pag.hotkey("alt", "left")
				sleep(delay/10)

				if (j != 21):
					pag.press("tab", presses = 3)
					sleep(delay/10)
					pag.press("enter")
					sleep(delay/10)
					sleep(delay)
			
			row = attributes + flags
			
			try:
				writer.writerow(row)
			except:
				for i in range(8, 96):
					row[i] = "null"
				writer.writerow(row)
				
			attributes = []
			flags = []

		
		offsetMode = False
		offsetValue = 1

	
		pag.press("down", presses = 10)
		sleep(delay/10)
		pag.moveTo(805, 562)
		sleep(delay/10)
		pag.leftClick()
		sleep(delay * 2)


case_details()
