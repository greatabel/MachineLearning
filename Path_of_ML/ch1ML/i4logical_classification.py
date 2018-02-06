import numpy as np

# 函数y = 2*x^2 + 1*x + 3
y = np.poly1d([2, 1, 3])

print(y, '\ny(-7)=', y(-7))