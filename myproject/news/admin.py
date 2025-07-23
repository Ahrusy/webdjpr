# news/admin.py
from django.contrib import admin
# Импортируем нашу модель News_post из текущего приложения (.)
from .models import News_post

# Регистрируем модель, чтобы она отображалась в админ-панели
admin.site.register(News_post)