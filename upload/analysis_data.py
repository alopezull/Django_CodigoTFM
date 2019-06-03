from .models import AlarmsData, FiltersDevices
import pandas as pd


def analysis(count_data, fechaini, fechafin, box, dev, filters):
	if [(count_data.ev_EventTime>=fechaini) & (count_data.ev_EventTime<=fechafin) & (count_data.BedRef==box) & (count_data.ev_DeviceName==dev)]:
		if [(filters['Tractament1']==1) | (filters['Tractament1']==2)]:
			cuenta1={}
			for x in filters.Text:
				cuenta1[x]=count_data.ev_Description.isin([x]).sum(axis=0)
			df_cuenta11=pd.DataFrame.from_dict(cuenta1,orient='index')
			df_cuenta11.rename(columns={0 :'Cantidad'}, inplace=True)
			df_cuenta1=df_cuenta11.drop(df_cuenta11[df_cuenta11['Cantidad']==0].index)

		if [(filters['Tractament2']==1) | (filters['Tractament2']==2)]:
			cuenta2={}
			for x in filters.Text:
				cuenta2[x]=count_data.ev_Description.isin([x]).sum(axis=0)
			df_cuenta22=pd.DataFrame.from_dict(cuenta2,orient='index')
			df_cuenta22.rename(columns={0 :'Cantidad'}, inplace=True)
			df_cuenta2=df_cuenta22.drop(df_cuenta22[df_cuenta22['Cantidad']==0].index)
		if [(filters['Tractament3']==1) | (filters['Tractament3']==2)]:
			cuenta3={}
			for x in filters.Text:
				cuenta3[x]=count_data.ev_Description.isin([x]).sum(axis=0)
			df_cuenta33=pd.DataFrame.from_dict(cuenta3,orient='index')
			df_cuenta33.rename(columns={0 :'Cantidad'}, inplace=True)
			df_cuenta3=df_cuenta33.drop(df_cuenta33[df_cuenta33['Cantidad']==0].index)			
	else: 
		df_cuenta=("No hay resultados disponibles")
	return (df_cuenta1, df_cuenta2, df_cuenta3)

