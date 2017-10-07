import pandas as pd
from pandas import *
import requests
import numpy as np
from pandas.io.parsers import TextParser
from bs4 import BeautifulSoup
import math


url = "https://www.sec.gov/Archives/edgar/data/51143/000005114313000007/ibm13q3_10q.htm"
response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')
df = pd.read_html(url)[5]
#df.to_csv("123.csv",mode='a')
# i = 0
# for d in df:
# 	d.to_csv("abcde.csv",mode='a')
# 	i+=1
check = df.isnull().any().any()
new = DataFrame(columns = range(0,df.iloc[:].shape[0]),index= range(0,df.loc[:].shape[0]))
m = 0
i = 0
for row in df.loc[:]:
    j = 0
    n = 0
    for co in df.iloc[:]:
        if type(df.ix[i,j])==str or (not math.isnan(df.ix[i,j])):
            new.ix[i,j] = df.ix[i,j]
            j+=1
            n+=1
        else:
            j+=1
            n+=1
            continue
    i+=1
    m+=1
print(new)
new.to_csv("123.csv",mode='a')

	#new = new.drop所有空的列


# df.to_csv("123.csv",mode='a')
# for row in df.loc[:]:
# 	if np.isnan(df.ix[i,0]):
# 		df.loc[i] = df.loc[i].shift(periods=2,axis=1)
# 		new.loc[i] = df.loc[i]
# 		i+=1
# 	else:
# 		new.loc[i] = df.loc[i]
	#new = new.drop所有空的列


# i = 0
# pieces = []
# for d in df:
# 	i+=1
# 	data = DataFrame(d)
# 	data.dropna(how='all')
# 	pieces.append("%s.csv"%i)
# merged_data = pd.concat(pieces)
# final_data = "%s-final-data.csv"%self.__year
# merged_data.to_csv(final_data)

# df = DataFrame(800,10)
# ro = 0
# co = 0
# for th in th_tags:
#     column_names.append(th.get_text())
# for d in df:
# 	for t in d.find_all('table'):
# 		for i in t.find_all('tr'):
# 			ro+=1
# 			for j in i.find_all('td'):

# 				if (j.get_text()!="NaN")|j.get_text()|(j.get_text()!="$"):
# 					co+=1
# 					df.iat[ro,co] = j.get_text()
# 				else: continue




'''
for t in soup:
	read_table()
print(df.columns)
print(df.index)


for t in soup:

	rows = t.find_all('tr')
	df = DataFrame(rows)
	print(df)
	header_df = DataFrame(rows[0])
	data_df = DataFrame(rows[1:])
	print(header_df)
	print(data_df)

for r in rows[1:]:
	data = r.find_all("{}".format('td'))
	df = data.text
	print(df)
'''