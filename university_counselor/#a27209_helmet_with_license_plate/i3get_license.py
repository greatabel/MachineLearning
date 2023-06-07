import cv2
import pytesseract
import os
import json  # 导入json模块

def detect_license(image_path):
    # 加载图片
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # 使用 OpenCV 转换图片为灰度图片
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 使用 OpenCV 进行边缘检测
    edges = cv2.Canny(gray, 30, 200)

    # 使用 OpenCV 寻找边缘检测后的轮廓
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 对找到的轮廓按面积大小进行排序
    contours = sorted(contours, key = cv2.contourArea, reverse = True)[:10]

    # 初始化车牌轮廓
    plate_contour = None

    for contour in contours:
        # 获取近似的多边形轮廓
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.018 * peri, True)

        # 如果近似的轮廓有四个顶点，那么就可能是车牌
        if len(approx) == 4:
            plate_contour = approx
            break

    license_plate = ''  # 初始化车牌号码
    # 如果找到了车牌轮廓
    if plate_contour is not None:
        # 获取车牌区域
        x, y, w, h = cv2.boundingRect(plate_contour)

        # 在原始图像上绘制一个矩形，以标记出车牌的位置
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # 截取车牌区域
        plate = gray[y:y+h, x:x+w]

        # 保存截取的车牌图像
        cv2.imwrite('license_images/'+ os.path.basename(image_path), plate)

        # # 显示标记了车牌位置的原始图像
        # cv2.imshow("Marked", img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # 使用 pytesseract 识别车牌号码，只识别数字
        license_plate = pytesseract.image_to_string(plate, config='--psm 11 --oem 3 -c tessedit_char_whitelist=0123456789')

        print("车牌号码：", license_plate)

    return license_plate

if __name__ == "__main__":
    # directory = 'original'
    directory = 'detected_images'
    license_plates = {}  # 初始化一个空字典来保存图片名称和对应的车牌号码
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"): 
            print(filename, '-'*10)
            license_plate = detect_license(os.path.join(directory, filename))
            license_plates[filename] = license_plate  # 将识别的车牌号码保存到字典

    # 将字典保存到 JSON 文件
    with open('license_plates.json', 'w') as file:
        json.dump(license_plates, file)
