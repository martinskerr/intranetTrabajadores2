from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from gestorUsers.forms import *
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from gestorUsers.models import *
from gestorUsers.forms import *


# Create your views here.

def panel(request):
    trabajadores = Usuario.objects.all()
    data = {
        'usuarios': trabajadores,
        'title': 'Panel de Administración',
        'nombre_admin': 'Martin Lopez',
        'sucursal_admin': 'Inacap 2023 Taller de soluciones',
        'tarea_1': 'Revisar solicitudes de vacaciones',
        'tarea_2': 'Revisar solicitudes de permisos',
        'tarea_3': 'Revisar solicitudes de licencias medicas',
        'tarea_4': 'Revisar solicitudes de horas extras',
    }
    return render(request, 'homeAdmin.html', data)

def index(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('vistaAdmin')  
            else:
                pass  

    return render(request, 'registration/login.html', {'form': form})


def eliminarUsuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario.delete()
    return redirect('listarUsers')


def modificarUsuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    data = {
        'form': SignUpForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario = SignUpForm(data=request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado correctamente"
            data['form'] = formulario
    return render(request, 'crudUsuarios/modificarUsuario.html', data)


