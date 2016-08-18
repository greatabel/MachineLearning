from termcolor import colored
import numpy as np



alist = [[1,2],[3,4]]
print(colored(alist, 'red'))
print('alist[0][1]=',alist[0][1])

print(colored('# Converting the list defined above into an array','green'))
arr = np.array(alist)
print('arr[0,1] =', arr[0,1])
print('arr[:,1] =',arr[:,1])
print('arr[1,:] =',arr[1,:])

