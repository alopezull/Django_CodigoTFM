from .models import AlarmsData
import pandas as pd


def analysis(count_data, filters):
	cuenta={}
	for x in count_data['Text']:
		cuenta[x]=count_data.ev_Description.isin([x]).sum(axis=0)
	df_cuenta=pd.DataFrame.from_dict(cuenta,orient='index')
	return cuenta

