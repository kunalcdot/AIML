import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Sample_Weather_Data.csv')

## dataframe properties / func
##------------------
df.shape
df.columns
df.info()
df.head()
df.tail()

df.count() ## total non null elements
df['Weather'].unique() # print the unique entries
df['Weather'].nunique() # number of unique entries
df['col_name'].value_counts() #print the number of time each unique value presents

df.isnull().sum()
df.fillna(0)
df.fillna({
	'cola':value,
	'colb':value
})
df.dropna(thresh=2) # drop the row if less than 2 non-null value 

#########  Groupby method ###
g = df.groupby('Wind Speed_km/h') # create an object with different dataframe
g.get_group(4).. 
g[col_name].mean()
############

## lambda ##
df['price_category'] = df.apply(lambda x: "Affordable" if x['price'] < 80 else "High Cost", axis=1)
# 'price_category' is new col. 

df['new'] = df.apply(lambda x: 1 if x['col1'] == x['col2'] else 0, axis=1) # similar to excel comarison b/w 2 cols.
###-------------------------------------------------------








