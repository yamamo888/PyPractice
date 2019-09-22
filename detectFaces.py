# -*- coding: utf-8 -*-

import os
import sys
import pdb

import cv2

cap = cv2.VideoCapture(0)


# ---------------------------- command argment ------------------------------ #
# name of image
img_name = str(sys.argv[1])
# --------------------------------------------------------------------------- #

# -------------------------- classifiers ------------------------------------ #
# reading detect-front-human-face by loading github
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
print('read face_cascade')
# reading detect-front-human-face with glasses by loading github
eyegls_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
print('read eye_cascade')
# --------------------------------------------------------------------------- #

# ---------------------------- images --------------------------------------- #
img = cv2.imread('lena.jpg')
#img = cv2.imread('occhan.jpg')
# --------------------------------------------------------------------------- #

# ---------------------------- parameters ----------------------------------- #
count = 0
fps = 30
size = (640, 480)
tick= cv2.getTickCount()
face = 0
eyes = 0

#flag
flag1 = 0
flag2 = 0

#state
state = 0
# --------------------------------------------------------------------------- #

# =============================================================================
# 検出関数
# =============================================================================
def detect(img, fc, egc, img_name="sample"):
    """
    Detect face & eye-glasses.
    [Args]
        img: images
        fc: face_cascade(CascadeClassifier)
        egc: eyegls_cascade(CascadeClassifier)
        img_name: name of saved images 
    """
    
    # all scale image -> gray scale image
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # detect face
    faces = fc.detectMultiScale(grayImg)
    
    # 1. 顔の検知
    for x, y, w, h in faces:
        # 検知した顔を矩形で囲む(塗りつぶし・モザイク...etcも可能)
        # 1:画像, 2,3:座標, 3:矩形の色
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # 顔画像(グレースケール)
        grayFace = grayImg[y: y + h, x: x + w]
        # 顔画像(カラースケール)
        colorFace = img[y: y + h, x: x + w]
        # detect eye-glasses (In: image of gray-scale face)
        eyeglasses = egc.detectMultiScale(grayFace)
        
        # 2. 眼鏡の検知
        for (egx, egy, egw, egh) in eyeglasses:
            cv2.rectangle(colorFace, (egx, egy), (egx + egw, egy + egh), (0, 255, 0), 2)
            
    # save images
    #cv2.imwrite("{}.png".format(img_name), img)
    cv2.imshow("{}.png".format(img_name), img)
    key = cv2.waitKey(0)

    # if esc key, stop program
    if key == 27:
        cv2.destroyAllWindows()    

    
    """
    parts = cascade.detectMultiScale(
        img, scaleFactor = 1.11, minNeighbors = 3, minSize = size)
    
    return parts
    """
# =============================================================================

# detection
detect(img,face_cascade,eyegls_cascade,img_name=img_name)
