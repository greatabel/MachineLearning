# 新修改运行：

ubuntu(我是在ubuntu 18.04）或者其他linux，或者osx等类unix系统
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
（可选：如果自己有gpu，可以根据requirements.txt中提示，修改requirements.txt)

5.
进行数据探索和展示
python3 i1data_explore.py

6.
(先导步骤：需要重新执行第四步，或者单独安装jupyter：pip install jupyter)
查看残差深度神经网络的工程可以，另外新建一个窗口，然后执行：
jupyter notebook i2ml_calassify_asphalt_resnets.ipynb
