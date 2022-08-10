
1.
安装python3.6 以上版本

2. 
安装pip3 
（如果网速慢 可以pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package  把some-package替换成自己的慢的包 )

3.
可选  可以不做（创建python3虚拟目录，隔绝不同版本库之间相互影响）
https://docs.python.org/zh-cn/3/tutorial/venv.html

4.
4.1
terminal底下进入工程目录下，在requirements.txt同级目录下运行：
pip3 install --upgrade -r requirements.txt

5.
需要处理的pdf都放在data文件夹即可，默认处理pdf

模拟运行在:
jupyter notebook i1ML_of_android_security.ipynb

开一个新的命令行：
命令行下进入 i4security_predict_web
python3 i4wsgi.py

6.
apk查看或者安装，请在android studio中打开 i5android_client工程

7.
（可选项）
如果买家不只是想展示和查看jupyter代码，还想自己训练和跑出来
那就需要安装和部署:
pip3 install --upgrade -r  full_requirements.txt
然后再再 i1ML_of_android_security.ipynb 中执行

8.
（可选项）
如果想查看浏览器pc站后端，浏览器访问：

http://localhost:5000/home

已经注册好的账号 可以直接登录：
greatabel1@126.com  abel
你也可以自己注册和登录
