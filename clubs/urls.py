from django.urls import path

from . import views

app_name = 'clubs'
urlpatterns = [
    path('', views.club, name='club'),
    path('add_club/', views.create_club, name='add_club'),
    path('<int:id>/', views.club_detail, name='club_detail'),
    path('<int:id>/edit_club/', views.edit_club, name='edit_club'),
]