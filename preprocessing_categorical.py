import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
from sklearn.cluster import KMeans
from sklearn import preprocessing, cross_validation
import pandas as pd
import openpyxl

df=pd.read_excel('abc.xlsx')
df.drop(['CASE_SUBMITTED_DAY','CASE_SUBMITTED_MONTH','CASE_SUBMITTED_YEAR','DECISION_DAY','DECISION_MONTH','DECISION_YEAR','NAICS_CODE'],1,inplace=True)
df.convert_objects(convert_numeric=True)
df.fillna(0,inplace=True)
#print(df.head())

def handle_non_numerical_data(df):
	columns=df.columns.values

	for column in columns:
		text_digit_vals={}
		def convert_to_int(val):
			return text_digit_vals[val]

		if df[column].dtype!= np.int64 and df[column].dtype!= np.float64:
			column_contents=df[column].values.tolist()
			unique_elements=set(column_contents)
			x=0
			for unique in unique_elements:
				if unique not in text_digit_vals:
					text_digit_vals[unique]=x
					x+=1
			df[column]= list(map(convert_to_int,df[column]))

	return df
df=handle_non_numerical_data(df)
fp=pd.ExcelWriter('result.xlsx', engine='xlsxwriter')
df.to_excel(fp, 'sheet1')
fp.save()
