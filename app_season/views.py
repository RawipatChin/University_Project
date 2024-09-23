from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def sunny(request):
    return render(request, 'app_season/sunny.html')

def rainy(request):
    return render(request, 'app_season/rainy.html')

def snowy(request):
    return render(request, 'app_season/snowy.html')
