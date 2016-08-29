import numpy as np
import matplotlib.pyplot as plt

def main():
    N = 10
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radiuses

    print('x=',x,'y=',y,'colors=',colors,'area=',area)
    plt.scatter(x, y, s=area,c=colors, alpha=0.5)
    plt.show()

if __name__ == "__main__":
    main()