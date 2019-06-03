import pandas as pd
from upload.models import AlarmsData


def insert_data_into_db(file):
    print("Inserting data to DB from file- ", file)
    data = pd.read_excel(file)
    # iterate on the dataset to store into DB only the required values
    for row in  data.itertuples():
            alarm = AlarmsData(ev_ID=row.ev_ID, ev_EventTime=row.ev_EventTime, PatientRef=row.PatientRef,
                               BedRef=row.BedRef, ev_DeviceName=row.ev_DeviceName, ev_SerialNumber=row.ev_SerialNumber,
                               ev_EventType=row.ev_EventType, ev_Description=row.ev_Description, ev_Code=row.ev_Code,
                               ev_EndEvent=row.ev_EndEvent, filename=file)
            alarm.save()

    print("Saved")
    