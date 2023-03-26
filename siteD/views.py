from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from .forms import TaskForm

def index(request):
    zap1 = {
        'title1': 'Главная страница',
        'tasks': models.Task.objects.all()
    }
    return render(request, "siteD/index.html", zap1)

def about(request):
    return render(request, "siteD/about.html")

def create(request):
    error = ""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
        else:
            error = 'Форма была заполнена неверно'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, "siteD/create.html", context)