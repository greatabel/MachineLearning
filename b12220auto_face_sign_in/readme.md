检测部分推荐部署ubuntu或者其他linux，或者osx等类unix系统
其他系统没有经过充分测试

1.
安装python3.6 以上版本

1.1
安装
brew link libpng
（否则requirements.txt中的zlib安装会有问题）

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



6.
另外开一个命令行，进入i3sentiment_predict_web
进入虚拟环境
执行：app.py

7.
访问：
http://127.0.0.1:5000/home

8.
实际使用工程，请将i0FaceDetectionFlask 部署在公共云平台（至少需要公开的ip和端口，提供给其他端访问）

9.
（可选）
方法1:使用andriod studiao打开 i1android_app 工程
然后编译到自己手机上
方法2:使用b12220auto_face_sign_in/i1android_app/app/build/outputs/apk/debug/app-debug.apk 
传到自己手机上
（ 如果需要修改后端地址，可以更新b12220auto_face_sign_in/i1android_app/app/src/main/assets/test.html 
的28行)