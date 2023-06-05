1. 
whole project based on python3
(project should work at all versons above python3.5 [include python3.5] )

2. 
创建虚拟环境
create virtual environment
at Unix/MacOS run:
python3 -m venv  mlsystem-env

at windows run:
python -m venv  mlsystem-env

then enter virtual environment:
Windows run:
mlsystem-env\Scripts\activate.bat

Unix/MacOS run:
source mlsystem-env/bin/activate


3. 
来到工程目录requirements.txt所在目录：
pip3 install -r requirements.txt

4.
运行本地mac程序

新开一个窗口，同样进入虚拟环境然后,运行 i0pedestrian_detection.py

注意事项：
macbook上面，因为没有支持macbook的GPU，所以使用CPU版本，考虑到CPU的运行神经网络性能，
我采取了各种措施提高处理效率：
python3 i0pedestrian_detection.py  --network=yolo3_mobilenet0.25_voc

如果是带英伟达GPU的笔记本(RTX1080/RTX1080Ti/RTX2080/RTX2080Ti...)，
可以开更强的模型，开GPU版本：
python3 i0pedestrian_detection.py  --network=yolo3_darknet53_voc --gpu=True
可以修改第48行，把“if count % 15 == 0” 中的15修改为1， 这样处理起来帧数更高，更流畅

5.
对于未戴头盔被抓拍的图，我们后台运行：
python3 i3get_license.py
会出来她的车牌截图（准确）和截取的车牌号（一般准确)




