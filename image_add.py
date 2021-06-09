import cv2
import matplotlib.pyplot as plt
import numpy as np

'''처음에 두 이미지의 배열의 크기가 달라서 에러가 발생 하였다 -> resize()'''
img_1 = cv2.imread('cat.jpg')
img_2 = cv2.imread('forrest.jpg')
# print(img_1.shape)
# print(img_2.shape)
img_1 = np.resize(img_1, (531, 800, 3))
# print(img_1.shape)

add_1 = cv2.add(img_1, img_2) #opencv 를 이용한 이미지 합치기
plt.imshow(cv2.cvtColor(add_1, cv2.COLOR_BGR2GRAY))
plt.show()

add_2 = img_1 + img_2 #numpy에서 기본적으로 제공하는 연산을 이용
plt.imshow(cv2.cvtColor(add_2, cv2.COLOR_BGR2GRAY))
plt.show()
