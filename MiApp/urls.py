from django.urls import path
from MiApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name='Inicio'),    
    path('tienda/', views.tienda, name='Tienda'),   
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)