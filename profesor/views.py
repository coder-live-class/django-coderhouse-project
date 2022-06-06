import random
import string
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.shortcuts import render

from profesor.models import Profesor
from profesor.forms import ProfesorForm


def profesor_list(request):
    profesors = Profesor.objects.all()

    context_dict = {
        'profesors': profesors
    }

    return render(
        request=request,
        context=context_dict,
        template_name="profesor/profesor_list.html"
    )


@login_required
def profesor_form(request):
    if request.method == 'POST':
        profesor_form = ProfesorForm(request.POST)
        if profesor_form.is_valid():
            data = profesor_form.cleaned_data

            # Una pequeña muestra de procesos de unit test
            KEY_LEN = 20
            char_list = [
                random.choice((string.ascii_letters + string.digits))
                for _ in range(KEY_LEN)
            ]
            mock_name = ''.join(char_list)
            print(f'----------> Prueba con: {mock_name}')

            profesor = Profesor(
                name=mock_name,
                last_name=data['last_name'],
                email=data['email'],
                profession=data['profession'],
            )
            profesor.save()

            profesors = Profesor.objects.all()
            context_dict = {
                'profesors': profesors
            }
            return render(
                request=request,
                context=context_dict,
                template_name="profesor/profesor_list.html"
            )

    profesor_form = ProfesorForm(request.POST)
    context_dict = {
        'profesor_form': profesor_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='profesor/profesor_form.html'
    )


@login_required
def update_profesor(request, pk: int):
    profesor = Profesor.objects.get(pk=pk)

    if request.method == 'POST':
        profesor_form = ProfesorForm(request.POST)
        if profesor_form.is_valid():
            data = profesor_form.cleaned_data
            profesor.name = data['name']
            profesor.last_name = data['last_name']
            profesor.email = data['email']
            profesor.profession = data['profession']
            profesor.save()

            profesors = Profesor.objects.all()
            context_dict = {
                'profesors': profesors
            }
            return render(
                request=request,
                context=context_dict,
                template_name="profesor/profesor_list.html"
            )

    profesor_form = ProfesorForm(model_to_dict(profesor))
    context_dict = {
        'profesor': profesor,
        'profesor_form': profesor_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='profesor/profesor_form.html'
    )


@login_required
def delete_profesor(request, pk: int):
    profesor = Profesor.objects.get(pk=pk)
    if request.method == 'POST':
        profesor.delete()

        profesors = Profesor.objects.all()
        context_dict = {
            'profesors': profesors
        }
        return render(
            request=request,
            context=context_dict,
            template_name="profesor/profesor_list.html"
        )

    context_dict = {
        'profesor': profesor,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='profesor/profesor_confirm_delete.html'
    )
