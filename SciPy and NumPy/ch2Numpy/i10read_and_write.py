from termcolor import colored,cprint

import numpy as np
import numpy.random as rand

# Opening the text file with the 'r' option, # which only allows reading capability
f = open('i10somefile.txt', 'r')
# Parsing the file and splitting each line, # which creates a list where each element of # it is one line
alist = f.readlines()
cprint(alist, 'green', 'on_red')
# Closing file 
f.close()

# After a few operations, we open a new text file
# to write the data with the 'w' option. If there
# was data already existing in the file, it will be overwritten.
f = open('i10somefile.txt', 'w')
# Writing data to file 
newdata = "1 2 3"
f.writelines(newdata)

# Closing file 
f.close()