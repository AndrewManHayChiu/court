from django.urls import path

from . import views

app_name='core'
urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('features/', views.features, name='features'),
    path('faq/', views.faq, name='faq'),
    path('pricing/', views.pricing, name='pricing'),
    path('privacy/', views.privacy, name='privacy'),
]

