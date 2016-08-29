import matplotlib.pyplot
import pylab

def main():
    x = [1,2,3,4]
    y = [10,20,30,40]
    y1 = [20,30,40,50]
    # s is size
    # http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.scatter
    matplotlib.pyplot.scatter(x, y, s=100,c='green')
    matplotlib.pyplot.scatter(x, y1, s=10, c='red')
    matplotlib.pyplot.show()


if __name__ == "__main__":
    main()