import random as rn



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

    n = int( input("enter integer value for n: " ) )
    m = int( input("enter integer value for m: ") )
    a = int( input("enter integer value for a: " ) )
    b = int( input("enter integer value for b: " ) )
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


if __name__ == '__main__':
    solving_chapter2_problem_c2_q25()