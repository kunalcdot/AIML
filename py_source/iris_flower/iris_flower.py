import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
import sys
from sklearn.datasets import load_iris





		

#------------------------------main func ----------------------------------	
if __name__ == "__main__":
# nra_init(nra)

    # timedata = time.time()
    msg = ("****************************************************************************\n")
    
    print(msg)
    
    iris_data = load_iris()
    print(iris_data.keys())
    
    print(msg)
    # print(iris_data['DESCR'])
    # print(iris_data['target_names'])
    # print(iris_data['feature_names'])
    
    iris_df = pd.DataFrame(data=iris_data['data'],columns=iris_data['feature_names'])
    print(iris_df)
    
    target_Df = pd.DataFrame(data=iris_data['target'],columns=iris_data['target_names'])
    print(target_Df)
    
    
    sys.exit(0)	
    
    # file_path = 'goalscorers.csv'
    # file_path = 'melb_data.csv'
# read the data and store data in DataFrame titled melbourne_data
    # DataFrame = pd.read_csv(file_path) 
    
    print(DataFrame.columns)
    
    
    print(DataFrame['Price'])
    
    
    print(DataFrame[['Price','Rooms']])
    print(msg+"\n")
    
    print(DataFrame['Price'][0])
    
    
    
    

    sys.exit(0)	

