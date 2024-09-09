from django.urls import path
from ServApp import views

urlpatterns = [    
    path('', views.servicios, name='Servicios'),
]