
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("<h1 style='color:blue;text-align:center'>Hello, World!</h1>")
    context = {"title": "Home"}
    return render(request, 'home.html', context)


def register(request):
    return render(request, 'register.html')


def about(request):
    return render(request, 'about.html')


def login(request):
    return render(request, 'login.html')