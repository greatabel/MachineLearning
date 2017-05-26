import pylab
import numpy

x = numpy.linspace(-1, 1 , 10)
signal = 2 + x + 2 * x * x
noise = numpy.random.normal(0, 0.1, 10)
y = signal + noise
print('x=', x, 'y=', y)