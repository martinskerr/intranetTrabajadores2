from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .models import *

# Create your views here.


def signUp(request):
    form = SignUpForm
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vistaAdmin')
        

    return render(request, 'crudUsuarios/createUser.html', {'form': form})

@login_required
def vistaAdmin(request):
    if request.user.is_superuser:
        users = Trabajador.objects.all()
        data = {
                'usuarios': users,
                'title': 'Panel de Administración',
                'nombre_admin': 'Martin Lopez',
                'sucursal_admin': 'Inacap 2023 Taller de soluciones',
                'tarea_1': 'Revisar solicitudes de vacaciones',
                'tarea_2': 'Revisar solicitudes de permisos',
                'tarea_3': 'Revisar solicitudes de licencias medicas',
                'tarea_4': 'Revisar solicitudes de horas extras',
            }
        return render(request, 'homeAdmin.html', data)
    else:
        return render(request, 'homeUser.html')

def viewUsers(request):
    users = Trabajador.objects.all()
    data = {
         'usuarios': users
    }
    return render(request, 'crudUsuarios/listUser.html', data)

