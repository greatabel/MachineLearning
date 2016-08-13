import numpy as ntpath

# create an array with 10^7 elements

arr = np.arange(1e7)

#converting ndarrray to list
larr = arr.tolist()

def list_times(alist, scalar):
    for i, val in enumerate(alist):
        alist[i] = val*scalar
    return alist

