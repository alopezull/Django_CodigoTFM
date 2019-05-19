from django.db import models
from django_pandas.managers import DataFrameManager


# Create your models here.

# A status to save if the file was used to update the db or not. Default = no
STATUS_FILE = (
    ('y', 'added'),
    ('n', 'not added'),
)

class Events_file(models.Model):
    events = models.FileField(upload_to='events')
    added_to_db = models.CharField(max_length=1, choices=STATUS_FILE, default='n')
    upload_date = models.DateTimeField('upload date')


class AlarmsData(models.Model):
    ev_ID = models.IntegerField(default=0)
    ev_EventTime = models.DateTimeField('date event')
    PatientRef = models.IntegerField(default=0)
    BedRef = models.CharField(max_length=10)
    ev_DeviceName = models.CharField(max_length=30)
    ev_SerialNumber = models.CharField(max_length=50)
    ev_EventType = models.IntegerField(default=0)
    ev_Description = models.CharField(max_length=200)
    ev_Code = models.CharField(max_length=200)
    ev_EndEvent = models.IntegerField(default=0)
    filename = models.CharField(max_length=200, default='filename missing')

class Filters_file(models.Model):
    filters = models.FileField(upload_to='filters')
    added_to_db = models.CharField(max_length=1, choices=STATUS_FILE, default='n')
    upload_date = models.DateTimeField('upload date')

class FiltersDevices(models.Model):
    Code = models.CharField(max_length=200)
    Text = models.CharField(max_length=200)
    Tractament1= models.IntegerField(default=0)
    Tractament2= models.IntegerField(default=0)
    Tractament3= models.IntegerField(default=0)
    Device_Type = models.CharField(max_length=200, default='type device missing')
    