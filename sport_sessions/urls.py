from django.urls import path

from . import views

app_name = 'sport_sessions'
urlpatterns = [
    path('', views.session, name='sessions'),
    path('<int:id>/', views.session_detail, name='session_detail'),
    path('create_session/', views.create_session, name='create_session'),
    path('<int:id>/rsvp/', views.SessionRSVPCreateView.as_view(), name='session_rsvp_create'),
    path('<int:id>/edit/', views.edit_session, name='edit_session'),
]