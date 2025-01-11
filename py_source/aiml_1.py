import time
# import serial
# import re
import os
import sys
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# import xlsxwriter
# import easygui as gui


def BasicDeciTree(X_new,y):
    # Basic DecisionTree Regressor.. Not using any leaf node variable
    
    # X_new => Data set
    # y => Target array (price)
    # --------------------------------------------------
    ## model - 4steps
    # Define
    # training - fit
    # predict
    # Evaluate/Validation - MAE (error)
    
    

# Define model. Specify a number for random_state to ensure same results each run
    model = DecisionTreeRegressor(random_state=1)
    # model = DecisionTreeRegressor(max_leaf_nodes = 10, random_state=1)
    
# Create a separate train and test set
    train_X, val_X, train_y, val_y = train_test_split(X_new, y, random_state = 0)
    
# Fit model
    model.fit(train_X, train_y)
    
    # test model.. predict 
    
    predicted_home_prices = model.predict(val_X)
    MAE = mean_absolute_error(val_y, predicted_home_prices)
    print("Decision Tree Error value (MAE) = ",f'{round(MAE):,}')
    
    
def OptimDeciTree(X_new,y):
    # Optimise DecisionTree Regressor using max leaf node variable
    
    # X_new => Data set
    # y => Target array (price)
    # --------------------------------------------------
    ## model - 4steps
    # Define
    # training - fit
    # predict
    # Evaluate/Validation - MAE (error)
    
    max_nodes = [5,1000,2000,3000,5000]

    for node in max_nodes:
    

    # Define model. Specify a number for random_state to ensure same results each run
        # model = DecisionTreeRegressor(random_state=1)
        model = DecisionTreeRegressor(max_leaf_nodes = node, random_state=1)
        # model = RandomForestRegressor(random_state=1)
    # Create a separate train and test set
        train_X, val_X, train_y, val_y = train_test_split(X_new, y, random_state = 0)
        
    # Fit model
        model.fit(train_X, train_y)
        
        # test model.. predict 
        
        predicted_home_prices = model.predict(val_X)
        MAE = mean_absolute_error(val_y, predicted_home_prices)
        print("Error value (MAE) with Max Leaf = "+str(node)+" = ",f'{round(MAE):,}')
        

def RandForestTree(X_new,y):
    model = RandomForestRegressor(random_state=1)
    # Create a separate train and test set
    train_X, val_X, train_y, val_y = train_test_split(X_new, y, random_state = 0)
        
    # Fit model
    model.fit(train_X, train_y)
        
        # test model.. predict 
        
    predicted_home_prices = model.predict(val_X)
    MAE = mean_absolute_error(val_y, predicted_home_prices)
    print("Random Forest MAE = ",f'{round(MAE):,}')
        












		

#------------------------------main func ----------------------------------	
if __name__ == "__main__":
# nra_init(nra)

    timedata = time.time()
    msg = ("****************************************************************************\n")
    
    print(msg)
    
    # file_path = 'goalscorers.csv'
    file_path = 'melb_data.csv'
# read the data and store data in DataFrame titled melbourne_data
    goal_data = pd.read_csv(file_path) 
# print a summary of the data in Melbourne data
    # print(goal_data.describe())
    X = goal_data
    # print(X)
    print(X.columns)
    
    ## get the data as per required features
    features = ['Rooms','Distance','Bedroom2','Car']
    X_new = X[features]
    # print(X_new) # X_new having less number of features from X dataset
    print(X_new.describe())
    
    y = X.Price ## target variable.. prediction target
    
    BasicDeciTree(X_new,y)
    OptimDeciTree(X_new,y)
    RandForestTree(X_new,y)
    sys.exit(0)	
    
    
    
    # --------------------------------------------------
    ## model - 4steps
    # Define
    # training - fit
    # predict
    # Evaluate/Validation - MAE (error)
    
    

# Define model. Specify a number for random_state to ensure same results each run
    # model = DecisionTreeRegressor(random_state=1)
    model = DecisionTreeRegressor(max_leaf_nodes = 10, random_state=1)
    
    
    
# Create a separate train and test set
    train_X, val_X, train_y, val_y = train_test_split(X_new, y, random_state = 0)
    
    
    
# Fit model
    model.fit(train_X, train_y)
    
    # test model.. predict 
    # print("Making predictions for the following 5 houses:")
    # print(model.predict(X_new.head()))
    
    predicted_home_prices = model.predict(val_X)
    MAE = mean_absolute_error(val_y, predicted_home_prices)
    print(MAE)
    
    
    
    
    
    
    
    
    
    
    # y = goal_data.minute
    # print(y)
    sys.exit(0)	
    goal_model = DecisionTreeRegressor(random_state=1)
    goal_model.fit(X, y)
    







    sys.exit(0)	

