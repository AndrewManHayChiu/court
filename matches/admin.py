from django.contrib import admin
from nested_admin import NestedStackedInline, NestedModelAdmin, NestedTabularInline

from .models import Match, Rally, Set, Team

# class RallyInline(NestedStackedInline):
#     model = Rally
#     extra = 0

class SetAdmin(admin.StackedInline):
    model = Set
    extra = 0
    # inlines = [RallyInline]

class MatchAdmin(admin.ModelAdmin):
    model = Match
    
    inlines = [SetAdmin]
    
    list_display = ('id', 'session', 'date', 'combination')
    
    fieldsets = (
        (None, {'fields': ['session', 'date', 'time', 'created_at', 'updated_at', 'deleted_at']}),
        ('Type', {'fields': ['combination']}),
        ('Teams', {'fields': ['team_one', 'team_two']})
    )
    
    readonly_fields = ('created_at', 'updated_at', 'deleted_at')

# Register your models here.
admin.site.register(Match, MatchAdmin)
admin.site.register(Team)