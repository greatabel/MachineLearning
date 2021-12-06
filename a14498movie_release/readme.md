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
运行起来整个网站  可以在terminal中:
python3 i4wsgi.py
然后访问：http://localhost:5000/home

已经注册好的账号 可以直接登录：
username: greatabel1@126.com 
password: abel
你也可以自己注册和登录

6.
修改个人主页： http://localhost:5000/profile
修改编辑电影实体的后台管理页：http://localhost:5000/blogs

7.
（可选项）
虽然我已经分析了近期数据社交网络结构图，
如果想自己进行分析，可以运行：
python3 i1network_analysis.py
(分析不同电影，自行修改i1network_analysis.py的第10行和第90行中对应的文件名字)