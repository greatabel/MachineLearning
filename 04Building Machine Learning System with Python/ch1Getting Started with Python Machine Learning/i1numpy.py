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

    d = np.array([10,20,30,40,50])
    print(d,'d*2=',d*2,'d**2=',d**2)
    print('d[np.array([2,3,4])]=',d[np.array([2,3,4])])
    print(d>30,'d[d>30]=',d[d>30])
    print('numpy.clip(a,a_min,a_max,a=None)的运用：方法解释：Clip（limit）the values in the array.'+
          '这个方法会给出一个区间，在区间之外的数字将被剪除到区间的边缘，例如给定一个区间[0,1]，则小于0的  将变成0，大于1则变成1.')
    print('d.clip(15,40)=',d.clip(15,40))