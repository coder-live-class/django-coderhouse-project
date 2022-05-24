import datetime
from django import forms
from django.forms import ModelForm
from app_coder.models import Profesor


class CourseForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Nombre')
    code = forms.IntegerField(label='Camada')


class ProfesorForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Nombre')
    last_name = forms.CharField(max_length=40, label='Apellido')
    email = forms.EmailField(label='Correo electrónico')
    profession = forms.CharField(max_length=40, label='Profesión')

# class ProfesorForm(ModelForm):
#     class Meta:
#         model = Profesor
#         fields = '__all__'


class HomeworkForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Nombre de la Entrega')
    due_date = forms.DateField(
        label='Fecha de Entrega',
        widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'})
    )
    is_delivered = forms.BooleanField(label='Entregado', required=False)
