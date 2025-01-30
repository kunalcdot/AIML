import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
import time
import numpy as np



def stock_analysis_preprocess(df,mode):
    
    # mode = 1 ==> only stage1
    # mode = 2 ==> only stage2
    # mode = 3 ==> both stage1 and 2
    # print('ver2')
    ## stage 1 : Feature engineering: crerate new columns
    
    # df = pd.read_csv(file)
    df['Sales'] = pd.to_numeric(df['Sales'].str.replace(',',''))
    df['Operating Profit'] = pd.to_numeric(df['Operating Profit'].str.replace(',',''))
    df['PAT'] = pd.to_numeric(df['PAT'].str.replace(',',''))
    
    
    df['OPM%'] = df['Operating Profit']/df['Sales']*100
    df['NPM%'] = df['PAT']/df['Sales']*100
    
    # df['Other Income'] = pd.to_numeric(df['Other Income'].str.replace(',','')) # for financial stock, giving error
    df['Interest'] = pd.to_numeric(df['Interest'].str.replace(',',''))
    df['Depreciation'] = pd.to_numeric(df['Depreciation'].str.replace(',',''))
    df['PBT'] = pd.to_numeric(df['PBT'].str.replace(',',''))
    df['Reserves'] = pd.to_numeric(df['Reserves'].str.replace(',',''))
    df['Debt'] = pd.to_numeric(df['Debt'].str.replace(',',''))
    df['Net Block'] = pd.to_numeric(df['Net Block'].str.replace(',',''))
    df.head()
    
    g = df.groupby('Stock Name')
    
    df['Sales_Gr%'] = g['Sales'].pct_change(periods = 1)*100

    n = 3
    df['Sales_Gr_3yr%'] = ((((g['Sales'].pct_change(periods=n))+1)**(1/n))-1)*100
    
    df['OP_Gr%'] = g['Operating Profit'].pct_change(periods = 1)*100
    n = 3
    df['OP_Gr_3yr%'] = ((((g['Operating Profit'].pct_change(periods=n))+1)**(1/n))-1)*100
    
    df['PAT_Gr%'] = g['PAT'].pct_change(periods = 1)*100
    n = 3
    df['PAT_Gr_3yr%'] = ((((g['PAT'].pct_change(periods=n))+1)**(1/n))-1)*100
    
    
    
    
    
    
    
    
    
    
    
    df.head()
    
    
    
    
    
    
    
    if (mode == 3):
        ## stage 2 : Remove outlier
        # Remove -ve and infinity values to get a reliable s.d. 
        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        df.dropna(inplace=True)
        df = df[df['OPM%'] >= 0]
        df = df[df['NPM%'] >= 0]
        
        # Outlier outside u+3sigma to u-3sigma 
        df_no_outliers = remove_outliers_sd(df, ['OPM%', 'NPM%', 'Sales_Gr%', 'Sales_Gr_3yr%'])
        df = df_no_outliers
    
    return (df)
    
    
    
def remove_outliers_sd(df, column_list):
    for col in column_list:
        mean = df[col].mean()
        sd = df[col].std()
        df = df[(df[col] >= mean - 3 * sd) & (df[col] <= mean + 3 * sd)]
    return df


def stock():
    print('test')
    
    
    
    
    

    

#------------------------------main func ----------------------------------	
if __name__ == "__main__":
# nra_init(nra)

    # timedata = time.time()
    msg = ("****************************************************************************\n")
    print(msg)
    file = 'stock_data_ver02'
    df = pd.read_csv(file)
    
    df = stock_analysis_preprocess(df)
    
    
    
    sys.exit(0)
    
















