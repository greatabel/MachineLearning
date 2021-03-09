import numpy as np
from scipy import spatial

def euc_distance(v1, v2):
    """用欧氏距离判断相似距离"""
    return np.linalg.norm(np.array(v1) - np.array(v2))

def cos_similar(v1, v2):
    """用余弦向量判断相似程度"""
    return 1 - spatial.distance.cosine(np.array(v1), np.array(v2))


puppy_vec = [1.0, 0.0] + [0.0] * 998
dog_vec = [0.0, 1.0] + [0.0] * 998
some_word_vec = [0.0] * 499 + [1.0] + [0.0] * 500

print(euc_distance(puppy_vec, dog_vec))
print(euc_distance(puppy_vec, some_word_vec))
print(cos_similar(puppy_vec, dog_vec))
print(cos_similar(puppy_vec, some_word_vec))