from django.shortcuts import render
from .forms import FormContacto
from django.core.mail import EmailMessage
from MiProyecto import settings

# Create your views here.
def contacto(request):
    
    form_contacto = FormContacto()
    
    if request.method =="POST":
        form_contacto = FormContacto(datos = request.POST)
        if form_contacto.is_valid:
            nombre = request.POST.get("nombre")
            correo = equest.POST.get("correi")
            mensaje = request.POST.get("mensaje")
            
            email = EmailMessage("Mensaje desde Mi proyecto",
                                 "El usuario {} con direccion de correo{} escribio lo siguiente"
                                 .format(nombre, correo, mensaje), settings.EMAIL_HOST_USER,
                                 correo, reply_to=[correo])
            
            
    return render(request, "ContactoApp/contacto.html", {'formulario': form_contacto})
