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
自行安装中文处理分词和中文字典库
!pip install --upgrade paddlepaddle -i https://mirror.baidu.com/pypi/simple
!pip install --upgrade paddlehub -i https://mirror.baidu.com/pypi/simple

https://github.com/PaddlePaddle/PaddleHub/blob/release/v2.1/README_ch.md paddlehub的相关介绍
我们使用了他的vocabuary和分词


替换的情感词介绍在mydata/情感词汇本体 好像是大林鸿飞教授开源的，可以论文引用里面写下
不过你原来的情感词我也翻译后加入到最上面了

处理的语料来自你原来提供的文件夹

5.
terminal底下进入工程目录下，在requirements.txt同级目录下运行：
pip3 install --upgrade -r requirements.txt


6.
根据需要 修改要处理的数据集（默认是foods）
修改asum_main.py的23，24行后，
cmd/terminal进入文件夹 后执行：
python3 asum_main.py

tips：
第一次运行，paddle下载相关模型需要一段时间，请耐心等待
根据自己机器性能（cpu，内存，时间）
模型迭代次数在 asum_main.py 56行修改，
还有数据集的长度自己修改下。否则可能比较好耗时。你自己在预料大小和迭代次数试验，达到一个平衡

