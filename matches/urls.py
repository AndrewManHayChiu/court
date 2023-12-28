from django.urls import path

from . import views

app_name = 'matches'
urlpatterns = [
    path('', views.match_list, name='match'),
    path('add_match/', views.create_match_and_set, name='add_match'),
    # path('match_set/<int:match_id>/', views.create_set, name='match_set')
]