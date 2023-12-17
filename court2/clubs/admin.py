from django.contrib import admin
from .models import Club, Location

class ClubAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Description', {'fields': ['description']}),
        ('Website', {'fields': ['website']}),
    ]
    
    list_display = ['name', 'description', 'website']
    
class LocationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Address', {'fields': ['address']}),
        ('City', {'fields': ['city']}),
        ('State', {'fields': ['state']}),
        ('Country', {'fields': ['country']}),
        ('Postal Code', {'fields': ['postal_code']}),
    ]
    
    list_display = ['name', 'address', 'city', 'state', 'country', 'postal_code']

# Register your models here.
admin.site.register(Club, ClubAdmin)
admin.site.register(Location, LocationAdmin)