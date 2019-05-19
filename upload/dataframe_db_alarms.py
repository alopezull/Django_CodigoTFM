from .models import AlarmsData
import pandas as pd

def data_alarms():
	df_alarms = pd.DataFrame.from_records(AlarmsData.objects.all().values().distinct());
	print(df_alarms.head())
