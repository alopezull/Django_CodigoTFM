from upload.models import FiltersDevices
import pandas as pd

def data_filters(FiltersDevices):
    df_filters = pd.DataFrame.from_records(FiltersDevices.objects.all().values().distinct());
    return(df_filters)
