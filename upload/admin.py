from django.contrib import admin
from .models import Events_file, Events_df, Events_filt, AlarmsData, Filters_file, Filters_df, FiltersDevices
from . import insert_data, insert_filters, dataframe_db_alarms, dataframe_db_filters, filter_data

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

def db_alarms(modeladmin, request, queryset):
    #queryset.update(added_to_db='y')
    for obj in queryset:
        filename = obj.events
        dataframe_db_alarms.data_alarms(filename)
    queryset.update(added_to_df='y')
db_alarms.short_description = 'Dataframe alarms'

def db_filters(modeladmin, request, queryset):
    #queryset.update(added_to_db='y')
    for obj in queryset:
        filename = obj.filters
        dataframe_db_filters.data_filters(filename)
    queryset.update(added_to_df='y')
db_filters.short_description = 'Dataframe filters'

def filt_alarms(modeladmin, request, queryset):
    #queryset.update(added_to_db='y')
    for obj in queryset:
        filename = obj.events
        filter_data.filtering(filename)
    queryset.update(filtered_db='y')
filt_alarms.short_description = 'Filter data'

def test_pandas1(modeladmin, request, queryset):
    dataframe_db_alarms.data_alarms()
test_pandas1.short_description = "test dataframe pandas"

def test_pandas2(modeladmin, request, queryset):
    dataframe_db_filters.data_filters()
test_pandas2.short_description = "test dataframe pandas"

class Events_fileAdmin(admin.ModelAdmin):
    list_display = ['events', 'added_to_db', 'upload_date']
    ordering = ['-upload_date']
    actions = [mark_updated1, test_pandas1, db_alarms, filt_alarms]

class Filters_fileAdmin(admin.ModelAdmin):
    list_display = ['filters', 'added_to_db', 'upload_date']
    ordering = ['-upload_date']
    actions = [mark_updated2, test_pandas2, db_filters]

#admin.site.register(Events_file) # the only line needed to upload a file
admin.site.register(Events_file, Events_fileAdmin) # upload file and more info
admin.site.register(Filters_file, Filters_fileAdmin)
