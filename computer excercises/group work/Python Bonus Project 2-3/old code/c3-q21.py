import matplotlib.pyplot as plt





if __name__ == '__main__':
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
