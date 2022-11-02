

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



if __name__ == '__main__':
    solving_chapter2_problem_c2_q1()