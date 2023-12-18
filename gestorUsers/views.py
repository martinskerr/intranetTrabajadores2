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
        return render(request, 'homeAdmin.html')
    else:
        return render(request, 'homeUser.html')

def viewUsers(request):
    users = Usuario.objects.all()
    data = {
        'usuarios': users
    }
    return render(request, 'crudUsuarios/listUser.html', data)