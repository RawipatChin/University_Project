from django.urls import path
from . import views

urlpatterns = [
    path('', views.cloths, name='cloths'),
    path('<int:cloth_id>', views.cloth, name='cloth'),
]
