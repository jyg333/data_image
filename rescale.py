"""resize & rescaling
modify height and width
Reason : most of camera doesn't support maximum capability """

import cv2 as cv

image = cv.imread('photos/cat.jpg',cv.IMREAD_COLOR)
cv.imshow('cat',image)

#rescaling 함수 만들기, opencv01에서 import
def rescaleFrame(frame, scale = 0.75):

    width = int(frame.shape[1] * scale)  #shape[1] is basically width
    height = int(frame.shape[0] * scale)#shape[0] is basically height
    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)#interpolation 보간법 pixel size를 줄이는 경우 INTER_AREA




cv.waitKey(0)