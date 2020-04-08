# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 19:53:47 2020

@author: vaibh
"""

#!/usr/bin/env python
# coding: utf-8

# In[19]:


import cv2
import numpy as np

cap = cv2.VideoCapture(0)
a=0
for i in range(30):
    ret,source=cap.read()
    
while(1):
    # Take each frame
    _, frame = cap.read()
    #if a==0:
     #   source=frame
      #  a+=1

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    red1 = np.array([0,150,110])
    red2 = np.array([10,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, red1, red2)
    #edges = cv2.Canny(mask,100,255)
    
    l_r=np.array([170,150,100])
    u_r=np.array([180,255,255])
    mask2=cv2.inRange(hsv,l_r,u_r)
    mask=mask + mask2
    
    
    #blur = cv2.GaussianBlur(res,(5,5),0)
    kernal=np.ones((2,2),np.uint8)
    mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal,2)
    mask=cv2.morphologyEx(mask,cv2.MORPH_DILATE,kernal,2)
    res = cv2.bitwise_and(source,frame, mask=mask2)
    mask2=cv2.bitwise_not(mask)
    r1=cv2.bitwise_and(source,source,mask=mask)
    r2=cv2.bitwise_and(frame,frame,mask=mask2)

    # Bitwise-AND mask and original image
    #res = cv2.bitwise_and(frame,frame, mask= mask)
    result=cv2.addWeighted(r1,1,r2,1,0)

    #cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    #cv2.imshow('fram1e',mask2)
    #cv2.imshow('fram1e',r2)
    
    cv2.imshow('res',result)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()

