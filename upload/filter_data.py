from .models import AlarmsData
import pandas as pd

def filtering (alarm1):
	alarm2=alarm1.drop(alarm1[alarm1["ev_DeviceName"]=="AGW"].index)
	alarm3=alarm2.drop(alarm2[(alarm2["ev_EventType"]==10) | (alarm2["ev_EventType"]==20) | (alarm2["ev_EventType"]==30)].index)  
	alarm4=alarm3.drop(alarm3[alarm3["ev_EndEvent"]==1].index)
	return alarm4