from .models import AlarmsData
import pandas as pd

def filt_forms (alarms, fechaini, fechafin, box, dev):
	alarm1=alarms[(alarms["ev_EventTime"]>=fechaini) & (alarms["ev_EventTime"]<=fechafin)]
	alarm_date=len(alarm1)
	alarm2=alarms[alarms["BedRef"]==box]
	alarm_box=len(alarm2)
	if dev=="Alaris":
		alarm3=alarms[alarms['ev_DeviceName'].str.contains('Alaris')]
	else:
		alarm3=alarms[alarms["ev_DeviceName"]==dev]
	alarm_dev=len(alarm3)
	if dev=="Alaris":
		alarm4=alarms[(alarms["ev_EventTime"]>=fechaini) & (alarms["ev_EventTime"]<=fechafin) & (alarms["BedRef"]==box) & (alarms['ev_DeviceName'].str.contains('Alaris'))]
	else:
		alarm4=alarms[(alarms["ev_EventTime"]>=fechaini) & (alarms["ev_EventTime"]<=fechafin) & (alarms["BedRef"]==box) & (alarms["ev_DeviceName"]==dev)]
	alarm_tot=len(alarm4)
	return (alarm_date, alarm_box, alarm_dev, alarm_tot)