import os
import cv2
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


from common import get_training_data

# ----------- 地域设置 -----------

# save_path = "data"

# demo_path = "data/train/s/1_右食指_u_b_20210416081256.bmp"


# labels = ["n", "s"]

# mysize = 145

# ----------- 性别设置 -----------
# save_path = "data_gender"

# demo_path = save_path + "/train/female/1_右食指_u_b_20210416081253.bmp"

# labels = ["male", "female"]

# mysize = 145

# ----------- 民族设置 -----------
save_path = "data_nationality"

demo_path = save_path + "/train/han/17_右食指_u_b_20210418094411.bmp"

labels = ["han", "tibetan"]

mysize = 145

# -------- end of setting -----


train = get_training_data(save_path + "/train",labels, mysize)
test = get_training_data(save_path + "/test", labels, mysize)
print(f"Train: {len(train)}, Test: {len(test)}")


plt.figure(figsize=(7, 7))
plt.imshow(train[2][0])
plt.title(labels[train[2][1]])
plt.show()

"""
全局阈值
全局阈值技术是对整个图像使用单个阈值的技术，而局部阈值技术对从整个图像获得的分区子图像使用唯一阈值。

"""
sample = train[2][0]
rgb = cv2.cvtColor(sample, cv2.COLOR_BGR2RGB)
plt.imshow(rgb)
plt.show()


gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
plt.imshow(gray, cmap="gray")
plt.show()


thresholds = [10, 20, 50, 60, 70, 80, 90, 100]
for threshold in thresholds:
    val, thresh = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    plt.imshow(thresh, cmap="gray")
    plt.title(f"Threshold = {threshold}")
    plt.show()


def show_threshold(image, threshold):
    cv2_threshs = [
        cv2.THRESH_BINARY,
        cv2.THRESH_BINARY_INV,
        cv2.THRESH_TRUNC,
        cv2.THRESH_TOZERO,
        cv2.THRESH_TOZERO_INV,
    ]

    names = [
        "IMAGE_ORIGINAL",
        "THRESH_BINARY",
        "THRESH_BINARY_INV",
        "THRESH_TRUNC",
        "THRESH_TOZERO",
        "THRESH_TOZERO_INV",
    ]

    for name, cv2_thresh in zip(names, cv2_threshs):
        val, image_new = cv2.threshold(image, threshold, 255, cv2_thresh)
        plt.imshow(cv2.cvtColor(image_new, cv2.COLOR_BGR2RGB), cmap="gray")
        plt.title(f"Threshold={threshold}, {name}")
        plt.show()


show_threshold(gray, 140)


# Otsu 的方法用于执行自动图像阈值处理。 在最简单的形式中，
# 该算法返回一个单一的强度阈值，将像素分为前景和背景两类。
"""
在计算机视觉和图像处理中，大津二值化法用来自动对基于聚类的图像进行二值化，[1] 或者说，
将一个灰度图像退化为二值图像。该算法以大津展之命名。算法假定该图像根据双模直方图（前景像素和背景像素）把包含两类像素，
于是它要计算能将两类分开的最佳阈值，使得它们的类内方差最小；由于两两平方距离恒定，
所以即它们的类间方差最大。[2] 因此，大津二值化法粗略的来说就是一维Fisher判别分析的离散化模拟。

原始方法的多级阈值扩展称为多大津算法

理解和原理写入论文，可以看： https://zhuanlan.zhihu.com/p/95034826

"""
value, img_otsu = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
plt.imshow(cv2.cvtColor(img_otsu, cv2.COLOR_BGR2RGB), cmap="gray")
plt.title(f"Otsu's method")
plt.show()


print("-" * 20)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
img_new = cv2.imread(demo_path, 1)
img_vect = img_new.reshape((-1, 3))
img_vect = np.float32(img_vect)

# print(img_vect, img_vect.shape)

plt.hist(img_vect, 256, [0, 256])
plt.show()

ret, label, centroids = cv2.kmeans(
    img_vect, 3, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS
)


centroids = np.uint8(centroids)
img_kmeans = centroids[label.flatten()]
img_kmeans = img_kmeans.reshape(img_new.shape)

plt.title("KMeans Segmentation")
plt.imshow(cv2.cvtColor(img_kmeans, cv2.COLOR_BGR2RGB))
plt.show()


def kmeans_segmentation(image, k_=2):
    img_vect = np.float32(image).reshape(-1, 3)
    criterio = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
    ret, label, centroids = cv2.kmeans(
        img_vect, k_, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS
    )
    centroids = np.uint8(centroids)
    img_kmeans = centroids[label.flatten()]
    return img_kmeans.reshape(image.shape)


for k in [2, 3, 4, 5, 6, 7, 8]:
    plt.imshow(cv2.cvtColor(kmeans_segmentation(img_new, k), cv2.COLOR_BGR2RGB))
    plt.title(f"KMeans Segmentation for K={k}")
    plt.show()


histogram, bins = np.histogram(gray, 256, [0, 256])
plt.plot(histogram, color="red")
plt.title("Image Histogram")
plt.ylabel("y")
plt.xlabel("x")
plt.grid()
plt.show()
