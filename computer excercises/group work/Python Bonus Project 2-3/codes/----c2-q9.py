import numpy as np
import matplotlib.pyplot as plt


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



if __name__ == '__main__':
    solving_chapter2_problem_c2_q9()