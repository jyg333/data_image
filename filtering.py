import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

img_1 = cv2.imread('forrest.jpg' )
# img_gray = cv2.cvtColor(img_1,cv2.COLOR_BGR2GRAY)

plt.imshow(cv2.cvtColor(img_1,cv2.COLOR_BGR2RGB))
img_2 = cv2.cvtColor(img_1,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray image",img_2)
cv2.waitKey(0)
plt.show()

"""(4x4) kernel 만들기, numpy.ones() """

size = 4
kernel = np.ones((size ,size),np.float32) / size ** 2
print(kernel)

dst = cv2.filter2D(img_2,-1, kernel) #주변값의 평균값으로 해당픽셀을 바꾸어 준다
plt.imshow(cv2.cvtColor(dst,cv2.COLOR_BGR2RGB))
plt.show()
#  낮아진 픽셀의 이미지를 확인할 수 있다.

#자동으로 블러링을 적용
dst_1 = cv2.blur(img_2,(4, 4))
plt.imshow(cv2.cvtColor(dst_1,cv2.COLOR_BGR2RGB))
plt.show()

#Gaissian blurring, 정규분포 /Kernel size가 홀수가 되어야 한다
dst_2 = cv2.GaussianBlur(img_2,(5,5),0)
plt.imshow(cv2.cvtColor(dst_2,cv2.COLOR_BGR2RGB))
plt.show()

"""Blur처리를 하면, 노이즈 및 손상을 줄일 수 있다는 이점이 있다."""