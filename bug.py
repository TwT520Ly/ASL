import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('flower.jpg',0) #直接读为灰度图像

for i in range(2000): #添加点噪声
    temp_x = np.random.randint(0,img.shape[0])
    temp_y = np.random.randint(0,img.shape[1])
    img[temp_x][temp_y] = 255

print(type(img))
print(img.shape)
blur = cv2.GaussianBlur(img,(11,11),0)
plt.subplot(1,2,1),plt.imshow(img,'gray')#默认彩色，另一种彩色bgr
plt.subplot(1,2,2),plt.imshow(blur,'gray')

plt.show()