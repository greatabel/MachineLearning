import os
import cv2



path_n = "orignal_data/n/1/指背"
path_s = "orignal_data/s/1/指背"

for filename in os.listdir(path_n):             
	#listdir的参数是文件夹的路径
    print(filename)
    file_path =  path_n + '/' +filename
    # print(file_path)
    im = cv2.imread(file_path)
    # 截取需要的部分，排除干扰
    im_0 = im[140:380,0:640]
    print(im.shape, '#', im_0.shape)
    cv2.imshow('t', im_0)
    cv2.waitKey()