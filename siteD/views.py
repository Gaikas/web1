from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Привет Дима</h1>")

def about(request):
    return HttpResponse("<h2>Вторая страница</h2>")