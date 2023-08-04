# -*- coding: utf-8 -*-
import cv2
import os


def readImg(filePath, channel=3):
    if not os.path.exists(filePath):
        print("FilePath Error: this path is not exists!")
        return None
    if channel == 3:
        return cv2.imread(filePath, 1)
    elif channel == 1:
        return cv2.imread(filePath, 0)
    else:
        print("Channel Error: The channels can only be =3 or =1!")
        return None


def myImgShow(windowName, img, isTransform=False):
    if isTransform:
        cv2.namedWindow(windowName, cv2.WINDOW_FREERATIO)
    if img is None:
        print("Img Error: this img is None!")
        return
    cv2.imshow(windowName, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()