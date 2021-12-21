负载调优模拟部分部署ubuntu或者其他linux，或者osx等类unix系统
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
python3 i0simulate_edge_compute.py

6.
cpu_timecounsume_compare.png
heat_heavy_compare.png
是对比图，分值越高越好

i1heuristic_algorithm_cpu_timecounsume.png
i1heuristic_algorithm_heat_heavy.png
i2qlearning_cpu_timecounsume.png
i2qlearning_heat_heavy.png
是强化学习阶段学习过程图

