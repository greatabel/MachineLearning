import numpy as np
import scipy as sp
from termcolor import colored,cprint


def error(f, x,y):
    return sp.sum( (f(x) - y)**2 )

def main():
    N = 3
    x = np.random.rand(N)
    y = np.random.rand(N) * 100
    def f(x):
        return x * 90 + 5
    
    print('x=',x,'y=',y,'f=',f(x),'\n',colored('error=','red'),error(f,x,y))

if __name__ == "__main__":
    main()