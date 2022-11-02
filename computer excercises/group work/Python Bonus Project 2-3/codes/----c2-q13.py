import math

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

if __name__ == '__main__':
    solving_chapter2_problem_c2_q13()
    