# Generated by Django 2.2 on 2019-05-19 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0009_events_df_filters_df'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Events_df',
        ),
        migrations.DeleteModel(
            name='Events_filt',
        ),
        migrations.DeleteModel(
            name='Filters_df',
        ),
    ]
