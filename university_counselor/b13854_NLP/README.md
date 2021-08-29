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


4.2
数据准备：

数据集介绍： data/Data_README.md

全量数据集下载（可选）：https://ai.google.com/research/NaturalQuestions/download （16G） 
可下载可不下载，我已经给你分割出中小量数据集，方便跑，在data/文件夹。全量已经帮你跑过了在5.2

下载（必须）
https://dl.fbaipublicfiles.com/fasttext/vectors-english/wiki-news-300d-1M.vec.zip
解压后放在和readme.md平级目录，一共wiki-news-300d-1M.vec 2.26G

model.h5 其他模型 105M 已经给你训练好，打包在工程目录下
还有其他pickle中间文件已经生成，不要删除


5.0
 i0.py 不用执行，我已经处理了
5.1
可以执行 i1data_explore.py 进行数据探索，为模型提供思路
terminal底下运行：
python3 i1data_explore.py
5.2
主要是训练部分，和交叉验证训练的有效性（可选择，可以不允许，我已经在16G全量数据训练）
python3 i2my_lstm_train.py
5.3

主要是调用训练好模型，进行对问题在维基百科文章中的长短答案进行预测
python3 i3load_and_test_model.py