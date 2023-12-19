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
    trabajadores = Trabajador.objects.all()
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


def ingresoDatosTrabajador(request):
    if request.method == 'POST':
        form = TrabajadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vistaAdmin')  # Reemplaza con la URL deseada
    else:
        form = TrabajadorForm()
    return render(request, 'crudUsuarios/datosTrabajador.html', {'form': form})



def crearHorario(request):
    # horario = Horario.objects.all().order_by('dia', 'hora_inicio')
    # return render(request, 'horariosTrabajadores/horario.html', {'horario': horario})
    pass

def ingresarArchivos(request):
    return render(request, 'ingresarArchivos.html')

def listarSolicitudes(request):
    return render(request, 'listarSolicitudes.html')