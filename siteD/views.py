from django.shortcuts import render
from django.http import HttpResponse
from . import models
from .forms import TaskForm

def index(request):
    zap1 = {
        'title1': 'Главная страница',
        'tasks' : models.Task.objects.order_by('-id')
    }
    return render(request, "siteD/index.html", zap1)

def about(request):
    return render(request, "siteD/about.html")

def create(request):
    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, "siteD/create.html")