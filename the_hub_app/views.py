from django.shortcuts import render, redirect
from django.http import HttpResponse
#from .models import 


def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def news(request):
    return render(request, 'pages/news.html')

def social(request):
    return render(request, 'pages/social.html')


def sports(request):
    return render(request, 'pages/sports.html')

def sports_news(request):
    return render(request, 'pages/sports_news.html')
# Create your views here.
