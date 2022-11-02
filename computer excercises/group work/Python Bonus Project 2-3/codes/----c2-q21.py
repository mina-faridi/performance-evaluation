import random
import time

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


if __name__ == '__main__':
    solving_chapter2_problem_c2_q21()