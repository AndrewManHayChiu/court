from datetime import datetime
from django import forms

from .models import Session, SessionRSVP

class SessionForm(forms.ModelForm):
    
    class Meta:
        model = Session
        
        fields = (
            'date',
            'start_time',
            'end_time',
            'doubles',
            'singles',
            'max_attendees',
            'notes',
            'hidden',
        )
        
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'placeholder': 'YYYY-MM-DD',
                    'class': 'form-control',
                    'value': datetime.now().strftime('%Y-%m-%d')}),
            'start_time': forms.DateTimeInput(
                attrs={
                    'type': 'time',
                    'placeholder': 'HH:MM',
                    'class': 'form-control'}),
            'end_time': forms.DateTimeInput(
                attrs={
                    'type': 'time',
                    'placeholder': 'HH:MM',
                    'class': 'form-control'}),
            'doubles': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }

class EditSessionForm(forms.ModelForm):
    
    class Meta:
        model = Session
        
        fields = (
            'date',
            'start_time',
            'end_time',
            'doubles',
            'singles',
            'max_attendees',
            'notes',
            'hidden',
        )
        
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'placeholder': 'YYYY-MM-DD',
                    'class': 'form-control'}),
            'start_time': forms.DateTimeInput(
                attrs={
                    'type': 'time',
                    'placeholder': 'HH:MM',
                    'class': 'form-control'}),
            'end_time': forms.DateTimeInput(
                attrs={
                    'type': 'time',
                    'placeholder': 'HH:MM',
                    'class': 'form-control'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(EditSessionForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.initial['start_time'] = self.instance.start_time.strftime('%H:%M')
            self.initial['end_time'] = self.instance.end_time.strftime('%H:%M')

class SessionRSVPForm(forms.ModelForm):
    non_user_name = forms.CharField(max_length=255, required=False)
    
    class Meta:
        model = SessionRSVP
        
        fields = (
            'user',
            'is_attending',
            'paid',
            'payment_method',
            'non_user_name',
        )
        
        # widgets = {
        #     'is_attending': forms.CheckboxInput(attrs={'class': 'form-control'}),
        #     'paid': forms.CheckboxInput(attrs={'class': 'form-control'}),
        #     'payment_method': forms.Select(attrs={'class': 'form-control'}),
        #     'non_user_name': forms.TextInput(attrs={'class': 'form-control'}),
        # }