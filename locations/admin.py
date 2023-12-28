from django.contrib import admin

from .models import Location

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'state')
    
    fieldsets = [
        (None, {'fields': ['name', 'created_by', 'created_date', 'modified_date']}),
        ('Location', {'fields': ['address1', 'address2', 'suburb', 'state', 'country', 'zip_code']}),
    ]
    
    readonly_fields = ['created_by', 'created_date', 'modified_date']
    

# Register your models here.
admin.site.register(Location, LocationAdmin)