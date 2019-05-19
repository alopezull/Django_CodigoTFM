from django.contrib import admin
from .models import Events_file, AlarmsData, Filters_file, FiltersDevices
from . import insert_data, insert_filters, dataframe_db_alarms, dataframe_db_filters

# new fuction to add an action into admin
def mark_updated1(modeladmin, request, queryset):
    #queryset.update(added_to_db='y')
    for obj in queryset:
        filename = obj.events
        insert_data.insert_data_into_db(filename)
    queryset.update(added_to_db='y')
mark_updated1.short_description = 'Add the contained data to database'

def mark_updated2(modeladmin, request, queryset):
    #queryset.update(added_to_db='y')
    for obj in queryset:
        filename = obj.filters
        insert_filters.insert_filters_into_db(filename)
    queryset.update(added_to_db='y')
mark_updated2.short_description = 'Add the contained filters to database'

def test_pandas1(modeladmin, request, queryset):
    dataframe_db_alarms.data_alarms()
test_pandas1.short_description = "test dataframe alarms in pandas"

def test_pandas2(modeladmin, request, queryset):
    dataframe_db_filters.data_filters()
test_pandas2.short_description = "test dataframe filters in pandas"

class Events_fileAdmin(admin.ModelAdmin):
    list_display = ['events', 'added_to_db', 'upload_date']
    ordering = ['-upload_date']
    actions = [mark_updated1, test_pandas1]

class Filters_fileAdmin(admin.ModelAdmin):
    list_display = ['filters', 'added_to_db', 'upload_date']
    ordering = ['-upload_date']
    actions = [mark_updated2, test_pandas2]

#admin.site.register(Events_file) # the only line needed to upload a file
admin.site.register(Events_file, Events_fileAdmin) # upload file and more info
admin.site.register(Filters_file, Filters_fileAdmin)
