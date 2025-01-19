import time
# import serial
# import re
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
# from sklearn.tree import DecisionTreeRegressor
# from sklearn.metrics import mean_absolute_error
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestRegressor

# import xlsxwriter
# import easygui as gui
#---------------------------------------------------------------
# implementing gradient descent algo
# perform linear regression using  GradDescAlgo and compare with sklear linearregression model 
#
#---------------------------------------------------------------

def GradDescAlgo(X,Y):
    # X independent var set, Y dependent/target var set. 
    # bboth are single column same size list.. numpy array.. can be used for matrix calculation
    
    print("start")
    m = 0
    c = 0
    
    L = 0.00021 # learning rate
    iter_no = 4000000 # number of iteration
    n = len(X) # considering X and Y are same length
    Y_pred = m*X + c
    cost_old = (1/n)*(sum((Y-Y_pred)**2))
    
    for i in range(iter_no):
        
        
        Dm = (-2/n)*(sum(X*(Y-Y_pred)))
        Dc = (-2/n)*(sum(Y-Y_pred))
        
        m = m - L*Dm
        c = c - L*Dc
        
        Y_pred = m*X + c
        cost = (1/n)*(sum((Y-Y_pred)**2))
        
        msg = "Iteration = "+str(i)+"\tCost = "+str(cost)+"\t"
        msg += "m = "+str(m)+"\tc = "+str(c)+"\n"
        print(msg)
        # print ("m {}, c {}, cost {} iteration {}".format(m,c,cost, i))
        # plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='brown')  # regression line
    
        
        if math.isclose(cost, cost_old, rel_tol=1e-10):
            print("************Got the optimum point")
            break
        cost_old = cost
    # plot the data
    Y_pred = m*X + c

    plt.scatter(X, Y) 
    plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='blue')  # regression line
    # plt.show()


def test_score_problem():
    df = pd.read_csv('test_scores.csv')
    print(df)
    math_score = df['math']
    cs_score = df['cs']
    
    GradDescAlgo(math_score,cs_score)
    # plt.scatter(math_score, cs_score) 
    # plt.scatter(cs_score,math_score) 
    # plt.show()





		

#------------------------------main func ----------------------------------	
if __name__ == "__main__":
# nra_init(nra)

    timedata = time.time()
    msg = ("****************************************************************************\n")
    
    print(msg)
    test_score_problem()
    # X = np.array([1,2,3,4,5,6,7,8,9,10])
    # Y = np.array([12,28,35,40,57,67,78,83,100,105])
    
    # X = np.array([1,2,3,4,5])
    # Y = np.array([5,7,9,11,13])
    
    # GradDescAlgo(X,Y)
    sys.exit(0)	
    
