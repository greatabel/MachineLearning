# -*- coding: utf-8 -*-
"""


关键帧提取工具

这种关键帧提取算法是基于帧间差异的。

原理很简单
首先，我们加载视频并计算每帧之间的帧间差异

然后，我们可以选择这三种方法中的一种来提取关键帧，分别是
全部基于差分法：
    
1.使用差序
    平均帧间差异最大的前几帧
    被认为是关键帧。
2.使用差异阈值
    平均帧间差异大于
    阈值被认为是关键帧。
3.使用局部最大值
    平均帧间差为局部最大值的帧是
    被认为是关键帧。
    需要注意的是，平滑之前的平均差值
    计算局部最大值可以有效去除噪声以避免
    重复提取相似场景的帧。

经过几次实验，第三种方法具有更好的关键帧提取效果。

""" 
import cv2
import operator
import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy.signal import argrelextrema



class Frame:
    """class to hold information about each frame
    
    """
    def __init__(self, id, diff):
        self.id = id
        self.diff = diff
 
    def __lt__(self, other):
        if self.id == other.id:
            return self.id < other.id
        return self.id < other.id
 
    def __gt__(self, other):
        return other.__lt__(self)
 
    def __eq__(self, other):
        return self.id == other.id and self.id == other.id
 
    def __ne__(self, other):
        return not self.__eq__(other)
 
 
def smooth(x, window_len=13, window='hanning'):
    s = np.r_[2 * x[0] - x[window_len:1:-1],
              x, 2 * x[-1] - x[-1:-window_len:-1]]
    #print(len(s))
 
    if window == 'flat':  # moving average
        w = np.ones(window_len, 'd')
    else:
        w = getattr(np, window)(window_len)
    y = np.convolve(w / w.sum(), s, mode='same')
    return y[window_len - 1:-window_len + 1]
 

def rel_change(a, b):
   x = (b - a) / max(a, b)
   print(x)
   return x
 
def main(movie_name):
    videopath = 'demo_video/'+ movie_name + '.mp4'
    print(sys.executable)
    #Setting fixed threshold criteria
    USE_THRESH = False
    #fixed threshold value
    THRESH = 0.6
    #Setting fixed threshold criteria
    USE_TOP_ORDER = False
    #Setting local maxima criteria
    USE_LOCAL_MAXIMA = True
    #Number of top sorted frames
    NUM_TOP_FRAMES = 50
     
    #Video path of the source file
    # videopath = 'demo_video/blue_earth2.mp4'
    #Directory to store the processed frames
    dir = 'movie/static/img/source/'
    #smoothing window size
    len_window = int(50)
    
    
    print("target video :" + videopath)
    print("frame save directory: " + dir)
    # load video and compute diff between frames
    cap = cv2.VideoCapture(str(videopath)) 
    curr_frame = None
    prev_frame = None 
    frame_diffs = []
    frames = []
    success, frame = cap.read()
    i = 0 
    while(success):
        luv = cv2.cvtColor(frame, cv2.COLOR_BGR2LUV)
        curr_frame = luv
        if curr_frame is not None and prev_frame is not None:
            #logic here
            diff = cv2.absdiff(curr_frame, prev_frame)
            diff_sum = np.sum(diff)
            diff_sum_mean = diff_sum / (diff.shape[0] * diff.shape[1])
            frame_diffs.append(diff_sum_mean)
            frame = Frame(i, diff_sum_mean)
            frames.append(frame)
        prev_frame = curr_frame
        i = i + 1
        success, frame = cap.read()   
    cap.release()
    
    # compute keyframe
    keyframe_id_set = set()
    if USE_TOP_ORDER:
        # sort the list in descending order
        frames.sort(key=operator.attrgetter("diff"), reverse=True)
        for keyframe in frames[:NUM_TOP_FRAMES]:
            keyframe_id_set.add(keyframe.id) 
    if USE_THRESH:
        print("Using Threshold")
        for i in range(1, len(frames)):
            if (rel_change(np.float(frames[i - 1].diff), np.float(frames[i].diff)) >= THRESH):
                keyframe_id_set.add(frames[i].id)   
    if USE_LOCAL_MAXIMA:
        print("Using Local Maxima")
        diff_array = np.array(frame_diffs)
        sm_diff_array = smooth(diff_array, len_window)
        frame_indexes = np.asarray(argrelextrema(sm_diff_array, np.greater))[0]
        for i in frame_indexes:
            keyframe_id_set.add(frames[i - 1].id)
            
        plt.figure(figsize=(40, 20))
        # plt.locator_params(numticks=100)
        plt.locator_params(axis='both', nbins=10)
        plt.stem(sm_diff_array)
        plt.savefig(dir + movie_name + '_plot.png')
    
    # save all keyframes as image
    cap = cv2.VideoCapture(str(videopath))
    curr_frame = None
    keyframes = []
    success, frame = cap.read()
    idx = 0
    while(success):
        if idx in keyframe_id_set:
            name = movie_name +"_keyframe_" + str(idx) + ".jpg"
            cv2.imwrite(dir + name, frame)
            keyframe_id_set.remove(idx)
        idx = idx + 1
        success, frame = cap.read()
    cap.release()

if __name__ == "__main__":

    main('blue_earth2')
