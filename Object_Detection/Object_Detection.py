import numpy as np
import cv2
cap=cv2.VideoCapture(0)

while(True):
    ret,img=cap.read()
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    blue1=np.array([100,100,100])
    blue2=np.array([130,255,255])

    red1=np.array([0,100,100])
    red2=np.array([5,255,255])

    green1=np.array([15,100,200])
    green2=np.array([30,255,255])
    
    mask1=cv2.inRange(hsv,blue1,blue2)
    mask2=cv2.inRange(hsv,green1,green2)
    mask3=cv2.inRange(hsv,red1,red2)
    mask = mask1 + mask2 + mask3
    
    blur = cv2.GaussianBlur(mask,(5,5),0)
    
    #_ , contours , _ = cv2.findContours(blur,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours, hierarchy = cv2.findContours(blur,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
   
    
    for cnt in contours:
        area=0
        area=cv2.contourArea(cnt)
        if area > 500:
             x,y,w,h = cv2.boundingRect(cnt)
             img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
             #img = cv2.drawContours(img, contours, -1, (0,255,0),2)            
             
    cv2.imshow("mask",blur)
    cv2.imshow("frame",img)
    k=cv2.waitKey(1)
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()    