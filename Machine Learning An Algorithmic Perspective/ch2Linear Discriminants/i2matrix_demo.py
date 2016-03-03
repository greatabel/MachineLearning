from numpy import *

a = array([[3,4,5],[6,7,8]])
b = array([[10,20],[10,40],[10,60]])
c = dot(a,b)
print(a)
print(b)
print('-'*10)
print(c)

print(" 'where' function demo:")
# http://ilanever.com/article/detail.do;jsessionid=C3D1AB96550C8CED231EB3B3B08FD26B?id=427
x = array([1,2,3,4])
y = array([10,20,30,40])
condition = array([True,True,False,False])
z = where(condition,x,y)
print(x,"\n",y,"\n",z)