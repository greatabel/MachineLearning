import random

def print_bold(msg, end='\n'):
    print("\033[1m" + msg + "\033[0m", end=end)

Out = []

# Array: Memory weights
Wgh = [0.0, 0.0]

Inp = []

# Wgh[0] = random.uniform(-1.0, 1.0)
# Wgh[1] = random.uniform(-1.0, 1.0)

# Constants of the Rigid parameters
Proportion_Learning_factor = 1

# abel hard code:
# Inp = [ [1,2],[10,20],[100, 200]
#         ]
for i in range(4):
    Inp.append([random.uniform(-10.0, 10.0), random.uniform(-10.0, 10.0)])

    Out.append(random.choice([True, False]))

for i, elem in enumerate(Inp):
    print('Inp[',i,']=', elem)
print('Expected Out=', Out)
print('Wgh=', Wgh)

# constants of the rigid parameters
Thr = 2.0

j = 0
k = 1000
while True:
    j += 1

    NEr = 0
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

        if Err != 0:
            NEr += 1
            Wgh[0] += Proportion_Learning_factor * Err * Inp[i][0]
            Wgh[1] += Proportion_Learning_factor * Err * Inp[i][1]
            print('Wgh=', Wgh)
            
    print_bold('#'*10 + "j=" + str(j))

    if NEr == 0:
        break

    if j >= k:
        break
