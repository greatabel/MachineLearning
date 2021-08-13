检测部分推荐部署ubuntu或者其他linux，或者osx等类unix系统
其他系统没有经过充分测试，过程稍有不同

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
运行现有的分析和训练：

在命令行下，（进入虚拟环境， 如果设置过虚拟环境）
运行：python3 i1native_bayes.py 即可

6.（可选）
目前我就标记了十几个数据，你可以在i0procssed_with_datatagging.csv的头十几个就是。
如果将来想要增加的标记好的数据集，可以这样：
6.1
 替换samples.txt为你的新的数据原始文本
6.2
 运行 i0prreprocessing.py
6.3
 在新生成的i0processed.csv 上面进行标记标记规则如下：

标记规则（正向标记sentiment列为1， 负向为0，无法判断就为-1）

6.4
 手工把标记好的数据集复制到i0addtiaonla_content.csv最后面

6.5
 然后执行步骤5
