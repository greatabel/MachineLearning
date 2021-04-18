检测部分推荐部署ubuntu或者其他linux，
其他代码可以部署到其他操作系统平台

1.
安装python3.6 以上版本

2. 
安装pip3 

3.
可选（创建python3虚拟目录，隔绝不同版本库之间相互影响）
https://docs.python.org/zh-cn/3/tutorial/venv.html

4.


terminal底下进入工程目录下，在requirements.txt同级目录下运行：
pip3 install --upgrade -r requirements.txt


5.
terminal 里面cd 到 a11009patient文件夹

then enter virtual environment:
Windows run:
movie-env\Scripts\activate.bat

Unix/MacOS run:
source movie-env/bin/activate

6.
Ubuntu 18.04 安装 RabbitMQ 和配置：
https://wangxin1248.github.io/linux/2020/03/ubuntu-install-rabbitmq.html
根据博客链接完成第六步的rabgitMQ server运行起来

7.
新开一个命令行，进入虚拟环境，进入a11009patient/i2website下，运行
python3 app.py

