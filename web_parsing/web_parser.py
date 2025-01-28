import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
import time

def ParseNCreatedf(r,Stock_name):
	# parse the screener web page and extract financial data to create a Data frame
	soup = BeautifulSoup(r.text, "html.parser")
	PnL_table = soup.find("section", id="profit-loss").find('table')
	fin_yr = heading = PnL_table.find_all('th', class_="")
	numbers = PnL_table.tbody.find_all('tr')
	sales_num = numbers[0]
	# op_num = numbers[2] # operating profit
	OP_num = numbers[2] # OP= operating profit
	OtherInc_num = numbers[4] # Other income
	Int_num = numbers[5]
	Depre_num = numbers[6]
	PBT_num = numbers[7]
	PAT_num = numbers[9]
	EPS_num = numbers[10]
	Div_payout_num = numbers[11]

# Balance Sheet extraction
	BS_table = soup.find("section", id="balance-sheet").find('table').tbody.find_all('tr')
	Eq_num = BS_table[0]
	Rsrv_num = BS_table[1]
	Borrow_num = BS_table[2]
	FixedAsset_num = BS_table[5]
	CWIP_num = BS_table[6]
	Investment_num = BS_table[7]
	Investment_num.find_all('td', class_="")

	# Cash flow extraction
	Cash_table = soup.find("section", id="cash-flow").find('table').tbody.find_all('tr')
	CFO_num = Cash_table[0]
	CFI_num = Cash_table[1]
	CFF_num = Cash_table[2]
	CFO_num.find_all('td', class_="")

# create a DataFrame

	FY_arr = []
	Sales_arr = []
	OP_num_arr = []
	OtherInc_num_arr = []
	Int_num_arr = []
	Depre_num_arr = []
	PBT_num_arr = []
	PAT_num_arr = []
	EPS_num_arr = []
	Div_payout_num_arr = []
	
	# BS numbers
	Eq_num_arr = []
	Rsrv_num_arr = []
	Borrow_num_arr = []
	FixedAsset_num_arr = []
	CWIP_num_arr = []
	Investment_num_arr = []
	
	# Cash numbers
	CFO_num_arr = []
	CFI_num_arr = []
	CFF_num_arr = []
	
	# Stock_name = 'ASIANPAINT'
	no_of_yrs = len(heading)
	
	for i in range(0,(no_of_yrs-1)):
	    # print(heading[i].text)
	    # print(sales_num.find_all('td', class_="")[i].text)
	    FY_arr.append(fin_yr[i].text)
	    Sales_arr.append(sales_num.find_all('td', class_="")[i].text)
	    OP_num_arr.append(OP_num.find_all('td', class_="")[i].text)
	
	    OtherInc_num_arr.append(OtherInc_num.find_all('td', class_="")[i].text)
	    Int_num_arr.append(Int_num.find_all('td', class_="")[i].text)
	    Depre_num_arr.append(Depre_num.find_all('td', class_="")[i].text)
	    PBT_num_arr.append(PBT_num.find_all('td', class_="")[i].text)
	    PAT_num_arr.append(PAT_num.find_all('td', class_="")[i].text)
	    EPS_num_arr.append(EPS_num.find_all('td', class_="")[i].text)
	    Div_payout_num_arr.append(Div_payout_num.find_all('td', class_="")[i].text)
	
	    Eq_num_arr.append(Eq_num.find_all('td', class_="")[i].text)
	    Rsrv_num_arr.append(Rsrv_num.find_all('td', class_="")[i].text)
	    Borrow_num_arr.append(Borrow_num.find_all('td', class_="")[i].text)
	    FixedAsset_num_arr.append(FixedAsset_num.find_all('td', class_="")[i].text)
	    CWIP_num_arr.append(CWIP_num.find_all('td', class_="")[i].text)
	    Investment_num_arr.append(Investment_num.find_all('td', class_="")[i].text)
	
	    CFO_num_arr.append(CFO_num.find_all('td', class_="")[i].text)
	    CFI_num_arr.append(CFI_num.find_all('td', class_="")[i].text)
	    CFF_num_arr.append(CFF_num.find_all('td', class_="")[i].text)

	df = pd.DataFrame({
	    'Stock Name': [Stock_name]* (no_of_yrs-1),
	    'FY':FY_arr,
	    'Sales':Sales_arr,
	    'Operating Profit':OP_num_arr,
	    'Other Income':OtherInc_num_arr,
	    'Interest':Int_num_arr,
	    'Depreciation':Depre_num_arr,
	
	    'PBT':PBT_num_arr,
	    'PAT':PAT_num_arr,
	    'EPS':EPS_num_arr,
	    'Div Payout':Div_payout_num_arr,
	    # 'Sales':Int_num_arr,
	    # 'Operating Profit':Depre_num_arr,
	
	    'Eq Capital':Eq_num_arr,
	    'Reserves':Rsrv_num_arr,
	    
	    'Debt':Borrow_num_arr,
	    'Net Block':FixedAsset_num_arr,
	    'CWIP':CWIP_num_arr,
	    'Investment':Investment_num_arr,
	
	    'CFO': CFO_num_arr,
	    'CFI': CFI_num_arr,
	    'CFF': CFF_num_arr
	    
	})
	return df
				

    
    
    
    
def download_stock_data(stock_name_arr,ip_df):
       ## run a loop as per input stock name array
       ## return a combined Dataframe and an array of stock for which it failed
       ## ip_df is supplied.. output_df will be concatination
       
    error_stock = []
    
    combined_df = ip_df
    for stock in stock_name_arr:
        # print("\n")
        print(stock)
        
        url = 'https://www.screener.in/company/'+stock+'/consolidated/'
        
        # time.sleep(0.1)
        r = requests.get(url)
        try:
            df = ParseNCreatedf(r,stock)
            
            combined_df = pd.concat([combined_df,df], ignore_index=True)
            
        except:
            print("Error in stock :"+stock)
            print("Wait 2second")
            error_stock.append(stock)
            time.sleep(2)
            
    return [combined_df,error_stock]        
            
            
            
def GetFinData(file_name):
    # Get the financial data of list of stock given in the csv file
    
    stock_df = pd.read_csv(file_name)
    print(stock_df.columns)
    
    stock_df10 = stock_df.head(100)
    NSE_stock_list = stock_df10['Symbol']
    
    # CREATE A DUMMY df
    stock = 'WONDERLA'
    r = requests.get('https://www.screener.in/company/'+stock+'/consolidated/')
    df = ParseNCreatedf(r,stock)
    
    max_retry_count = 3
    retry_count = 0
    
    while 1:
        [combined_df,error_stocks] = download_stock_data(NSE_stock_list,df)
        
        if (len(error_stocks)):
            print("Number of error stocks = "+str(len(error_stocks)))
            print(error_stocks)
            
            df = combined_df
            NSE_stock_list = error_stocks
            
            if retry_count == max_retry_count:
                break
            
            retry_count += 1
            print("\nRetry No......"+str(retry_count))
            time.sleep(5)
            
        
        else:
            print('Else block-->>')
            break
    
    print(combined_df)
    
    
    combined_df.to_csv('stock_data.csv')
    
    ### debugging
    
    # find missing stocks
    
    
    target_list = NSE_stock_list 
                        
    output_list = combined_df['Stock Name'].unique()
    print(combined_df['Stock Name'].nunique())
    print(stock_df10['Symbol'].nunique())
    
    
    print(set(target_list).difference(set(output_list)))


#------------------------------main func ----------------------------------	
if __name__ == "__main__":
# nra_init(nra)

    # timedata = time.time()
    msg = ("****************************************************************************\n")
    print(msg)
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
    
















