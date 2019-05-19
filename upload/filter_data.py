from upload.models import AlarmsData
import pandas as pd

def filtering(alarm):
	# Filtramos los datos que no nos interesan
	alarm1 = alarm.drop(alarm[alarm['ev_DeviceName']=='AGW'].index)
	alarm2 = alarm1.drop(alarm1[(alarm1['ev_EventType']==10)|(alarm1['ev_EventType']==20)|(alarm1['ev_EventType']==30)].index)
	alarm3 = alarm2.drop(alarm2[alarm2['ev_EndEvent']==1].index)
	return(alarm3)