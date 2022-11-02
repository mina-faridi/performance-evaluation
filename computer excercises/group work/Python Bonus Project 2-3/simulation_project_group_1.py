
############# Simlation's Bonus Project - Group 1 #############


from math import exp
import matplotlib.pyplot as plt
import numpy as np
from numpy import random,sort,cumsum
from gmpy2 import comb , fac
from numpy import e , dot ,sum , power
from scipy.stats import binom
from scipy.integrate import quad
import math
import random
import time
import random as rn

############# Chapter 2 : Question 1

def calculate_pmf_of_2_games(nl_first,l_first,nl_second,l_second,p_tie,p_win):
    result = [0 for i in range(5)]
    # x -> 0 : losing , losing
    result[0] = l_first * l_second 
    # x -> 1 : not losing -> tie , losing + losing + not tising -> tie
    result[1] = (nl_first * p_tie * l_second) + (l_first * nl_second * p_tie)
    # x -> 2 : not losing -> tie , not losing -> tie + losing , not losing -> win + not losing -> win , losing
    result[2] = round((nl_first * p_tie * nl_second * p_tie) + (nl_first * p_win * l_second) + (l_first * nl_second * p_win),2)
    # x -> 3 : not losing -> win , not losing -> tie + not losing -> tie , not losing -> win
    result[3] = round((nl_first * p_win * nl_second * p_tie) * 2,2)
    # x -> 4 : not losing -> win , not losing -> win
    result[4] = round(nl_first * p_win * nl_second * p_win,2)
    return result

def display_pmf(input_array):
    # displaying the probability of each item in the input
    for i in range(len(input_array)):
        print(f'P(x = {i}) : {input_array[i]}')
    # displaying otherwise probability 
    print(f'P(X > {len(input_array)}) : 0')

    
def solving_chapter2_problem_c2_q1():
    # probabilities:
    nl_first  = 0.4 # not losing in the first game probability
    nl_second = 0.7 # not losing in the second game probability
    l_first   = 0.6 # losing in the first game probability 
    l_second  = 0.3 # losing in the second game probability 

    p_tie     = 0.5 # probability of tie
    p_win     = 0.5 # probability of win

    # calling the caculte pmf with our probability definition
    result = calculate_pmf_of_2_games(nl_first,l_first,nl_second,l_second,p_tie,p_win)
    display_pmf(result)

############# Chapter 2 : Question 5

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

############# Chapter 2 : Question 9

n = 99
p = 0.4
k = np.linspace(10,60,num=50,endpoint=False)
ans = []


