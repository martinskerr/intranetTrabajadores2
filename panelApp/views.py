from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from gestorUsers.forms import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from gestorUsers.models import *
from gestorUsers.forms import *
from django.contrib import messages


# Create your views here.

def index(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('post_login_redirect')
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

# Vista de redirección post-login
@login_required
def post_login_redirect(request):
    if request.user.is_superuser:
        return redirect('vistaAdmin')
    else:
        return redirect('vistaUser')

# Vista para el usuario normal
@login_required
def home_user(request):
    # Lógica específica para la página de inicio del usuario
    return render(request, 'homeUser.html')

# Vista para el administrador
@login_required
def home_admin(request):
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

# Vista para cerrar sesión
def logout_view(request):
    logout(request)
    return redirect('index')  # Redirige a la vista de inicio de sesión


def ingresoDatosTrabajador(request):
    if request.method == 'POST':
        form = TrabajadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vistaAdmin')  # Reemplaza con la URL deseada
    else:
        form = TrabajadorForm()
    return render(request, 'crudUsuarios/datosTrabajador.html', {'form': form})

def actualizar_trabajador(request, id):
    trabajador = get_object_or_404(Trabajador, id=id)
    if request.method == 'POST':
        form = TrabajadorForm(request.POST, instance=trabajador)
        if form.is_valid():
            form.save()
            return redirect('vistaAdmin')  # Reemplaza con la URL deseada
    else:
        form = TrabajadorForm(instance=trabajador)
    return render(request, 'crudUsuarios/actualizarUser.html', {'form': form})


def eliminar_trabajador(request, id):
    trabajador = get_object_or_404(Trabajador, id=id)
    trabajador.delete()
    return redirect('vistaAdmin') 


def crearHorario(request):
    # horario = Horario.objects.all().order_by('dia', 'hora_inicio')
    # return render(request, 'horariosTrabajadores/horario.html', {'horario': horario})
    pass

def ingresarArchivos(request):
    return render(request, 'ingresarArchivos.html')

def listarSolicitudes(request):
    return render(request, 'listarSolicitudes.html')