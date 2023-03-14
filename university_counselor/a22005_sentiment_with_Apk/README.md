在mac/ubuntu18.04系统上测试过，windows应该可以，但是没测试过windows

1.
安装python3.6 以上版本

2. 
安装pip3 

3.
可选  可以不做（创建python3虚拟目录，隔绝不同版本库之间相互影响）
https://docs.python.org/zh-cn/3/tutorial/venv.html

4.
4.1
terminal底下进入工程目录下，在requirements.txt同级目录下运行：
pip install --upgrade -r requirements.txt

5.
运行后端api和Pc站，
进入i4security_predict_web
模拟运行在:
命令行底下运行: python3 i4wsgi.py


6.
已经注册好的账号 可以直接登录：
http://localhost:5000/home

username: greatabel1@126.com 
password: abel
你也可以自己注册和登录

如果想访问单独的登陆页，可以访问：
http://localhost:5000/single_login

# ------------ ------------ ------------ ------------ 

7.

运行机器学习训练模型部分：
jupyter notebook i2deep-learning-for-sentiment-analysis.ipynb
查看点击网站的ML button，或者
打开浏览器：http://localhost:8888/notebooks/i2deep-learning-for-sentiment-analysis.ipynb

8.
（********可选********）
获得更多数据
在mac/ubuntu系统：
下载直接在命令行运行：

（查看本地chrome浏览器版本，替换chrome文件夹中chromedriver为相应版本:
https://chromedriver.chromium.org/downloads)

可以抓取环球网相关新闻和咨询，然后进行筛选
python3  i0scrapy_huanqiu.py


可以抓取本地新浪网相关新闻资讯，然后进行筛选
python3  i1scrapy_localnews.py

