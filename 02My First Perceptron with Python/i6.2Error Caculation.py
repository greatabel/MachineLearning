import random

Out = []

# Array: Memory weights
Wgh = [0.0, 0.0]

Inp = []

Wgh[0] = random.uniform(-1.0, 1.0)
Wgh[1] = random.uniform(-1.0, 1.0)

# abel hard code:
# Inp = [ [1,2],[10,20],[100, 200]
#         ]
for i in range(5):
    Inp.append([random.uniform(-10.0, 10.0), random.uniform(-10.0, 10.0)])

    Out.append(random.choice([True, False]))

for i, elem in enumerate(Inp):
    print('Inp[',i,']=', elem)
print('Expected Out=', Out)
print('Wgh=', Wgh)

# constants of the rigid parameters
Thr = 2.0


for i, elem in enumerate(Inp):
    print('\n turn:', i,'Inp=',Inp[i])
    # Perceptron caculateion for the case
    Sum = Inp[i][0] * Wgh[0] + Inp[i][1] * Wgh[1]
    
    if Sum > Thr:
        Axn = 1
    else:
        Axn = 0

    Err = Out[i] - Axn
    print('Sum=', Sum, 'Axn:', Axn, 'Expected Out=', Out[i], 'Err=', Err)
