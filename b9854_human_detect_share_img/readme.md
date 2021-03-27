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
云端部署部分在 i2ecs_server

做实验可以本地，如果要其他人真正可以用，这部分必须部署在阿里云ecs服务器等带ip的公网
并且修改i1client.py的 addr = 'http://localhost:5000'

在公网服务器上，新开一个窗口，同样进入虚拟环境然后,运行i2ecs_server中的 i2server.py

6.
配置视频来源

6.1
i0pedestrian_detection.py 的46-47行 代码为读取测试视频，如果想测试自己笔记本摄像头

6.2
可以打开43-44行，注视掉46-47，就可以访问本机摄像头

6.3
将来如果需要接入真实的交通摄像头，功能也准备好了，就注视掉以上部分，打开49-54，就可以
支持所有的海康/大华主流摄像头

7.

