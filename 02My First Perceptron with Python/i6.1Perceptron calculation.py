import random
# Array: Memory weights
Wgh = [0.0, 0.0]

Inp = []

# abel hard code:
# Inp = [ [1,2],[10,20],[100, 200]
#         ]
for i in range(5):
    Inp.append([random.uniform(-10.0, 10.0), random.uniform(-10.0, 10.0)])

print('Inp=', Inp)

# constants of the rigid parameters
Thr = 2.0

Wgh[0] = random.uniform(-1.0, 1.0)
Wgh[1] = random.uniform(-1.0, 1.0)

print('Wgh:', Wgh)

for i, elem in enumerate(Inp):
    print('\nindex=', i,Inp[i])
    # Perceptron caculateion for the case
    Sum = Inp[i][0] * Wgh[0] + Inp[i][1] * Wgh[1]
    print('Sum=', Sum)
    if Sum > Thr:
        Axn = 1
    else:
        Axn = 0
    print('Axn:', Axn)