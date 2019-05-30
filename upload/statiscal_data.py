from upload.models import AlarmsData
import pandas as pd

def statiscal(alarmas):
	mensual_total= alarmas.resample('M').sum()
	diario_total=mensual/30
	mensual_mean= alarmas.resample('M').mean()
	diario_mean=mensual/30
	mensual_max=alarmas.resample('M').max()
	diario_max=mensual_max/30
	mensual_min=alarmas.resample('M').min()
	diario_min=mensual_min/30

	return (diario_total, diario_mean, diario_max, diario_min)

