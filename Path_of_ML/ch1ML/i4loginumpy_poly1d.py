import numpy as np

# 函数y = 2*x^2 + 1*x + 3
y = np.poly1d([2, 1, 3])

print(y, ' ( x= -7) =', y(-7))

# true 代表 y = (x - 1)(x - 2)(x - 3)
y1 = np.poly1d([1, 2, 3], True)
print(y1, ' (x = 3) =', y1(3))