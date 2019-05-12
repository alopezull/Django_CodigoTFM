from django.contrib import admin
from .models import Events_file, AlarmsData, Filters_file, FiltersDevices
from . import insert_data, pandas_from_db, insert_filters

# new fuction to add an action into admin
def mark_updated(modeladmin, request, queryset):
    #queryset.update(added_to_db='y')
    for obj in queryset:
        filename = obj.events
        insert_data.insert_data_into_db(filename)
    queryset.update(added_to_db='y')
mark_updated.short_description = 'Add the contained data to database'

def mark_updated(modeladmin, request, queryset):
    #queryset.update(added_to_db='y')
    for obj in queryset:
        filename = obj.events
        insert_data.insert_filters_into_db(filename)
    queryset.update(added_to_db='y')
mark_updated.short_description = 'Add the contained filters to database'

def test_pandas(modeladmin, request, queryset):
    pandas_from_db.dataframe_db()
test_pandas.short_description = "test dataframe pandas"

class Events_fileAdmin(admin.ModelAdmin):
    list_display = ['events', 'added_to_db', 'upload_date']
    ordering = ['-upload_date']
    actions = [mark_updated, test_pandas]

class Filters_fileAdmin(admin.ModelAdmin):
    list_display = ['filters', 'added_to_db', 'upload_date']
    ordering = ['-upload_date']
    actions = [mark_updated, test_pandas]

#admin.site.register(Events_file) # the only line needed to upload a file
admin.site.register(Events_file, Events_fileAdmin) # upload file and more info
admin.site.register(Filters_file, Filters_fileAdmin)
