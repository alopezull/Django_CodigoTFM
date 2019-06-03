import pandas as pd
from .models import FiltersDevices

def insert_filters_into_db(file):
    print("Inserting filters to DB from file- ", file)
    data = pd.read_excel(file)
    # iterate on the dataset to store into DB only the required values
    for row in  data.itertuples():
            filt = FiltersDevices(Code=row.Code, Text=row.Text, Tractament1=row.Tractament1, Tractament2=row.Tractament2,Tractament3=row.Tractament3, Device_Type=file)
            filt.save()

    print("Saved")