# Generated by Django 2.2 on 2019-06-05 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlarmsData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ev_ID', models.IntegerField(default=0)),
                ('ev_EventTime', models.DateTimeField(verbose_name='date event')),
                ('PatientRef', models.IntegerField(default=0)),
                ('BedRef', models.CharField(max_length=10)),
                ('ev_DeviceName', models.CharField(max_length=30)),
                ('ev_SerialNumber', models.CharField(max_length=50)),
                ('ev_EventType', models.IntegerField(default=0)),
                ('ev_Description', models.CharField(max_length=200)),
                ('ev_Code', models.CharField(max_length=200)),
                ('ev_EndEvent', models.IntegerField(default=0)),
                ('filename', models.CharField(default='filename missing', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Events_file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('events', models.FileField(upload_to='events')),
                ('added_to_db', models.CharField(choices=[('y', 'added'), ('n', 'not added')], default='n', max_length=1)),
                ('upload_date', models.DateTimeField(verbose_name='upload date')),
            ],
        ),
        migrations.CreateModel(
            name='Filters_file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filters', models.FileField(upload_to='filters')),
                ('added_to_db', models.CharField(choices=[('y', 'added'), ('n', 'not added')], default='n', max_length=1)),
                ('upload_date', models.DateTimeField(verbose_name='upload date')),
            ],
        ),
        migrations.CreateModel(
            name='FiltersDevices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(max_length=200)),
                ('Text', models.CharField(max_length=200)),
                ('Tractament1', models.IntegerField(default=0)),
                ('Tractament2', models.IntegerField(default=0)),
                ('Tractament3', models.IntegerField(default=0)),
                ('Device_Type', models.CharField(default='type device missing', max_length=200)),
            ],
        ),
    ]
