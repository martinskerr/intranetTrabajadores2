"""
URL configuration for intranetTrabajadores2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from gestorUsers.views import *
from panelApp.views import * 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name="index"),
    path('register/',signUp, name="signUp"),
    path('users/',viewUsers, name='viewUsers'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('vistaAdmin/', vistaAdmin, name='vistaAdmin'),
    path('listarUsers/', viewUsers, name='listarUsers'),
    path('modificarUsuario/<id>/', modificarUsuario, name='modificarUsuario'),
    path('eliminarUsuario/<id>/', eliminarUsuario, name='eliminarUsuario'),
    path('crearHorario/', crearHorario, name='crearHorario'),
    path('ingresarArchivos/', ingresarArchivos, name='ingresarArchivos'),
    path('listarSolicitudes', listarSolicitudes, name='listarSolicitudes'),
    path('ingresoDatosTrabajador/', ingresoDatosTrabajador, name='ingresoDatosTrabajador')
]
