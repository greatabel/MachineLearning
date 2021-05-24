检测部分推荐部署ubuntu或者其他linux，
其他代码可以部署到其他操作系统平台

1.
安装python3.6 以上版本

2. 
安装pip3 
https://www.runoob.com/w3cnote/python-pip-install-usage.html

3.
可选（创建python3虚拟目录，隔绝不同版本库之间相互影响）
https://docs.python.org/zh-cn/3/tutorial/venv.html
windows用户：https://www.codenong.com/41501636/

4.
terminal底下进入工程目录下，在requirements.txt同级目录下运行：
pip3 install --upgrade -r requirements.txt


5.
terminal 里面cd 到 a12387_fraud_detect文件夹

then enter virtual environment:
Windows run:
movie-env\Scripts\activate.bat

Unix/MacOS run:
source movie-env/bin/activate

6.
打开浏览器访问：
http://127.0.0.1:5000/predict/

可选：
（如果需要查看模型训练模型时候,可以运行i0detect.ipynb
然后访问：
http://localhost:8888/notebooks/i0detect.ipynb）







