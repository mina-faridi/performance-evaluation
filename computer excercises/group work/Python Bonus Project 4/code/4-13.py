import numpy as np
import matplotlib.pyplot as plt
a = 1
b = 10
mu, sigma = 5.5, 0.1 # mean and standard deviation
x = np.random.normal(mu, sigma, 1000)
y = np.random.normal(mu, sigma, 1000)

for i in range(len(x)):
    if x[i]<a:
        x[i]=0
    elif x[i]> b:
        x[i]=0

for i in range(len(y)):
    if y[i]<a:
        y[i]=0
    elif y[i]> b:
        y[i]=0
count, bins, ignored = plt.hist(x, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')
count, bins, ignored = plt.hist(y, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='b')
plt.show()

s = x + y
count, bins, ignored = plt.hist(s, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')
plt.show()

s = x - y
count, bins, ignored = plt.hist(s, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')
plt.show()