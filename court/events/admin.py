from django.contrib import admin
from .models import Event, EventRsvp


class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'date']}),
        ('Details', {'fields': ['club', 'location', 'player_limit']}),
    ]
    
    list_display = ['name', 'club', 'location', 'date', 'player_limit']

class EventRsvpAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['event']}),
        ('User', {'fields': ['user']}),
        ('RSVP', {'fields': ['rsvp']}),
        ('RSVP Datetime', {'fields': ['rsvp_datetime']}),
    ]
    
    list_display = ['event', 'user', 'rsvp', 'rsvp_datetime']

# Register your models here.
admin.site.register(Event, EventAdmin)
admin.site.register(EventRsvp, EventRsvpAdmin)  