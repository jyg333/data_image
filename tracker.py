import cv2
import numpy as np

#사용자가 값을 바꿔가면서 내용을 확인할 수 있
def change_color(x):
    r = cv2.getTrackbarPos("R","Image") #지정 TrackBar로 부터 값을 가져오는 함
    g = cv2.getTrackbarPos("G","Image")
    b = cv2.getTrackbarPos("B","Image")
    image[:] = [b, g, r]
    cv2.imshow('Image', image)

image = np.zeros((600, 400, 3), np.uint8) #임의의 이미지
cv2.namedWindow('Image')

"""RGB 값을 바꿀 수 있는 3개의 트랙바를 윈도우에 붙힐 수 있다"""
cv2.createTrackbar("R","Image", 0, 255, change_color)
cv2.createTrackbar("G","Image", 0, 255, change_color)
cv2.createTrackbar("B","Image", 0, 255, change_color)

cv2.imshow('Image',image)
cv2.waitKey(0)

