from upload.models import AlarmsData
import pandas as pd

def dataframe_db():
    df = pd.DataFrame.from_records(AlarmsData.objects.all().values().distinct());
    print(df.head())

