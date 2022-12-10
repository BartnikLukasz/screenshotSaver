import pyscreenshot as ImageGrab
import cv2
import numpy as np
import glob
import os
from PIL import Image
import time
import logging as log


def take_screenshot(x1, y1, x2, y2):
    return ImageGrab.grab(bbox=(x1, y1, x2, y2))


def mse(previous, new):
    if previous is None or new is None:
        return 100
    img1 = cv2.cvtColor(np.array(previous), cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(np.array(new), cv2.COLOR_BGR2GRAY)
    diff = cv2.subtract(img1, img2)
    err = np.sum(diff ** 2)
    return err / (float((posY2-posY1) * (posX2 - posX1)))


def get_latest_file(path):
    file = max(glob.glob(path), key=os.path.getctime, default=None)
    if file is None:
        return None
    return Image.open(file)


dirPath = 'resources\\W9\\'
posX1 = 460
posY1 = 300
posX2 = 1450
posY2 = 780

if __name__ == '__main__':
    iterator = 1
    time.sleep(6)
    while 1:
        last = get_latest_file(dirPath+"*")
        taken = take_screenshot(posX1, posY1, posX2, posY2)
        error = mse(last, taken)
        print("Comparing last: {} with new: {}, error is: {}".format(last, taken, error))
        if error > 2:
            fileName = str(iterator) + ".png"
            if iterator == 1:
                taken.save(dirPath+fileName)
                iterator += 1
            elif last.filename == dirPath+str(iterator - 1) + ".png":
                taken.save(dirPath+fileName)
                iterator += 1
        time.sleep(6)
