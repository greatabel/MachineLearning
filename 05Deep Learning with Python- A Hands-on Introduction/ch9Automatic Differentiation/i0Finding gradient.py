#Wrapper Around Numpy
import autograd.numpy as numpy
#Function to generate gradients
from autograd import grad
#Define the function
def f(x1, x2): return numpy.sqrt(x1 * x1 + x2 * x2)
#Compute the gradient w.r.t the first input variable x1
g_x1_f = grad(f,0)
#Compute the gradient w.r.t the second input variable x2
g_x2_f = grad(f,1)
#Evaluate and print the value of the function at x1=1, x2=2
print( f(1,2) )
#Produces 2.23
#Evaluate and print the value of the gradient w.r.t x1 at x1=1, x2=2
print( g_x1_f(1,2) )
#Produces 0.44
#Evaluate and print the value of the gradient w.r.t x2 at x1=1, x2=2
print( g_x2_f(1,2) )
#Produces 0.89
