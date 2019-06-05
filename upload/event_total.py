from .models import AlarmsData
import pandas as pd

def recuento_total(alarms):
	# Recuento alarmas
	if (alarms.empty):
		print("No existen valores")
	else:
		# Hasta el primer filtraje
		alarms1=alarms[(alarms["ev_EventTime"]>="2018-07-01") & (alarms["ev_EventTime"]<="2018-05-14")]
		cant_alarms1=len(alarms1)
		# Hasta el segundo filtraje
		alarms2=alarms[(alarms["ev_EventTime"]>="2018-07-01") & (alarms["ev_EventTime"]<="2018-07-02")]
		cant_alarms2=len(alarms2)
		# Hasta el tercer filtraje
		alarms3=alarms[(alarms["ev_EventTime"]>="2018-07-01") & (alarms["ev_EventTime"]<="2019-02-28")]
		cant_alarms3=len(alarms3)
		# Sin paciente
		alarms_pac=alarms[alarms["PatientRef"]==0]
		cant_pac0=len(alarms_pac)
	return (cant_alarms1, cant_alarms2, cant_alarms3, cant_pac0)