from .models import AlarmsData
import pandas as pd
from django_pandas.io import read_frame

def data_alarms(AlarmsData):

	DataFrameManager = AlarmsData.Manager.from_queryset(DataFrameQuerySet)
    
    #df=AlarmsData.objects.all()
    #df_alarms=df.to_dataframe()

    #df_alarms = read_frame(df)

    #df_alarms = pd.DataFrame.from_records(AlarmsData.objects.all().values().distinct());
	return (DataFrameManager)