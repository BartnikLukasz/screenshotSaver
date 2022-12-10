from pytesseract import pytesseract
import os
import re


def get_text(dir, name):
    return pytesseract.image_to_string(dir + name, lang="pol")


def get_number_of_files(path):
    return len(os.listdir(path))


resourcesDir = "resources"
lectureDir = "\\W6\\"

pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
regex = re.compile("(?<!\\n)\\n(?!\\n)")
iterator = 1
text = ""
while iterator <= get_number_of_files(resourcesDir + lectureDir):
    text += re.sub(regex, " ", string=get_text(resourcesDir + lectureDir, str(iterator) + ".PNG"))
    text += "---------\n\n"
    iterator += 1

with open(resourcesDir+lectureDir+'Result.txt', 'w') as file:
    file.write(text)
