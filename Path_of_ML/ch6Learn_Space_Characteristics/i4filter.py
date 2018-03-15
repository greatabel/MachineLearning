import numpy as np
import cv2 # OpenCV是一个非常棒的视觉处理库，cv2是OpenCV的Python版
import matplotlib.pyplot as plt

DIR = '../data/moredata/'
img = cv2.imread(DIR + 'dog.png') 
f = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # cv2用BGR格式编码图片，转换成RGB存储

def show_img(img):
    """展示图片"""
    plt.figure(figsize=(3, 3))
    plt.axis('off')
    plt.imshow(img)
    plt.show()

    
g = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]], dtype='float32')


# 执行卷积运算，也就是cv2的filter2D。命名filter源自信号滤波的概念，本节后面会提到
cov = cv2.filter2D(f, -1, g) 

show_img(cov)

