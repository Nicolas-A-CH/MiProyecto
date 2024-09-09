from django.shortcuts import render
from .forms import FormContacto
from django.core.mail import EmailMessage

# Create your views here.
def contacto(request):
    
    form_contacto = FormContacto()
    
    if request.method =="POST":
        form_contacto = FormContacto(datos = request.POST)
        if form_contacto.is_valid:
            nombre = request.POST.get("nombre")
            correo = equest.POST.get("correi")
            mensaje = request.POST.get("mensaje")
            
            email = EmailMessage("")
    
    return render(request, "ContactoApp/contacto.html", {'formulario': form_contacto})
