from .models import AlarmsData
import pandas as pd

def cantidad_box_dev(alarms, box, dev):
	# Alarmas por box
	if (alarms['BedRef']==box) & (alarms['ev_DeviceName']==dev):
		prova = alarms['ev_ID'].count()
	else:
		print("No existen valores para este box y dispositivo")
	return prova