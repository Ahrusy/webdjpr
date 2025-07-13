from django.shortcuts import render
# myproject/pages/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contacts(request):
    return render(request, 'contacts.html')

def data_page(request):
    return render(request, 'pages/data.html')

def test_page(request):
    return render(request, 'pages/test.html')