from .models import AlarmsData, FiltersDevices
import pandas as pd


def analysis(count_data, filters):
	if [(filters['Tractament1']==1) | (filters['Tractament1']==2)]:
		cuenta1={}
		for x in filters.Text:
			cuenta1[x]=count_data.ev_Description.isin([x]).sum(axis=0)
		df_cuenta11=pd.DataFrame.from_dict(cuenta1,orient='index')
		df_cuenta1=df_cuenta11.rename(columns={0 :'Cantidad'}, inplace=True)

	if [(filters['Tractament2']==1) | (filters['Tractament2']==2)]:
		cuenta2={}
		for x in filters.Text:
			cuenta2[x]=count_data.ev_Description.isin([x]).sum(axis=0)
		df_cuenta22=pd.DataFrame.from_dict(cuenta2,orient='index')
		df_cuenta2=df_cuenta22.rename(columns={0 :'Cantidad'}, inplace=True)

	if [(filters['Tractament3']==1) | (filters['Tractament3']==2)]:
		cuenta3={}
		for x in filters.Text:
			cuenta3[x]=count_data.ev_Description.isin([x]).sum(axis=0)
		df_cuenta33=pd.DataFrame.from_dict(cuenta3,orient='index')
		df_cuenta3=df_cuenta33.rename(columns={0 :'Cantidad'}, inplace=True)

	return (df_cuenta1, df_cuenta2, df_cuenta3)

