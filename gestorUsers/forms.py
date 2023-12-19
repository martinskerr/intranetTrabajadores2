from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=55, required=True)
    first_name = forms.CharField(max_length=55, required=True)
    last_name = forms.CharField(max_length=55, required=True)
    email = forms.EmailField(max_length=100, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    username.widget.attrs.update({'class': 'form-control'})
    first_name.widget.attrs.update({'class': 'form-control'})
    last_name.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update({'class': 'form-control'})
    password1.widget.attrs.update({'class': 'form-control'})
    password2.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2')
        
class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = ['rut_trabajador', 'nombre_trabajador', 'apellido_trabajador', 
                  'fecha_nacimiento', 'telefono', 'direccion', 
                  'fecha_inicio_contrato', 'fecha_termino_contrato', 
                  'tipo_contrato', 'cargo', 'area', 'empresa', 'usuario']
        widgets = {
            'rut_trabajador': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_trabajador': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_trabajador': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_inicio_contrato': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_termino_contrato': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'tipo_contrato': forms.Select(attrs={'class': 'form-control'}),
            'cargo': forms.Select(attrs={'class': 'form-control'}),
            'area': forms.Select(attrs={'class': 'form-control'}),
            'empresa': forms.Select(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
        }