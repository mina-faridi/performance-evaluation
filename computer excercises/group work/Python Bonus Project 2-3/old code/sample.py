

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













from numpy import random,sort,cumsum
import matplotlib.pyplot as plt

h = 10 #
x = random.uniform(0,h, 1000)
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


