风格检测部分部署ubuntu或者其他linux，或者osx等类unix系统
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

cmd/terminal进入文件夹 后执行：
python3 wsgi.py

6.
浏览器访问：

http://localhost:5000/picture_search

默认账号 greatabel1@126.com ps:abel
自己也可以正常注册

7.
下载 vgg16_weights_tf_dim_ordering_tf_kernels.h5
到 ~/.keras/models/ 目录（mac/linux路径如下）
-(具体参考 https://keras.io/zh/applications/ )
-

8.
如果想自己训练以图搜图：(在安装有库的环境或者虚拟环境)
图片自己根据分类放在static/image/source下 ，修改图片名称，根据已有图片分类
python3 i1offine_train.py

