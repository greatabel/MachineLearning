# 新修改运行：

ubuntu(我是在ubuntu 18.04）或者其他linux，或者osx等类unix系统
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
（可选：如果自己有gpu，可以根据requirements.txt中提示，修改requirements.txt)

5.

python3 launcher.py --exp_type=pg_re --simu_len=5 --num_ex=10 --ofile=data/pg_re --out_freq=10


项目改进主要集中在：
1. 升级原始版本py2.7 到 py3.6及以上
2. 去掉theano所有代码，替换为tensorflow实现
3. 去掉theano相关的依赖代码pg_network，改成numpy+tensorflow
4. 在新的1，2，3 运行园项目的discounted reward和slowd的对比图，表明效果的改善（比如slowdown 均工作放缓时间比theano版本改进了）
    （新对比图在data/pg_re_lr_curve.pdf）


# ------------------------------------------------------------------------

# 下面是旧的原始Theano版本工程的readme.md：

# DeepRM
HotNets'16 http://people.csail.mit.edu/hongzi/content/publications/DeepRM-HotNets16.pdf

Install prerequisites

```
sudo apt-get update
sudo apt-get install python-numpy python-scipy python-dev python-pip python-nose g++ libopenblas-dev git
pip install --user Theano
pip install --user Lasagne==0.1
sudo apt-get install python-matplotlib
```

In folder RL, create a data/ folder. 

Use `launcher.py` to launch experiments. 


```
--exp_type <type of experiment> 
--num_res <number of resources> 
--num_nw <number of visible new work> 
--simu_len <simulation length> 
--num_ex <number of examples> 
--num_seq_per_batch <rough number of samples in one batch update> 
--eps_max_len <episode maximum length (terminated at the end)>
--num_epochs <number of epoch to do the training>
--time_horizon <time step into future, screen height> 
--res_slot <total number of resource slots, screen width> 
--max_job_len <maximum new job length> 
--max_job_size <maximum new job resource request> 
--new_job_rate <new job arrival rate> 
--dist <discount factor> 
--lr_rate <learning rate> 
--ba_size <batch size> 
--pg_re <parameter file for pg network> 
--v_re <parameter file for v network> 
--q_re <parameter file for q network> 
--out_freq <network output frequency> 
--ofile <output file name> 
--log <log file name> 
--render <plot dynamics> 
--unseen <generate unseen example> 
```


The default variables are defined in `parameters.py`.


Example: 
  - launch supervised learning for policy estimation 
  
  ```
  python launcher.py --exp_type=pg_su --simu_len=50 --num_ex=1000 --ofile=data/pg_su --out_freq=10 
  ```
  - launch policy gradient using network parameter just obtained
  
  ```
  python launcher.py --exp_type=pg_re --pg_re=data/pg_su_net_file_20.pkl --simu_len=50 --num_ex=10 --ofile=data/pg_re
  ```
  - launch testing and comparing experiemnt on unseen examples with pg agent just trained
  
  ```
  python launcher.py --exp_type=test --simu_len=50 --num_ex=10 --pg_re=data/pg_re_1600.pkl --unseen=True
  ```

