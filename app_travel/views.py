from django.shortcuts import render

# Create your views here.

def summertravel(request):
    return render(request, 'app_travel/summertravel.html')

def raintravel(request):
    return render(request, 'app_travel/raintravel.html')

def wintertravel(request):
    return render(request, 'app_travel/wintertravel.html')