from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
    zap1 = {
        'title1': 'Главная страница',
        'tasks' : models.Task.objects.all()
    }
    return render(request, "siteD/index.html", zap1)

def about(request):
    return render(request, "siteD/about.html")