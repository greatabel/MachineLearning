from sympy import *
# https://zhuanlan.zhihu.com/p/111573239
import numpy

a = numpy.pi / 3
x = symbols('x')
expr = sin(x)

f = lambdify(x, expr, 'numpy')
print( f(a) )
print( expr.subs(x, pi/3) )


print('-------------使用 simplify (化简)--------------')
s = simplify(sin(x)**2 + cos(x)**2)
print(s)

alpha_mu = symbols('alpha_mu')
s1 = simplify(2*sin(alpha_mu)*cos(alpha_mu))
print(s1)