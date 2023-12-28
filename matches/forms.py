from django import forms
from django.contrib.auth.models import User
from datetime import datetime

from .models import Match, Rally, Set

class MatchForm(forms.ModelForm):
    
    class Meta:
        model = Match
        
        fields = (
            'date',
            'time',
            'session',
            # 'tournament',
            'is_doubles',
            'team_one',
            'team_two',
        )
        
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'placeholder': 'YYYY-MM-DD',
                    'class': 'form-control',
                    'value': datetime.now().strftime('%Y-%m-%d')}),
            'time': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'placeholder': 'HH:MM',
                    'class': 'form-control',
                    'value': datetime.now().strftime('%H:%M')}),
        }

class SetForm(forms.ModelForm):
    class Meta:
        model = Set
        
        fields = [
            # 'match', # This is automatically added when a match is created
            'set', 
            'winning_team',
            'winner_score',
            'loser_score',
            ]

# class RallyForm(forms.ModelForm):
#     server = forms.ModelChoiceField(queryset=Users.objects.all())
#     receiver = forms.ModelChoiceField(queryset=Users.objects.all())

#     class Meta:
#         model = Rally
#         fields = ['rally_number', 'server', 'receiver', 'shot', 'rally_result']