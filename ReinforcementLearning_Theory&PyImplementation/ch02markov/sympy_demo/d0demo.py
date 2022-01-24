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



print('-----------采用符号变量的 subs 方法进行替换操作----------------')
x = symbols('x')
expr = cos(x) + 1
print( expr.subs(x, 0) )

print('-----------将字符串转换为 SymPy 表达式----------------')
str_expr = 'x**2 + 2*x + 1'
expr = sympify(str_expr)
print(expr)
print( expr.subs(x, 1) )

print('-----------将字符串转换为 SymPy 表达式----------------')
p = pi.evalf(3) # pi 保留 3 位有效数字
print(p)