import os
import cv2


# path_n = "orignal_data/n/1/指背"
path_s = "orignal_data/s/1/指背"

# save_path = "data/n"
save_path = "data/s"

for filename in os.listdir(path_s):
    # for filename in os.listdir(path_n):
    # listdir的参数是文件夹的路径
    print(filename)
    file_path = path_s + "/" + filename
    # file_path =  path_n + '/' +filename
    # print(file_path)
    im = cv2.imread(file_path)
    # 截取需要的部分，排除干扰，去掉指甲部分，去掉背景黑色部分，只留下静脉区值得分析的
    im_0 = im[180:310, 0:600]
    print(im.shape, "#", im_0.shape)

    # 保存
    save_path_file = os.path.join(save_path, filename)
    # save_path_file = os.path.join(save_path,filename+'.jpg')
    cv2.imwrite(save_path_file, im_0)
    cv2.imshow("t", im_0)
    cv2.waitKey()
