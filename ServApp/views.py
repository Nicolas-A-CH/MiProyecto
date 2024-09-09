from django.shortcuts import render
from ServApp.models import Servicio

# Create your views here.
def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, "ServApp/servicios.html", {'servicios': servicios})
