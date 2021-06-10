import cv2
import matplotlib.pyplot as plt

#임계점을 지정하여 초과하는 값을 지정한다.

img_1 = cv2.imread("forrest.jpg",cv2.IMREAD_GRAYSCALE)
# cv2.threshold(image, treshold(number), max_value, type  )
ret, thres1 = cv2.threshold(img_1, 127, 255, cv2.THRESH_BINARY)
ret, thres2 = cv2.threshold(img_1, 127, 255, cv2.THRESH_BINARY_INV)
ret, thres3 = cv2.threshold(img_1, 127, 255, cv2.THRESH_TRUNC)
ret, thres4 = cv2.threshold(img_1, 127, 255, cv2.THRESH_TOZERO)
ret, thres5 = cv2.threshold(img_1, 127, 255, cv2.THRESH_TOZERO_INV)
images = []
images.append(thres1)
images.append(thres2)
images.append(thres3)
images.append(thres4)
images.append(thres5)

for i in images:
    plt.imshow(cv2.cvtColor(i, cv2.COLOR_GRAY2RGB))
    plt.show()


img_2 = cv2.imread('handwriting.jpg', cv2.IMREAD_GRAYSCALE)
ret, thres1 = cv2.threshold(img_2, 127, 255, cv2.THRESH_BINARY)
thres2 = cv2.adaptiveThreshold(img_2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,21, 3)
# 글씨 이미지를 예로들어, 단순 흑백 처리보다, 글씨의 임계점을 더 깔끔하게 처리가 가능하다.

plt.imshow(cv2.cvtColor(img_2, cv2.COLOR_GRAY2RGB))
plt.show()

plt.imshow(cv2.cvtColor(thres1, cv2.COLOR_GRAY2RGB))
plt.show()

plt.imshow(cv2.cvtColor(thres2, cv2.COLOR_GRAY2RGB))
plt.show()