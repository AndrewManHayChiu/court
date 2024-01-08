from django.urls import path

from . import views

app_name = 'sport_sessions'
urlpatterns = [
    path('', views.session, name='sessions'),
    path('<uuid:uuid>/', views.session_detail, name='session_detail'),
    path('create_session/', views.create_session, name='create_session'),
    path('<int:id>/rsvp/', views.SessionRSVPCreateView.as_view(), name='session_rsvp_create'),
    path('<int:id>/edit/', views.edit_session, name='edit_session'),
    path('<int:id>/add_to_waitlist/', views.AddToWaitlistView.as_view(), name='add_to_waitlist'),
    path('rsvp/<int:rsvp_id>/delete/', views.remove_from_rsvp, name='remove_from_rsvp'),
    path('attendance/<int:rsvp_id>', views.toggle_attendance, name='toggle_attendance'),
    path('payment/<int:rsvp_id>', views.toggle_payment, name='toggle_payment'),
]