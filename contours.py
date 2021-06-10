import cv2
import matplotlib.pyplot as plt

img = cv2.imread('stair.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #contour를 용이하게 하기 위해 gray로 변환
ret, thresh = cv2.threshold(img_gray, 127, 255, 0) # if x > 127 -> x =  255, else x = 0

plt.imshow(cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB))
plt.show()

contours = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[0] #hiercarchy를 포함한 모든 contours찾기
# findcontour의 추출 값중 두번째 값이 모든 contour의 조합에 해
img_1 = cv2.drawContours(img, contours, -1, (0, 150, 0), 4) # -1: 모든 외곽 추출

plt.imshow(cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY))
plt.show()