from upload.models import AlarmsData
import pandas as pd

def statiscal(alarm):
	# Cantidad de alarmas por código
	alarms_counts1 = alarm.groupby('ev_Code', as_index=False).agg({"ev_ID": "count"})
	# Si lo realizamos por descripción, los valores deberían ser los mismos:
	alarms_counts2 = alarm.groupby('ev_Description', as_index=False).agg({"ev_ID": "count"})
	alarms_counts2.rename(columns={'ev_Description': 'Alarmas', 'ev_ID': 'Cantidad'}, inplace=True)
	
	# Cantidad de alarmas por boxes
	alarms_counts3 = alarm.groupby('BedRef',as_index=False).agg({"ev_ID": "count"})
	
	# Cantidad de alarmas por dispositivos (Bombas, Monitor, Respirador)
	# Creamos diccionario con valores a reemplazar (información proporcionada por el fabricante)
	alarms_counts4=alarm.groupby('ev_DeviceName', as_index=False).agg({"ev_ID": "count"})
	
	return (alarms_counts1, alarms_counts2, alarms_counts3, alarms_counts4)

def get_alarms_quantity(alarms): 

	alarms_counts2 = alarm.groupby('ev_Description', as_index=False).agg({"ev_ID": "count"}) 
	alarms_counts2.rename(columns={'ev_Description': 'Alarmas', 'ev_ID': 'Cantidad'}, inplace=True)
 
	alarmas=[]
	cantidad=[]
	for row in alarms_counts2.itertuples(): 
		alarmas.append(row.Alarmas)
		cantidad.append(row.Cantidad)

	return (alarmas, cantidad)

