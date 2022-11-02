
import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':
    #a
    x = np.arange(-1,1,0.01)
    plt.figure(0)
    plt.plot(x)
    dx = np.arange(-100,100,1)
    Fy = np.absolute(x)
    Fy = np.power(Fy,0.5)
    plt.plot(Fy)
    plt.show()

    #b
    x = np.arange(-1,1,0.01)
    plt.figure(1)
    plt.plot(x)
    dx = np.arange(-100,100,1)
    Fy = np.absolute(x)
    Fy = -1* np.log(Fy)
    plt.plot(Fy)
    plt.show()