from django.urls import path

from . import views

app_name='locations'
urlpatterns = [
    path('', views.location, name='location'),
    path('<int:location_id>/', views.location_detail, name='location_detail'),
    path('add_location/', views.create_location, name='add_location'),
]