from gmpy2 import comb , fac
from numpy import e , dot ,sum , power
from scipy.stats import binom
import matplotlib.pyplot as plt

def solving_chapter2_problem_c2_q41():
    w = 50 # week
    d = 5 #day
    p = 0.02
    n = d * w
    k = 5
    lambdaa = n * p # for part b

    pay_t = [10,20,50] # Ticket prices for part c
    p_pay_t = [0.5,0.3,0.2] # respective probabilities for part c

    pk= comb(n,k) * p**k * (1-p)**(n-k)
    print("P(X = k) = " , pk)

    # defining list of r values
    r_values = list(range(16))
    # list of pmf values
    dist = [binom.pmf(r, n, p) for r in r_values ]
    # plotting the graph
    plt.bar(r_values, dist)
    plt.show()

    approximation = e**(-lambdaa) * (lambdaa ** k / fac(k))
    print("Poisson  approximation of part a : " , approximation)


    tp_pay_t = dot(p, p_pay_t)
    p_mean = sum(dot(pay_t,tp_pay_t))
    mean = n * p_mean
    p_var = sum(dot(power(pay_t,2),tp_pay_t)) - p_mean**2
    var = n * p_var

    print("mean: " , mean )
    print("Variance: " , var )

if __name__ == '__main__':
    solving_chapter2_problem_c2_q41()