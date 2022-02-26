import os
import cv2
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


labels = ["n", "s"]

'''
加载数据集到numpy中

'''
def get_training_data(data_dir):
    data = list()
    for label in labels:
        path = os.path.join(data_dir, label)
        class_num = labels.index(label)
        for img in os.listdir(path):
            try:
                img_arr = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                # resized_arr = cv2.resize(img_arr, (img_size, img_size))
                data.append([img_arr, class_num])
                # data.append([resized_arr, class_num])
            except Exception as e:
                print(e)
    return np.array(data)