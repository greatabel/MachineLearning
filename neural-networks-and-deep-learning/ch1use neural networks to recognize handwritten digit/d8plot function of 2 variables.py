import numpy as np

from pylab import meshgrid

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt

from termcolor import colored

# https://glowingpython.blogspot.com/2012/01/how-to-plot-two-variable-functions-with.html

# the function that I'm going to plot
def z_func(x,y):
    return (1-(x**2 + y**3)) * np.exp(-(x**2 + y**2)/2)

def plot(X, Y, Z):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, 
                          cmap=cm.RdBu,linewidth=0, antialiased=False)

    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show()

def main():
    x = np.arange(-3, 3, 0.1)
    y = np.arange(-3, 3, 0.1)
    X,Y = meshgrid(x, y) # grid of point
    Z = z_func(X, Y) # evaluation of the function on the grid
    plot(X, Y, Z)
    # print(x,'y>',y,'X>',X, 'Y>',Y,'Z>',Z)
    # print(colored(' x =>', 'red'), X.shape)

if __name__ == "__main__":
    main()