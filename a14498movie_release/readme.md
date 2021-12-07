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

8.
（可选项）
虽然我已经分析了近期数据社交网络可视化部分，
如果想自己进行分析，可以运行：
python3 i2data_anlysis.py
如果想要替换网站的可视化结果，需要把生成的i3data_visialization文件夹替换网站中对应的文件夹

9.
（可选项)
i2sentiment_analysis
和
i1SGScrapy 已经下载和训练完毕。
如果将来需要运行，单独参考其中的readme.md文件
进入i2sentiment_analysis然后运行：jupyter notebook i2deep-learning-for-sentiment-analysis.ipynb
然后浏览器访问：http://localhost:8888/notebooks/i1deep-learning-for-sentiment-analysis.ipynb



