from django.contrib import admin

from .models import Profile

# Create custom profile
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    
    list_display = ('user', 'created_at', 'updated_at')
    
    fieldsets = [
        (None, {'fields': ['user', 'created_at', 'updated_at', 'deleted_at']}),
        ('Profile', {'fields': ['gender', 'handedness']}),
        ('Friends', {'fields': ['follows']}),        
    ]
    
    readonly_fields = ('created_at', 'updated_at', 'deleted_at')    
    
    

# Register your models here.
admin.site.register(Profile, ProfileAdmin)