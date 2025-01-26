import requests
from bs4 import BeautifulSoup
import pandas as pd

def ParseNCreatedf(r):
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
	
	Stock_name = 'ASIANPAINT'
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
	    'Stock Name': [Stock_name]* no_of_yrs,
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
	
	    'CFO': CFO,
	    'CFI': CFI,
	    'CFF': CFF
	    
	})
	return df
				

#------------------------------main func ----------------------------------	
if __name__ == "__main__":
# nra_init(nra)

    # timedata = time.time()
	msg = ("****************************************************************************\n")

	r = requests.get('https://www.screener.in/company/ASIANPAINT/consolidated/')
	df = ParseNCreatedf(r)
	print(df)



















	

	
    
    print(msg)