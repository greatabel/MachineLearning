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

show_img(f)
print('展示一部分图片像素值:\n' + str(f[:2, :2])) # 按RGB编码，0-255的像素数值