def facto (n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
        
    return fact

def combo(n, k):
    temp1 = facto(n)
    temp2 = facto(k)
    temp3 = facto(n-k)
    cmb = temp1/(temp2*temp3)
    return cmb

def q9(n,k,p):
    temp1 = combo(n,k)*pow(p,k)*pow(1-p,n-k)
    temp2 = combo(n,k-1)*pow(p,k-1)*pow(1-p,n-k+1)
    return temp1/temp2

def solving_chapter2_problem_c2_q9():
    print(k)

    for ks in k:
        ans.append(q9(n,int(ks),p))
        
    plt.plot(ans,k)
    plt.hlines(y = (n+1)*p, xmin = 0, xmax = 6, color ='r', linestyle='--')
    plt.vlines(x = 1, ymin=0, ymax = 60, color = 'y', linestyle = '--')
    plt.text(0, ((n+1)*p)+0.5, '(n+1)*p', ha ='left', va ='bottom')
    plt.text(1, 0.8, 'Ratio = 1',rotation ='vertical', ha ='right', va ='bottom')
    plt.xlabel("Ratio calculated with different values of K")
    plt.ylabel("values of K")

    plt.show()

############# Chapter 2 : Question 13

def pmf_girls (g, naturals, adoptedgirls):
    all = naturals + adoptedgirls
    if (adoptedgirls>g or all <g):
        return (0)
    else:
        return math.comb(naturals,g-2) * math.pow(0.5,naturals)

def solving_chapter2_problem_c2_q13():
    # print("insert number of the girls to find PMF")
    # g = int(input()) #pmf variable (num of girls)
    g = 3 #for example

    naturals = 5  # number of natural children
    adoptedgirls = 2  # number of adopted girls

    print(pmf_girls (g, naturals, adoptedgirls))

############# Chapter 2 : Question 17

def cel_to_fahr(cel_mu: float, cel_sigma: float) -> float:
    """
    since we know transform is linear, we can use the inverse transform
    fahr  = (cel * 9 / 5) + 32

    and new mean and sigma are:

    E[fahr] = (E[cel] * 9 / 5) + 32;

    var(fahr) = (9/5)^2 * var(cel)
    => sigma(fahr) = (9/5) * sigma(cel)

    """
    fahr_mu    = cel_mu * 9 / 5 + 32
    fahr_sigma = cel_sigma * 9 / 5

    return fahr_mu, fahr_sigma
    
def normal_pdf(x, mu:float, sigma:float) -> float:
    """
    normal distribution pdf function
    """
    return (1.0 / np.sqrt(2 * np.pi * sigma ** 2)) * np.exp(-0.5 * (x - mu) ** 2 / sigma ** 2)
    
def make_plot(axs, title: str, mu: float, sigma: float) -> None:
    """
    axs: matplotlib axes
    title: string
    mu: float
    sigma: float
    ------------------------
    We want to plot the distribution of the temperature
    and since we know it is normal, we can use the normal distribution function
    from scipy.stats.norm to plot it.
    for range of x, we use mu-3*sigma to mu+3*sigma
    to make sure we get a full range of the distribution.

    The normal range includes the Mu + - Sigma range, so we separate this area.
    """
    x     = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
    y     = normal_pdf(x, mu, sigma)
    left  = mu - sigma
    right = mu + sigma

    axs.plot(x, y, "k")
    axs.set_title(title, fontsize=14, loc="left")
    axs.vlines(left, 0,
        normal_pdf(left, mu, sigma),
        colors="r", linestyles="dashed")
    axs.text(
        left + (0.5 if left == 0 else 2),
        normal_pdf(left, mu, sigma) / 2,
        int(left),
        fontsize=10,
    )
    axs.vlines(right, 0,
        normal_pdf(right, mu, sigma),
        colors="r", linestyles="dashed")
    axs.text(
        right - (5 if right % 10 == 0 else 9),
        normal_pdf(right, mu, sigma) / 2,
        int(right),
        fontsize=10,
    )
    axs.spines["top"  ].set_visible(False)
    axs.spines["right"].set_visible(False)
    axs.spines["left" ].set_visible(False)
    axs.tick_params(left=False, labelleft=False)


def solving_chapter2_problem_c2_q17():
    fig, axs = plt.subplots(1, 2, figsize=(10, 6))
    
    celsius_mu    = 10
    celsius_sigma = 10
    
    fahrenheit_mu, fahrenheit_sigma = cel_to_fahr(celsius_mu, celsius_sigma)
    
    make_plot(
        axs[0], r"$\mathbf{Temperature \; in}$" +"\nCelsius",
        celsius_mu,
        celsius_sigma
    )
    make_plot(
        axs[1],
        r"$\mathbf{Temperature \; in}$" + "\nFahrenheit",
        fahrenheit_mu,
        fahrenheit_sigma,
    )
    plt.show()

############# Chapter 2 : Question 21

def tossCoin():
    resualt=None
    if random.randint(0,1)==0:
        resualt='head'
    else:
        resualt='tail'
    return resualt


# Press the green button in the gutter to run the script.

def solving_chapter2_problem_c2_q21():
    deposit = 0
    while True:
        numberOfTosses=0
        result=tossCoin()
        while result=='head':
            numberOfTosses+=1
            result=tossCoin()
        if numberOfTosses>0:
            deposit += pow(2, numberOfTosses)
            print('Congrats!! You have earned ' + str(pow(2, numberOfTosses)) + '$ In this round!')
        else:
            print('Sorry :( You did not win in this round')

        print('Total Deposit: '+str(deposit)+'$ ')
        print()
        print('-----------------------------------------------------------------')
        print()
        time.sleep(1.5)

############# Chapter 2 : Question 25

def M_i_randGenerator (m,M,n):
    for i in range(0,n):
        M[i] = rn.randint(0,m)

#M = [0,1,2]

def calculate_L(m,M,n,L):
    for x in range(0,n):
        for y in range(0,m):
            if y+1 <= M[x]:
                L[y] = L[y] + 1

def sigma_Mk(M,n):
    sum = 0
    for k in range (0 , n):
        sum = sum + M[k]
    return sum

def calculate_Joint_PMF (n,M,m,Prob_IJ,sum):
    for i in range(0,n):
        for j in range(0,m):
            if j+1 <= M[i] :
                Prob_IJ[i][j] = 1 / sum
            else:
                Prob_IJ[i][j] = 0.0
            print("Joint PMF of (", i+1 , "," , j+1 , ") is: " , Prob_IJ[i][j])


def calculate_Marginal_PMF_I (n , m,Prob_I,M,sum):
    for i in range(0,n):
        Prob_I[i] = M[i] / sum
        print( "Marginal PMF of I (", i+1 , ") is: ", Prob_I[i] )

def calculate_Marginal_PMF_J (n , m,L,Prob_J,sum):
    for j in range(0,m):
        Prob_J[j] = L[j] / sum
        print( "Marginal PMF of J (", j+1 , ") is: ", Prob_J[j] )

def probabilty_ij(n,m,p_ij):
    for i in range(0,n):
        for j in range(0,m):
            p_ij[i][j] = rn.random()
            print("probabilty of (",i+1, "," ,j+1,")" , p_ij[i][j])

def expected_value(n,M,p_ij,a,b):
    sigma = 0
    for i in range(0,n):
        for j in range(0,M[i]):
            sigma = sigma + ( p_ij[i][j] * a ) + ( (1 - p_ij[i][j]) * b )
    print("Exptected Value is: " , sigma)

def solving_chapter2_problem_c2_q25():

    n = int( input("enter integer value for n (4 in the question): " ) )
    m = int( input("enter integer value for m (3 in the question): ") )
    a = int( input("enter integer value for a (1 in the question): " ) )
    b = int( input("enter integer value for b (-1 in the question): " ) )
    print("-" * 60)

    """
    n=3
    m=4
    a = 1
    b = -1
    """

    M = [0] * n
    L = [0] * m
    sum = 0

    Prob_IJ = [[0]*m]*n
    Prob_I = [0] * n
    Prob_J = [0] * m
    p_ij = [[0]*m]*n

    M_i_randGenerator (m,M,n)
    print("M array is:" , M)
    print("-" * 60)

    calculate_L(m,M,n,L)
    print("L array is:" , L)
    print("-" * 60)

    sum = sigma_Mk(M,n)
    print("sum is:" , sum)
    print("-" * 60)

    calculate_Joint_PMF (n,M,m,Prob_IJ,sum)
    print("-" * 60)

    count = 0
    for i in range(0,n):
        for j in range(0,m):
            count = count + Prob_IJ[i][j]
    print("count is: ", count)
    print("-" * 60)

    calculate_Marginal_PMF_I (n , m,Prob_I,M,sum)
    print("-" * 60)

    calculate_Marginal_PMF_J (n , m,L,Prob_J,sum)
    print("-" * 60)

    probabilty_ij(n,m,p_ij)
    print("-" * 60)

    expected_value(n,M,p_ij,a,b)
    print("-" * 60)

############# Chapter 2 : Question 41

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

############# Chapter 3 : Question 1

def calculate_expected_value(p1,p2,x1,x2):
    return (p1 * x1) + (p2 * x2)

def solving_chapter2_problem_c3_q1():
    py_1 = 1/3
    py_2 = 1 - py_1

    gx_1 = 1
    gx_2 = 2

    print('Showing PMF:')
    print(f'--py(1) = P(X <= 1/3) = {py_1}')
    print(f'--py(2) = P(X <= 1/3) = {py_2}')

    print('-' * 60)
    
    expected_value = calculate_expected_value(py_1,py_2,gx_1,gx_2)
    print('Showing expected value')
    print(f'--E[Y] = (1/3 * 1) + (2/3 * 2) = {expected_value}')

    ############# Chapter 3 : Question 5

def solving_chapter2_problem_c3_q5():
    h = 10 #
    x = np.random.uniform(0,h, 1000)
    x_s = sort(x)

    pdf =[ 2*(h - t) / h**2 for t in x_s]

    plt.xlabel('x')
    plt.ylabel('$f_{X}(x)$')
    plt.title('PDF')
    plt.bar(x_s, pdf)
    plt.show()

    plt.rcParams["figure.autolayout"] = True
    cdf = cumsum(pdf)
    plt.plot(x_s, cdf, label="CDF")
    plt.legend()
    plt.show()

    cdf =[1-((h-t)/h)**2 for t in x_s]
    plt.xlabel('x')
    plt.ylabel('$F_{X}(x)$')
    plt.title('CDF')
    plt.plot(x_s, cdf, marker='o')
    plt.show()

############# Chapter 3 : Question 13

def normalProbabilityDensity(x):
    constant = 1.0 / np.sqrt(2*np.pi)
    return(constant * np.exp((-x**2) / 2.0))

def solving_chapter2_problem_c3_q13():
    Fahrenheit = 59
    mean = 10
    e = 10
    Celsius = (Fahrenheit - 32) * 5.0/9.0
    z_upper = (Celsius - e)/mean
    temperature, _ = quad(normalProbabilityDensity, np.NINF, z_upper)
    print('Probability: ', temperature)


############# Chapter 3 : Question 21

def solving_chapter2_problem_c3_q21():
    l = input("Please enter length l: ")
    l = int(l)
    x = [0 , l]
    y = [(1/l) , (1/l)]
    plt.plot(x, y)
    plt.xlabel('Y')
    plt.ylabel('Probability')
    plt.title('Probability function of Y')
    plt.show()
    y_in = input("Please enter length of first cut: ")
    y_in = int(y_in)


    x1 = [0, l]
    y1 = [(1 / l), (1 / l)]
    # plotting the line 1 points
    plt.plot(x1, y1, label="Probability function of Y")

    # line 2 points
    x2 = [0, y_in]
    y2 = [(1 / y_in), (1 / y_in)]
    # plotting the line 2 points
    plt.plot(x2, y2, label="Probability function of X|Y")

    # naming the x axis
    plt.xlabel('Probability')
    # naming the y axis
    plt.ylabel('')
    # giving a title to my graph
    plt.title('Probability function of Y and X|Y')

    # show a legend on the plot
    plt.legend()

    # function to show the plot
    plt.show()

    input("Please enter any key to calculate joint PDF of Y and X ")
    x = [0, y_in]
    y = [(1 / l)*(1 / y_in) , (1 / l)*(1 / y_in)]
    plt.plot(x, y)
    plt.xlabel('X,Y')
    plt.ylabel('Probability')
    plt.title('Joint probability function of X,Y')
    plt.show()
    print('--------------------------------------------------------------------------------------------------')
    print()
    print('The marginal PDF of X is: 1/l ln(l/x)')
    print('E[X] = l/4')

############# Chapter 3 : Question 21

def solving_chapter2_problem_c3_q25():
    sigma = input("Please enter σ value: ")
    sigma = float(sigma)
    c = np.arange(-10, 5, 0.01)
    y = np.exp(-((pow(c,2))/(2*pow(sigma,2))))
    print('Values of c: ', c)
    print('Values of P(c): ', y)

    plt.plot(c, y)

    plt.title("Probability of C^2 <= X^2 + Y^2")
    plt.xlabel("Values of c")
    plt.ylabel("Values of P(c)")
    plt.show()

if __name__ == '__main__':
    
    while True:
        chapter_number = int(input('Enter Chapter (2 or 3):'))

        if chapter_number not in [2,3]:
            print('Please enter a valid chapter (2 or 3)')
        else:
            if chapter_number == 2:
                while True:
                    question_number = int(input('Enter Question (1,5,9,13,17,21,25,41):'))
                    if question_number not in [1,5,9,13,17,21,25,41]:
                        print('Please enter a valid question')
                    else:
                        if question_number == 1:
                            solving_chapter2_problem_c2_q1()
                        elif question_number == 5:
                            solving_chapter2_problem_c2_q5()
                        elif question_number == 9:
                            solving_chapter2_problem_c2_q9()
                        elif question_number == 13:
                            solving_chapter2_problem_c2_q13()
                        elif question_number == 17:
                            solving_chapter2_problem_c2_q17()
                        elif question_number == 21:
                            solving_chapter2_problem_c2_q21()
                        elif question_number == 25:
                            solving_chapter2_problem_c2_q25()
                        elif question_number == 41:
                            solving_chapter2_problem_c2_q41()
                        break

            elif chapter_number == 3:
                while True:
                    question_number = int(input('Enter Question (1,5,13,21,25):'))
                    if question_number not in [1,5,13,21,25]:
                        print('Please enter a valid question')
                    else:
                        if question_number == 1:
                            solving_chapter2_problem_c3_q1()
                        elif question_number == 5:
                            solving_chapter2_problem_c3_q5()
                        elif question_number == 13:
                            solving_chapter2_problem_c3_q13()
                        elif question_number == 21:
                            solving_chapter2_problem_c3_q21()
                        elif question_number == 25:
                            solving_chapter2_problem_c3_q25()
                        break
            resume = input('Do you want to continue ? (1 for yes and anything else for no):')
            if resume == '1':
                print('\n\n')
                continue
            else:
                break
    