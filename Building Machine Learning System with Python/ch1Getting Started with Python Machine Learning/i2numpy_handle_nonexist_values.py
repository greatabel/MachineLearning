from termcolor import colored,cprint
import numpy as np


if __name__ == "__main__":
    print(colored( 'Handling nonexisting values:', 'red'))
    c = np.array([1,2,np.NAN,3,4])
    print("c = np.array([1, 2, np.NAN, 3, 4]) # let's pretend we have read this" +
        "from a text file")
    print('c=', c)
    print(colored( 'np.isnan(c)', 'red'))
    print(np.isnan(c))
