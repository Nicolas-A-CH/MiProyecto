from django.shortcuts import redirect, render
from .forms import FormContacto
from django.core.mail import EmailMessage
from MiProyecto import settings

# Create your views here.
def contacto(request):
    
    form_contacto = FormContacto()
    
    if request.method == "POST":
        form_contacto = FormContacto(data=request.POST)
        if form_contacto.is_valid():
            nombre = request.POST.get("nombre")
            correo = request.POST.get("correo")
            mensaje = request.POST.get("mensaje")
            
            email = EmailMessage(
                "Mensaje desde Mi proyecto",
                f"El usuario {nombre} con dirección de correo {correo} escribió lo siguiente:\n\n{mensaje}",
                settings.EMAIL_HOST_USER, 
                ["rogersprof@gmail.com"], 
                reply_to=[correo]
            )
            try:
                email.send()
                return redirect("/contacto/?ok")
            except:
                return redirect("/contacto/?error")
            
    return render(request, "ContactoApp/contacto.html", {'formulario': form_contacto})
