from django.urls import path
from . import views

urlpatterns = [
    path('summertravel', views.summertravel, name='summertravel'),
    path('raintravel', views.raintravel, name='raintravel'),
    path('wintertravel', views.wintertravel, name='wintertravel'),
]