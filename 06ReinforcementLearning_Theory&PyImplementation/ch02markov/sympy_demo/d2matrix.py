from sympy import *
# https://zhuanlan.zhihu.com/p/111573239

print('-------------构造矩阵--------------')
m0 = Matrix([[1, -1], [3, 4], [0, 2]])
print(m0)

print('-------------构造列向量--------------')
m1 = Matrix([1, 2, 3])
print(m1)
print('-------------构造行向量--------------')
print(m1.T)
print('-------------构造单位矩阵-------------')
print( eye(4) )


print('-------------Solve the following system-------------')
'''
   x + 4 y ==  2
-2 x +   y == 14
'''

from sympy import Matrix, solve_linear_system
x, y = symbols('x y')

system = Matrix([ [1, 4, 2], [-2, 1, 14] ])
s = solve_linear_system(system, x, y)
print(s)