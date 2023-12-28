from datetime import datetime
from django import forms

from .models import Club

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        
        fields = (
            'name',
            'description',
            'sport',
            'location',
            'day',
            'time',
            'price',
            'members_price',
            'rsvp_required',
            'contact',
            'hidden',
        )
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'shuttles': forms.TextInput(attrs={'class': 'form-control'} ),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'time': forms.DateTimeInput(
                attrs={
                    'type': 'time',
                    'placeholder': 'HH:MM',
                    'class': 'form-control'}),
        }
        
        labels = {
            'rsvp_required': 'RSVP required?',
            'hidden': 'Hide this club?',
            'location': 'Stadium',
        }