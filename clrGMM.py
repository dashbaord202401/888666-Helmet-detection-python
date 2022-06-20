# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 19:09:58 2020

@author: win 10
"""
import numpy as np
import cv2

cap = cv2.VideoCapture('vid1.mp4')

fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(40) & 0xff
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
