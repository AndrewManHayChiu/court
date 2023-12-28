from django.urls import path

from .views import EditProfileView, ProfileDetailView, ProfileView, SignUpView

app_name='members'
urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('<int:id>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('<int:id>/edit', EditProfileView.as_view(), name='edit_profile'),
    path('signup/', SignUpView.as_view(), name='signup'),
]