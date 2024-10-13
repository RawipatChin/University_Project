from django.urls import path
from . import views

urlpatterns = [
    path('summerfood', views.summerfood, name='summerfood'),
    path('rainfood', views.rainfood, name='rainfood'),
    path('winterfood', views.winterfood, name='winterfood'),
]