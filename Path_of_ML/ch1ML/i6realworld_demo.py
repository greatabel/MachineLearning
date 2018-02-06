import random
import numpy as np


x_0 = random.uniform(-10, 10)
y_0 = random.uniform(-10, 10)
print(x_0, y_0)

y = np.poly1d([2, 0, 3])
d_yx = np.polyder(y)



def step(x, d_yx):
    alpha = .2
    return x - alpha*d_yx(x)

print(step(x_0, d_yx))

x = x_0
x_list = [x]
for i in range(20):
    x = step(x, d_yx)
    x_list.append(x)

print(x_list)