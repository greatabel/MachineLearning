import cv2
import numpy as np
from PIL import Image
from pyheatmap.heatmap import HeatMap


def create_heatmap(image, data):
    image1 = cv2.imread(image)
    background = Image.new("RGB", (image1.shape[1], image1.shape[0]), color=0)
    # 开始绘制热度图
    hm = HeatMap(data)
    hit_img = hm.heatmap(base=background, r=100)
    # background为背景图片，r是半径，默认为10
    hit_img = cv2.cvtColor(np.asarray(hit_img), cv2.COLOR_RGB2BGR)
    # Image格式转换成cv2格式
    overlay = image1.copy()
    alpha = 0.5  # 设置覆盖图片的透明度
    cv2.rectangle(
        overlay, (0, 0), (image1.shape[1], image1.shape[0]), (255, 0, 0), -1
    )  # 设置蓝色为热度图基本色蓝色
    image2 = cv2.addWeighted(overlay, alpha, image1, 1 - alpha, 0)  # 将背景热度图覆盖到原图
    image3 = cv2.addWeighted(hit_img, alpha, image2, 1 - alpha, 0)  # 将热度图覆盖到原图
    cv2.imshow("ru", image3)
    cv2.imwrite("h_" + image, image3)
    cv2.waitKey(0)
    return image3


if __name__ == "__main__":
    t0 = [
        [116, 110, 30],
        [116, 110, 50],
        [116, 110, 32],
        [116, 110, 10],
        [116, 110, 30],
        [116, 110, 36],
        [236, 310, 50],
        [482, 469, 5],
        [400, 463, 8],
        [320, 453, 26],
        [200, 1140, 20],
        [180, 1136, 10],
        [120, 1130, 10],
        [90, 1126, 20],
    ]
    t1 = [
        [106, 120, 35],
        [106, 120, 50],
        [116, 120, 20],
        [116, 110, 10],
        [116, 110, 30],
        [116, 110, 36],
        [236, 310, 50],
        [482, 469, 5],
        [400, 463, 8],
        [116, 210, 26],
        [116, 210, 20],
        [116, 210, 10],
        [116, 210, 10],
        [116, 210, 20],
    ]
    create_heatmap("test0.jpg", t0)  # 数据来自通过眼动追踪技术生成的神经网络分析出
    create_heatmap("test1.jpg", t1)  # 数据来自通过眼动追踪技术生成的神经网络分析出
