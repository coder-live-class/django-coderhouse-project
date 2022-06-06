from django import forms

class ProfesorForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Nombre')
    last_name = forms.CharField(max_length=40, label='Apellido')
    email = forms.EmailField(label='Correo electrónico')
    profession = forms.CharField(max_length=40, label='Profesión')
