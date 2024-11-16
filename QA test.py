import cv2 
import pytesseract
import os
import time

# this could be used for QA of annotated images

label = open("labels_tesseract.csv", "a")
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/Cellar/tesseract/5.3.0_1/bin/tesseract'
path = "CNN/dataset"
files = os.listdir(path)

for file in files:
    string = pytesseract.image_to_string(path + "/" + file)
    string = string.split(" ")
    string.pop()
    string = " ".join(string)
    label.write("./CNN/dataset/" + file + "|" + string + "\n")