from .models import AlarmsData
import pandas as pd

def analysis_filt(data1, data2, data3, data4):
	# Eliminamos valores nulos
	res1=data.drop(data1[data1[1]==0].index)
	res2=data.drop(data2[data2[1]==0].index)
	res3=data.drop(data3[data3[1]==0].index)
	res4=data.drop(data4[data4[1]==0].index)
	return (res1, res2, res3, res4)