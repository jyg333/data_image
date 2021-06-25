import cv2
import matplotlib.pyplot as plt

img = cv2.imread('digit_image.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray,230, 255,0)
thresh = cv2.bitwise_not(thresh) #배경이 흰색 -> 검은색으로 반전시킴, 글자를 흰색으로 출력하기 위한 함

plt.imshow(cv2.cvtColor(thresh,cv2.COLOR_GRAY2RGB))
plt.show()

contours = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[0] #모든 line+hierarchy ,사각형 point 4 찾기
# ↳opencv 의 버전에 따라서 반환하는 변수의 개수가 다르기 때문에 [1] -> [0]으로 수정해서 오류 해결한다.
img_1 = cv2.drawContours(img,contours,-1,(0,0,255),4) #-1: 모든 외곽에 대해 그린다, RED = 255 로 윤곽을 그림

plt.imshow(cv2.cvtColor(img_1,cv2.COLOR_BGR2RGB))
plt.show()

contour = contours[2]
x, y, w, h = cv2.boundingRect(contour) #사격형의 x, y 좌표와 너비, 높이를 반환한다.
img_2 = cv2.rectangle(img_1,(x,y),(x+w,y+h),(0,0,255),3) #사각형 바운딩을 그린다.

plt.imshow(cv2.cvtColor(img_2,cv2.COLOR_BGR2RGB))
plt.show()