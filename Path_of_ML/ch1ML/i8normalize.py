import numpy as np


# 两条特征向量
f1 = np.array([0.2, 0.5, 1.1]).reshape(-1, 1)
f2 = np.array([-100.0, 56.0, -77.0]).reshape(-1, 1)

# 计算归一化
f1_scaled = (f1 - np.mean(f1)) / np.std(f1)
f2_scaled = (f2 - np.mean(f2)) / np.std(f2)

print(f1, '@'*5, f2)
print(f1_scaled, '#'*5, f2_scaled)

# 用sklearn封装的函数计算归一化
import sklearn.preprocessing as preprocessing
scaler = preprocessing.StandardScaler()
f1_sk_scaled = scaler.fit_transform(f1)
f2_sk_scaled = scaler.fit_transform(f2)

assert np.allclose(f1_sk_scaled, f1_scaled) and np.allclose(f2_sk_scaled, f2_scaled)