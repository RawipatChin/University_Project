from django.shortcuts import render

# Create your views here.

def summerfood(request):
    return render(request, 'app_food/summerfood.html')

def rainfood(request):
    return render(request, 'app_food/rainfood.html')

def winterfood(request):
    return render(request, 'app_food/winterfood.html')