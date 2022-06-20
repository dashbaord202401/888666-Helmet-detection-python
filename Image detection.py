# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 10:44:41 2020

@author: win 10
"""

import cv2
 
img = cv2.imread('img.jpeg')
 
cv2.imshow('Human Detection_Vijay',img)
 
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing 