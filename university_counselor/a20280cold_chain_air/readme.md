检测部分推荐部署ubuntu或者其他linux，或者osx等类unix系统
其他系统没有经过充分测试，但是window10 也是应该正常工作的

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
python3 i1openstreetmap_main.py

6.
浏览器访问：

http://localhost:5000/home

已经注册好的账号 可以直接登录：
greatabel1@126.com  abel
你也可以自己注册和登录

7.
修改编辑冷藏地点的后台管理页：

http://localhost:5000/blogs