
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
命令行底下运行: jupyter notebook i1spleeter_test.ipynb

替代VOCANO的转录代码：
命令行底下运行: python3 i2polyphonic_test.py

原型合并2个网络的代码（2个网络是概念网络）
python3 i3theory_neuralnetwork.py