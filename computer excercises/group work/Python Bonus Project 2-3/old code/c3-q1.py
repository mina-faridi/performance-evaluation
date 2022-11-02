#class care :

import  numpy as np


if __name__ =='__main__':

    print("data uniform")

    dat = np.random.uniform(0,1,size=1)

    if dat <= 1/3 :
        Gx = 1
    elif dat > 1/3 :
        Gx = 2

    print ("data uniform")
    print (dat)

    print ("Gx")
    print (Gx)
