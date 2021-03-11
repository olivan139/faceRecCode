import cv2
import time
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('photo_2020-02-13_14-43-31.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = cascade.detectMultiScale(gray, 1.1,4)
font = cv2.FONT_HERSHEY_SIMPLEX

for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('img',img)
cv2.waitKey()