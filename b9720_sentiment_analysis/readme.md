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
在命令行下，（进入虚拟环境， 如果设置过虚拟环境）
运行：jupyter notebook i1deep-learning-for-sentiment-analysis.ipynb 


9.

然后浏览器访问：http://localhost:8888/notebooks/i1deep-learning-for-sentiment-analysis.ipynb

10.
另外开一个命令行，进入i3sentiment_predict_web
进入虚拟环境
执行：app.py