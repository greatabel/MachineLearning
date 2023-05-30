# 部署文档

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



6.
数据探索 可视化
python3 i1good_case.py


7.（可选，可以不用部署允许，已经运行出结果）
python3 i0bad_case.py


# ---- start of requirements ------
 1. 采集视频（我已经找到一些网上）
2. 处理好视频（找到需要的部分，飞机舱视角）
3. 写好算法处理部分：opencv算法+形态学+canny算子+机器学习 就行
4. 接入算法和视频读取，展示，算法增强绘制跑道红线
5. 部署文档和依赖包管理"
# ---- end of requirements ------