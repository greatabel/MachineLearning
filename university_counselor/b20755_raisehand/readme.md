检测部分推荐部署ubuntu或者其他linux，或者osx等类unix系统
其他系统没有经过充分测试

1.
安装python3.6 以上版本

1.1
在osx上安装
brew link libpng
（否则requirements.txt中的dlib安装会有问题）

在ubuntu也是提前安装dlib:
https://www.jianshu.com/p/44469d7d86b3

2. 
安装pip3 

3.
（可选，非必须）（创建python3虚拟目录，隔绝不同版本库之间相互影响）
https://docs.python.org/zh-cn/3/tutorial/venv.html


4.
terminal底下进入工程目录下，在requirements.txt同级目录下运行：
pip3 install --upgrade -r requirements.txt



5.
另外开一个命令行，进入i3sentiment_predict_web
进入虚拟环境
执行：app.py

6.
访问：
http://127.0.0.1:5000/home

