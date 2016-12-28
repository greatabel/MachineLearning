from pylab import *
from numpy import *
import linreg

# auto = genfromtxt('./auto-mpg.data.txt',comments='"')
auto = loadtxt('auto-mpg-data/auto-mpg.data_after.txt',comments='"')
print(len(auto))

trainin=auto[::2,:8]
testin=auto[1::2,:8]
traintgt=auto[::2,1:2]
testtgt=auto[1::2,1:2]


beta = linreg.linreg(trainin,traintgt)
testin = concatenate((testin,-ones((shape(testin)[0],1))),axis=1)
testout = dot(testin,beta)
error = sum((testout - testtgt)**2)
print(error)