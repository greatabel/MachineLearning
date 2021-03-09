# for data in range(nData):
#     for n in range(N):
#         activation[data][n] = 0
#         for m in range(M+1):
#             activation[data][n] += weight[m][n] * inputs[data][m]

#         # now dicide wether the neuron fires or not
#         if activation[data][n] > 0:
#             activation[data][n] = 1
#         else:
#             activation[data][n] = 0
a = [1,2,3]
b = [4,5,6]

print('0 intuitive way:')
ab = []
for i in range(0, len(a)):
    ab.append(a[i]*b[i])
print(ab)

print('1 better way:')
print("a=", a)
print("b=", b)
c = [a*b for a,b in zip(a,b)]
print(c)

print('2 other way : use numpy')
import numpy as np

a1 = np.array(a)
b1 = np.array(b)
print(a1*b1)