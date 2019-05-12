import pandas as pd
from .models import FiltersDevices

def insert_filters_into_db(file):
    print("Inserting filters to DB from file- ", file)
    data = pd.read_excel(file)
    # data=file_content.drop(columns=['ev_ReceivingTime','ev_ReceivingTimeUTC','dev_ID',
    #                                 'ev_DeviceNumber','ev_Status','ev_DescriptionLocalized',
    #                                 'par_ID', 'ev_PhysicalDeviceNumber','ev_CustomData'], axis='1')

    # iterate on the dataset to store into DB only the required values
    for row in  data.itertuples():
            filters = FiltersDevices(Code=row.Code, Text=row.Text, Tractament1=row.Tractament1, Tractament2=row.Tractament2,Tractament3=row.Tractament3, Device_Type=file)
            filters.save()

    print("Saved")