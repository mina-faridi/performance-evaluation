import numpy as np
if __name__ == '__main__':
    x = []
    n = int(input("Enter number of elements of x : "))
    for i in range(0, n):
        temp = int(input("enter x elements : "))
        x.append(temp)  # adding the element
    y = []
    n = int(input("Enter number of elements of y : "))
    for i in range(0, n):
        temp = int(input("enter y elements : "))
        y.append(temp)  # adding the element
    if np.var(x) == np.var(y):
        print("Two random variables have the same variance.")
        sum = []
        sub = []
        for i in x:
            for j in y:
                sum.append(i+j)
        for i in x:
            for j in y:
                sub.append(i-j)

        cor = np.corrcoef(sum, sub)
        if cor[0,1] == 0:
            print("The two random variables set (X+Y) and (X-Y) are uncorrelated")
        else:
            print("(X+Y) and (X-Y) are Correlated")
    else:
        print("Two random variables DONT have the same variance.")