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
df.describe(include=["object", "bool"]) # to include objects
df.describe().T # only numeric cols 

df.count() ## total non null elements
df['Weather'].unique() # print the unique entries
df['Weather'].nunique() # number of unique entries
df['col_name'].value_counts() #print the number of time each unique value presents
df['col_name'].value_counts(normalize = True) #to get percentage wise data.. good for plotting


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

# sorting
df.sort_values(by="Total day charge", ascending=False)
# change col type
df["Churn"] = df["Churn"].astype("int64") # from bol to integer



## lambda ##
df['price_category'] = df.apply(lambda x: "Affordable" if x['price'] < 80 else "High Cost", axis=1)
df_high_earn['married'] = df_high_earn['marital-status'].apply(lambda x: 1 if x[0:7] == 'Married' else 0)
# 'price_category' is new col. 

df['new'] = df.apply(lambda x: 1 if x['col1'] == x['col2'] else 0, axis=1) # similar to excel comarison b/w 2 cols.
###-------------------------------------------------------

########################################
        # Graph Plot
########################################
# Univariate distribution---------------------
# using pandas command
fg = df['Department'].value_counts().plot(kind='bar', title='Distribution',rot=45)
fg.set_xlabel('Department')
fg.set_ylabel('Count')
plt.show()
# ----------------------

# using matplotlib command 
Y = df['Department'].value_counts()
X = df['Department'].unique()
plt.bar(X,Y,color = 'cyan')
plt.xticks(rotation = 45)
plt.xlabel('Department')
plt.ylabel('Count')
plt.title('Employee Distribution among Departments')
plt.show()

###------
    # histogram and PDF plot ---> only for numeric data
ax = df['Speed_mph'].plot(kind='kde', title='Coaster Speed (mph)')
ax.set_xlabel('Speed (mph)')  

## Map method ##
# can be used to label any data.. like high,mid,low -> 2,1,0
d = {"High": 2, "Mid": 1, "Low":0}
df["International plan"] = df["International plan"].map(d)


# Multivariate distribution-- => Correlation-------------------
# crosstab() / contingency table

pd.crosstab(df["Churn"], df["International plan"],normalize=True,margins=True) ## margin gives subtotal










