"""k-nearest neighbor 알고리즘"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

#0 - 100 까지 25개의 랜덤한 수
train_data =np.random.randint(0, 100,(25,2)).astype(np.float32)

# 데이타는 0또는  1
response = np.random.randint(0,2,(25,1)).astype(np.float32)

#산점도를 그리는 matplotlib function
red = train_data[response.ravel()==0]
plt.scatter(red[:,0],red[:,1],80,'r','^')
# value = 1
blue = train_data[response.ravel() == 1]
plt.scatter(blue[:,0],blue[:,1],80,'b','s')

new_one = np.random.randint(0, 100,(1,2)).astype(np.float32)
plt.scatter(new_one[:,0],new_one [:,1],80,'g','o')

knn = cv2.ml.KNearest_create()
knn.train(train_data,cv2.ml.ROW_SAMPLE, response)
ret,  result, neighbor, dist = knn.findNearest(new_one,3)

print('result : ',result)
print('neighbor : ',neighbor)
print('dist : ',dist)

plt.show()

img_1 =cv2.imread('digits.png') #(20 x20) 5000개의 이미지 데이터
gray = cv2.cvtColor(img_1,cv2.COLOR_BGR2GRAY) #shape = (1000,2000)

# divide horizontal 100 rows, vertical 50 columns
cells = [np.hsplit(row,100) for row in np.vsplit(gray, 50)]
x = np.array(cells)
print(x.shape)
train = x[:,:].reshape(-1,400).astype(np.float32) #400크기로 한줄로 바꾸는 코드 ,shape =(5000,400)

k = np.arange(10)
train_labels = np.repeat(k, 500)[:,np.newaxis]

np.savez('trained.npz',train = train,train_labels = train_labels)
#5000개의 학습 데이터 지정


"""숫자인식 Test"""
import glob
#1줄에 100개씩 담겨있는 이미지 데이터, 0- 9까지 생성
cv2.imwrite('test0.png',x[0, 0])
cv2.imwrite('test1.png',x[5, 0])
cv2.imwrite('test2.png',x[10, 0])
cv2.imwrite('test3.png',x[15, 0])
cv2.imwrite('test4.png',x[20, 0])
cv2.imwrite('test5.png',x[25, 0])
cv2.imwrite('test6.png',x[30, 0])
cv2.imwrite('test7.png',x[35, 0])
cv2.imwrite('test8.png',x[40, 0])
cv2.imwrite('test9.png',x[45, 0])

file_name = 'trained.npz'

#학습 데이터를 불러오는 함수
def load_train_data(file_name):
    with np.load(file_name) as data:
        train = data['train']
        train_labels = data['train_labels']
    return train, train_labels

#숫자 이미지를  (20 x 20) 크기로 스케일링
def resize(image):
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_resize = cv2.resize(gray,(20, 20)) #최종적으로 (1 * 400) 크기로 반환된다
    cv2.imshow('image',gray_resize)
    return gray_resize.reshape(-1, 400).astype(np.float32)

def check(test,train ,train_labels):
    knn = cv2.ml.KNearest_create()
    knn.train(train,cv2.ml.ROW_SAMPLE,train_labels)
    # 근접알고리즘을 이용해 가까운 5가지 숫자 탐색
    ret, result, neighbor, dist = knn.findNearest(test,k = 5)
    return result

train, train_labels = load_train_data(file_name)

for file_name in glob.glob('./test*.png'):
    test = resize(file_name)
    result = check(test, train, train_labels)
    print(result)
    cv2.waitKey(0)
cv2.destroyAllWindows()

"""k-nearest algorithm을 이용해서 근접한 숫자랑 비교하여 숫자인식"""

