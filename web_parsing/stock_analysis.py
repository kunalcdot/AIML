import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
import time



#------------------------------main func ----------------------------------	
if __name__ == "__main__":
# nra_init(nra)

    # timedata = time.time()
    msg = ("****************************************************************************\n")
    print(msg)
    file = 
    df = pd.read_csv(file)
    
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
    df.head()
    
    
    # stock = 'WIPRO'
    # url = 'https://www.screener.in/company/'+stock+'/consolidated/'
        
    # r = requests.get(url)
        
    
    # df = ParseNCreatedf(r,stock)
    # print(df)
    # df.to_csv('stock_data.csv')
    
    # sys.exit(0)
    
    file_name = 'NSE_stocks_Dec2024.csv'
    # file_name = 'NSE_temp1.csv'
    GetFinData(file_name)
    
    sys.exit(0)
    
















