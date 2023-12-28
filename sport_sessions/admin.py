from django.contrib import admin

from .models import Session, SessionRSVP

class SessionRsvpAdmin(admin.StackedInline):
    model = SessionRSVP
    
    list_display = [
        'session',
        'user',
    ]

class SessionAdmin(admin.ModelAdmin):
    model = Session
    
    list_display = [
        'club',
        'start_time',
        'end_time',
        'max_attendees'
    ]
    
    fieldsets = (
        (None, {'fields': ['club', 'created_at', 'updated_at', 'deleted_at', 'notes']}),
        ('Details', {'fields': ['date', 'start_time', 'end_time', 'max_attendees']}),
        ('Singles / Doubles', {'fields': ['singles', 'doubles']}),
        ('Settings', {'fields': ['hidden', 'waiting_list_enabled']})
    )   
    
    readonly_fields = ('created_at', 'updated_at', 'deleted_at')
    
    inlines = [SessionRsvpAdmin]
    
# Register your models here.
admin.site.register(Session, SessionAdmin)