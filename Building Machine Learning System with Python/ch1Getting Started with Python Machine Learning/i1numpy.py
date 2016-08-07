import numpy as np

if __name__ == "__main__":
    print(np.version.full_version)
    a = np.array([0,1,2,3,4,5])
    print('a=',a,'a.ndim=',a.ndim, a.shape)

    b = a.reshape((3,2))
    print('b=',a,'b.ndim=',b.ndim, b.shape)
    b[1][0] = 77
    print('b=',b,'a=',a)

    c = a.reshape((3,2)).copy()
    print('c=',c)
    c[0][0] = -99
    print('c=',c,'a=',a)