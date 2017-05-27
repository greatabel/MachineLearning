import pylab
import numpy

x = numpy.linspace(-1, 1 , 100)
signal = 2 + x + 2 * x * x
noise = numpy.random.normal(0, 0.1, 100)
y = signal + noise
# print('x=', x, '\ny=', y)
pylab.plot(signal, 'b')
pylab.plot(y, 'g')
pylab.plot(noise, 'r')
pylab.xlabel("x")
pylab.ylabel("y")
pylab.legend(["Without Noise", "With Noise", "Noise"], loc = 2)

pylab.show()