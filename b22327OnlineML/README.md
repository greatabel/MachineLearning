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
pip install --upgrade -r requirements.txt

5.
模拟运行在:
python3 i1wsgi.py



6.
浏览器访问：

http://localhost:5000/home

已经注册好的管理员账号 可以直接登录：
管理员1
username: greatabel1@126.com 
password: abel
你也可以自己注册和登录

管理员2
username: admin@126.com
password: admin

-------------------
一般用户测试账号:
username:test@126.com   
password: test

7.
个人主页： http://localhost:5000/profile


# ------ 需求 -------

1.用户注册登陆、个人主页包含你说的部门 科室
2.excel需要导出成统一的csv格式 进行统一上传，才可以在线编辑
3.在线修改和历史记录追踪
4 下载功能
5.设置不同用户权限，用户系统管理