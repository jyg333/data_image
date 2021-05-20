import cv2
import numpy as np

#이미지를 읽어서 numpy 객체로 만드는 함수, cv2.imread(filename, flag),flag : how to read image
#flag options : color, grayscale, unchanged
# cv2.imshow(title, image), 함수를 이요하여 화면에 출력
# cv2.imwrite(file_name, flag), 특정한 이미즈를 파일로 저장하는 함수.

img_basic = cv2.imread('cat.jpg', cv2.IMREAD_COLOR)
cv2.imshow('img_basic', img_basic)
cv2.waitKey(0) # imshow 이후 윈도우 유지
cv2.imwrite('result1.png' , img_basic)

cv2.destroyAllWindows() #turn off window, print next window
#numpy 객체를 gray 형태로 바꾸준다
img_gray = cv2.cvtColor(img_basic, cv2.COLOR_BGR2GRAY)
cv2.imshow('img_GRAY', img_gray)
cv2.waitKey(0)
cv2.imwrite('result2.png', img_gray)


"""이미지 크기, 특정한 픽셀을 확인"""
print(img_basic.size)
print(img_basic.shape)
px1 = img_basic[100, 100]
print(px1)
#특정 범위의 픽셀만 바꾸는 방법
for i in range(0, 100):
    for j in range(0, 100):
        img_basic[i, j] = [255, 255, 255]
cv2.imshow("im_basic2", img_basic)
cv2.waitKey(0)
#처리속도가 빠른 방법
img_basic[0: 100, 0: 100] = [0, 0, 0]
cv2.imshow("im_basic3", img_basic)
cv2.waitKey(0)

#ROI : region of interset ,유의미한 공 이미지 공간을 맞춰주는 것이 중요함
roi = img_basic[200:350, 100:250]
img_basic[0:150, 0: 150] = roi
cv2.imshow("im_basic4", img_basic)
cv2.waitKey(0)

#color process
img_basic[:, :, 2] = 0 #BGR, 모든 필셀에 대해서 red = 0
cv2.imshow("im_basic5", img_basic)
cv2.waitKey(0)

"""Image Transformation"""
expand = cv2.resize(img_basic, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
cv2.imshow("im_basic6", img_basic)
cv2.waitKey(0)
print(expand.size )
shrink = cv2.resize(img_basic, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
cv2.imshow("im_basic7", img_basic)
cv2.waitKey(0)
print(shrink.size)

#location transfer
height, width = img_basic.shape[:2]
M = np.float32([[1, 0, 50], [0, 1, 10]])
transfer = cv2.warpAffine(img_basic,M,(height, width))
cv2.imshow("im_basic8", transfer)
cv2.waitKey(0)

#rotation
M2 = cv2.getRotationMatrix2D(( ), 90, 0.5) # center, angle, scale
rot = cv2.warpAffine(img_basic, M2, (height, width))
cv2.imshow("im_basic9", rot)
cv2.waitKey(0)

