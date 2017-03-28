import numpy as np

w = np.array([1,2,3])
x = np.array([4,5,6])

answer = 0
for i in range(len(x)):
  answer += w[i]*x[i]
print('method1:answer=', answer)
print('method2: using numpy')
np_answer = w.dot(x)
print('w=',w)
print('x=',x)
print('w.dot(x)=', np_answer)


