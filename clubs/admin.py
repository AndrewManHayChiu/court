from django.contrib import admin

from .models import Club

class ClubAdmin(admin.ModelAdmin):
    list_display = [
        'name', 
        'description', 
        'location', 
        'day',
        'price',
        'rsvp_required',
        'hidden',
    ]
    
    fieldsets = [
        ('Club', {'fields': ['name', 'description', 'website', 'location', 'day']}),
        ('Prices', {'fields': ['price', 'members_price']}),
        ('Settings', {'fields': ['organiser', 'rsvp_required', 'hidden']})
    ]
    
# Register your models here.
admin.site.register(Club, ClubAdmin)