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

print(colored('# Creating an array','blue'))
arr = np.arange(10,20)
print('arr=', arr)

print('# Creating the index array')
index = np.where(arr > 15)
print('index = np.where(arr > 15) index = ',index)

new_arr = arr[index]
print('new_arr = arr[index]  new_arr=',new_arr )

print('delete')
new_arr = np.delete(arr, index)
print('new_arr =', new_arr)
print('arr=', arr)



