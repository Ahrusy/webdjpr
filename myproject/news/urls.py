# myproject/pages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='news_home'),
]