import cv2
import numpy as np

"""내 유튜브 구독 목록을 따로 저장해 높기 위해 캠처한 이미지를 병합하여 저장하기위해 사용"""

img_1 = cv2.imread('1.png')
img_2 = cv2.imread('2.png')
img_3 = cv2.imread('3.png')
print(img_1.shape)
print(img_2.shape)
print(img_3.shape)

im_v = cv2.vconcat([img_1,img_2])
im_v2 = cv2.vconcat([im_v, img_3])
cv2.imwrite('im_v2.png',im_v2)

#combine different width
#shape[0] -> height, shape[1] -> width
def vconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC): #INTER_CUBIC :  4x4 보간법
    w_min = min(im.shape[1] for im in im_list)
    im_list_resize = [cv2.resize(im, (w_min, int(im.shape[0] * w_min / im.shape[1])), interpolation=interpolation)
                      for im in im_list]
    return cv2.vconcat(im_list_resize)

im_v_resize = vconcat_resize_min([img_1, img_2, img_3])
cv2.imwrite('resize.jpg', im_v_resize)