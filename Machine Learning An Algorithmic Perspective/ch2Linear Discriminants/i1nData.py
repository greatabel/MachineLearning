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

print("a=", a)
print("b=", b)
c = [a*b for a,b in zip(a,b)]
print(c)