import cv2 
import pytesseract
import os
import time

# this could be used for QA of annotated images

label = open("labels_tesseract.csv", "a")

path = ".CNN/dataset"
files = os.listdir(path)
for file in files:
    print(file)
    time.sleep(10000)
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/Cellar/tesseract/5.3.0_1/bin/tesseract'
string = pytesseract.image_to_string(file)

print(string)