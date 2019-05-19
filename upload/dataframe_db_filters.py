from .models import FiltersDevices
import pandas as pd

def data_filters():
	df_filters = pd.DataFrame.from_records(FiltersDevices.objects.all().values().distinct());
	print(df_filters.head())