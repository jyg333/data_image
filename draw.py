"""draw shapes and Putting Text"""
import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8') #dtype uint8 은 이미지 데이터에 쓰인다
# cv.imshow('blank',blank)
# img = cv.imread('photos/cat.jpg')
# cv.imshow('cat',img)
# blank[:] = 0,255,0

#paint image a certain color
# cv.imshow('Green',blank)

#draw Rectangle
# cv.rectangle(blank, (0,0),(250,250),(0,255,0),thickness=2)
# #If give thickness=cv.FILLED option, rectangle is filled with color. And same result will be get,when thickness  =-1
# cv.imshow('Rectangle',blank)
#
# #Draw Circle
# cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2),40,(0,0,255),thickness=2) #make circle on center of the frame
# cv.imshow('Circle',blank)
#
# #Draw Line
# cv.line(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2),(255,255,255), thickness=3)
# cv.imshow('Line',blank)

#Put text
cv.putText(blank,'Hello,  Good boy~',(100,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,0),thickness=1)
cv.imshow('Text',blank)
cv.waitKey(0)