from django.contrib import admin

from polls.models import DataPoint

# Register your models here.

class DataPointAdmin(admin.ModelAdmin):
    list_display = ('x', 'y')
    search_fields = ('x', 'y')

admin.site.register(DataPoint, DataPointAdmin)