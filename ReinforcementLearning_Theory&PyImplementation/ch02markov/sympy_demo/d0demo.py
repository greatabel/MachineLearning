from sympy import *
# https://zhuanlan.zhihu.com/p/111573239

vars = symbols('x_1:5')
print(vars)

print('---------------------------')
x, y, z = symbols('x y z')
print(x, y, z)

y = expand((x + 1)**2) # expand() 是展开函数
z = Rational(1, 2) # 构造分数 1/2

print(x, y, z)
print('---------------------------')


# 采用符号变量的 subs 方法进行替换操作，例如：
x = symbols('x')
expr = cos(x) + 1
print( expr.subs(x, 0) )
