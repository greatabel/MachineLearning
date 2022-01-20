1. 
来到工程目录requirements.txt所在目录：
pip3 install -r requirements.txt

2
进入虚拟环境然后,运行 i0pedestrian_detection.py


：
python3 i0pedestrian_detection.py  --network=yolo3_mobilenet0.25_voc 


可以开更强的模型，开GPU版本：
python3 i0pedestrian_detection.py  --network=yolo3_mobilenet0.25_voc --gpu=True

python3 i0pedestrian_detection.py  --network=yolo3_darknet53_voc --gpu=True
可以修改第48行，把“if count % 15 == 0” 中的15修改为1， 这样处理起来帧数更高，更流畅



