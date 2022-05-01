

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
python3 wsgi.py



6.
浏览器访问：

http://localhost:5000/home

已经注册好的账号 可以直接登录：
username: greatabel1@126.com 
password: abel
你也可以自己注册和登录

7.
个人主页： http://localhost:5000/profile




---------- ---------- 可选项 ---------- ---------- 
从步骤8开始都是可选项，不是必须
---------- ---------- 可选项 ---------- ---------- 

8.
目前是技术原型展示，我并没有添加所有的数据到数据库和es仓库。

如果想要自己后续添加或者修改编辑内容的后台管理页：
http://localhost:5000/blogs

增加出去爬虫之外的数据导入，比如pdf文本导入到系统或者es中：
可以点击 add doc连接，自己从pdf上copy文字输入到列表中；
或者命令行下：python3 i0ocr.py (记得修改14行的文件名，获得processeddata的text，目前60-70%准确度)然后再复制黏贴

9.
因为我在关系型数据库搜不到时候，会从es中读取。
如果想部署好备用的es：
(可选) docker 安装elasticsearch
docker pull docker.elastic.co/elasticsearch/elasticsearch:7.16.3

docker run -p 127.0.0.1:9200:9200 -p 127.0.0.1:9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.16.3


测试：curl -X GET "localhost:9200/_cat/nodes?v=true&pretty"
参考文档： https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html
-

单独在python2.7 下面pip install crawley


10.
数据已经下载好，放在data文件夹下，可以不用再下载。
如果想下载：
下载对应自己电脑系统版本的chromedriver 放在 downloader/i2SGScrapy/
可以运行抓取爬虫：i0scrapy_huanqiu.py
