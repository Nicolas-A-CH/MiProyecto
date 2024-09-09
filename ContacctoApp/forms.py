from django import forms

class FormContacto(forms.Form):
    nombre = forms.CharField(max_length=30, label='Nombre', required=True)
    correo = forms.EmailField(label="Correo Electrónico", required=True)
    mensaje = forms.CharField(
        max_length=250, 
        required=True, 
        label="Mensaje", 
        widget=forms.Textarea
    )
