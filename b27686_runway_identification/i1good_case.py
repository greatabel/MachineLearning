import cv2
import numpy as np
import os


def process_frame(frame, frame_counter):
    # 转换为灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 对比度增强
    equ = cv2.equalizeHist(gray)

    # 使用 Canny 边缘检测，降低阈值以检测更细的边缘
    edges = cv2.Canny(equ, 50, 150, apertureSize=3)

    # 使用 Probabilistic Hough Line Transform，降低角度分辨率以检测更细的线
    lines = cv2.HoughLinesP(
        edges, 1, np.pi / 360, 100, minLineLength=100, maxLineGap=10
    )

    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Save the image
    save_path = f"images/frame_{frame_counter}.png"
    cv2.imwrite(save_path, frame)


def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frame_counter = 0

    while cap.isOpened():
        ret, frame = cap.read()

        if ret == True:
            frame_counter += 1

            # 对每10帧进行处理
            if frame_counter % 10 == 0:
                process_frame(frame, frame_counter)
                cv2.imshow("Frame", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()


def main():
    # Create directory to save the frames if it does not exist
    if not os.path.exists("images"):
        os.makedirs("images")

    process_video("lane.mp4")


if __name__ == "__main__":
    main()
