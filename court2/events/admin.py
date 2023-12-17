from django.contrib import admin
from .models import Event, EventRsvp


class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'date']}),
        ('Details', {'fields': ['club', 'location', 'player_limit']}),
        ('Log', {'fields': ['created_datetime', 'updated_datetime', 'deleted_datetime']})
    ]
    
    list_display = ['name', 'club', 'location', 'date', 'player_limit', 'created_datetime']

class EventRsvpAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['event']}),
        ('User', {'fields': ['user']}),
        ('RSVP', {'fields': ['rsvp', 'created_datetime', 'updated_datetime']}),
    ]
    
    list_display = ['event', 'user', 'rsvp', 'created_datetime', 'updated_datetime']

# Register your models here.
admin.site.register(Event, EventAdmin)
admin.site.register(EventRsvp, EventRsvpAdmin)  