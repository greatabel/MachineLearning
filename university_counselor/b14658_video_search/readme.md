检测部分推荐部署ubuntu或者其他linux，或者osx等类unix系统
其他系统没有经过充分测试

1.
安装python3.6 以上版本

2. 
安装pip3 

3.
（可选，非必须）（创建python3虚拟目录，隔绝不同版本库之间相互影响）
https://docs.python.org/zh-cn/3/tutorial/venv.html


4.
terminal底下进入工程目录下，在requirements.txt同级目录下运行：
pip3 install --upgrade -r requirements.txt


5.

cmd/terminal进入文件夹 后执行：
python3 wsgi.py

6.
浏览器访问：

http://localhost:5000/home

默认账号 greatabel1@126.com ps:abel
自己也可以正常注册

7.
如果想自己训练以图搜图：(在安装有库的环境或者虚拟环境)
python3 i1offine_train.py

8.
协同推荐也可以自己重新训练,自己运行
moive/adapter/collaborative_filtering.py
数据集你也可以自己添加到ml-1m