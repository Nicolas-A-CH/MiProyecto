from django.shortcuts import render, HttpResponse

# Create your views here.

def inicio(request):
    return render(request, "MiApp/inicio.html")

def tienda(request):
    return render(request, "MiApp/tienda.html")