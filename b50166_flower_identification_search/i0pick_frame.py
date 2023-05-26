import cv2

# Opens the Video file

# source_fish_video = 'i0goldfish'
# source_fish_video = 'i1koi_carp'
source_fish_video = "i0Lewisia露薇花"
source_fish_video = "i1Dahlia大丽花"

cap = cv2.VideoCapture("demo_video/" + source_fish_video + ".mp4")
i = 0
while cap.isOpened():
    ret, frame = cap.read()
    print("i=", i)
    if ret == False:
        break
    if i % 10 == 0:
        cv2.imwrite(
            "movie/static/img/source/" + source_fish_video + "_" + str(i) + ".jpg",
            frame,
        )
    i += 1

cap.release()
cv2.destroyAllWindows()
