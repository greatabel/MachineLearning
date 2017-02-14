import random

Out = []

# Array: Memory weights
Wgh = []

Inp = []

# abel hard code:
# Inp = [ [1,2],[10,20],[100, 200]
#         ]
for i in range(5):
    Inp.append([random.uniform(-10.0, 10.0), random.uniform(-10.0, 10.0)])
    Wgh.append([random.uniform(-10.0, 10.0), random.uniform(-10.0, 10.0)])
    Out.append(random.choice([True, False]))
print('Inp=', Inp)

# constants of the rigid parameters
Thr = 2.0


print('\nWgh:', Wgh)
Sum = 0
for i, elem in enumerate(Inp):
    print('\nindex=', i,Inp[i])
    # Perceptron caculateion for the case
    Sum += Inp[i][0] * Wgh[i][0] + Inp[i][1] * Wgh[i][1]
    print('Sum=', Sum)
    
    if Sum > Thr:
        Axn = 1
    else:
        Axn = 0
    print('Axn:', Axn)

    Err = Out[i] - Axn
    print('Err=', Err)
