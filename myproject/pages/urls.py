# myproject/pages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.data_page, name='data'),
    path('test/', views.test_page, name='test'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contacts/', views.contacts, name='contacts'),
]