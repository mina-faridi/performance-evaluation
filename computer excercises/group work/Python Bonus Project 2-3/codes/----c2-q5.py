
from math import exp
import matplotlib.pyplot as plt

b = 30
c = 10
l = 15 # lambda = 15

def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

def poisson(k):
  return exp(-1 * l) * ((l**k)/fact(k))

def x_pmf(k):
  return poisson(k)

def y_pmf(k):
  if k == 0:
    prob = []
    for i in range (0,c):
      prob.append(poisson(i))
    return sum(prob)

  if k == (b-c):
    return x_pmf(b)  
    
  return poisson(k+c)

def discard(max_number):
  prob = []
  for i in range (0,max_number):
    prob.append(poisson(i))
  return 1 - sum(prob)

def solving_chapter2_problem_c2_q5():
    x = []
    for i in range(0,30):
        x.append(x_pmf(i))

    y = []
    for i in range(0,30):
        y.append(y_pmf(i))

    d = []
    for i in range(0,30):
        d.append(discard(i))

    plt.plot(range(0,30),x)
    plt.xlabel("Number of packets stored at the end of the first slot")
    plt.ylabel("PMF")
    plt.show()

    plt.plot(range(0,30),y)
    plt.xlabel("Number of packets stored at the end of the second slot")
    plt.ylabel("PMF")
    plt.show()

    plt.plot(range(0,30),d)
    plt.xlabel("Maximum number of packets that can be stored")
    plt.ylabel("Probability that some packets get discarded")
    plt.show()

if __name__ == '__main__':
    solving_chapter2_problem_c2_q5()