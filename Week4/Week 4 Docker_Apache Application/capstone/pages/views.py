from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def mountain (request):

    return render(request, 'pages/mountain.html')

def mountain_tn (request):
    return render(request, 'pages/mountain_tn.html')

def mountain_ca (request):
    return render(request, 'pages/mountain_ca.html')

def register (request):
    return render(request, 'pages/register.html')

def login (request):
    return render(request, 'pages/login.html')

def booked(request):
    return render(request, 'pages/booked.html')

def saved(request):
    return render(request, 'pages/saved.html')

