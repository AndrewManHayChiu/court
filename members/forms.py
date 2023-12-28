from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        
        fields = (
            'gender',
            'handedness',
        )
    
class NewUserForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'username',
        })
    )
    
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'first_name',
        })
    )
    
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'last_name',
        })
    )
    
    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            'type': 'email',
            }),
        required=True)
    
    class meta:
        model = User
        fields = (
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2'
        )
        
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user