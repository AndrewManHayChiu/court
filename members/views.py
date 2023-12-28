
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import UpdateView


from .forms import NewUserForm, EditProfileForm

from .models import Profile

# Create your views here.

class EditProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'members/edit_profile.html'

    def get_object(self, queryset=None):
        return self.request.user.profile

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(
            reverse_lazy(
                'members:profile_detail', 
                kwargs={'id': self.object.id}
            )
        )

class ProfileView(generic.ListView):
    model = Profile
    template_name = 'members/profiles.html'

class ProfileDetailView(generic.DetailView):
    model = Profile
    template_name = 'members/profile_details.html'

    def get_user(self, profile):
        User = get_user_model()
        try:
            user = User.objects.get(profile=profile)
        except User.DoesNotExist:
            user = None
        return user
    
    def get_object(self):
        id = self.kwargs.get('id')
        profile = get_object_or_404(Profile, id=id)
        return profile
    
    # Override default context to add matches
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        user = self.get_user(profile)
        matches = (user.team_one.all() | user.team_two.all()).distinct()
        context['profile'] = profile
        context['user'] = user
        context['matches'] = matches
        context['is_user'] = self.request.user == user
        return context
    
class SignUpView(generic.CreateView):
    # This is the default Django view
    # form_class = UserCreationForm 
    form_class = NewUserForm
    success_url = reverse_lazy('core:home')
    template_name = 'members/signup.html'