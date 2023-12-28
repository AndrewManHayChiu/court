from django import forms

from .models import Location

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        
        fields = (
            'name',
            'address1',
            'address2',
            'suburb',
            'state',
            'country',
            'zip_code',
        )
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }