from upload.models import AlarmsData
import pandas as pd

def statiscal(AlarmsData):
	# Cantidad de alarmas por boxes
	statiscal_box = data.groupby('BedRef')['ev_ID'].count()
	# Cantidad de alarmas por dispositivos (Bombas, Monitor, Respirador)
	statiscal_devices = data.groupby('ev_DeviceName')['ev_ID'].count()
	# Cantidad de alarmas sin paciente dado de alta
	statiscal_nopatient=data[data['PatientRef'] == 0]
	return (statiscal_box, statiscal_devices, statiscal_nopatient)


