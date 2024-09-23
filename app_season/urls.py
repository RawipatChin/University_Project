from django.urls import path
from . import views

urlpatterns = [
    path('sunny', views.sunny, name='sunny'),
    path('rainy', views.rainy, name='rainy'),
    path('snowy', views.snowy, name='snowy'),
]