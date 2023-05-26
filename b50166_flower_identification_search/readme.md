检测最好使用ubuntu或者其他linux，或者osx等类unix系统
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

http://localhost:5000/home

默认管理员账号 greatabel1@126.com ps:abel
自己也可以正常注册


非管理员账号：test@126.com
密码：test

<!-- 7.
如果想自己训练以图搜图分类：(在安装有库的环境或者虚拟环境)
python3 i1offine_train.py

-->



# ----- start of requirement -------

1. 可能是基于神经网络restnet那种
2. 准备好一批花卉素材，提前利用我们的restnet训练好结果
3. 然后在后端实现神经网络的api化，方便移动端调用
4. 移动端估计就是android app使用webview封装一个html5页面做识别，android app本身估计就是java /或者kotlin编写，webiview调用后端api 的神经网络模型，对用户上传图谱进行识别
5.  模型的后端api 可能需要部署到 阿里云ecs服务器ubuntu（公网ip），这样android apk才可以访问到
6.  （可选）提供部署脚本和部署自动化文件，阿里云ecs服务器去部署好

# ----- end   of requirement -------





