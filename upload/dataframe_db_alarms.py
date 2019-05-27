from .models import AlarmsData
import pandas as pd

def data_alarms(fechaini, fechafin, box, dev):
	df_alarms = pd.DataFrame.from_records(AlarmsData.objects.filter(ev_EventTime__lte=fechafin,
									ev_EventTime__gte=fechaini,
									BedRef=box,
									ev_DeviceName=dev).values().distinct())
	return df_alarms
