from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=55, required=True)
    first_name = forms.CharField(max_length=55, required=True)
    last_name = forms.CharField(max_length=55, required=True)
    email = forms.EmailField(max_length=100, required=True)
    tipocontrato = forms.ModelChoiceField(queryset=TipoContrato.objects.all())
    cargo = forms.ModelChoiceField(queryset=Cargo.objects.all())
    seccion = forms.ModelChoiceField(queryset=Seccion.objects.all())
    area = forms.ModelChoiceField(queryset=Area.objects.all())
    empresa = forms.ModelChoiceField(queryset=Empresa.objects.all())
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    username.widget.attrs.update({'class': 'form-control'})
    first_name.widget.attrs.update({'class': 'form-control'})
    last_name.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update({'class': 'form-control'})
    tipocontrato.widget.attrs.update({'class': 'form-control'})
    cargo.widget.attrs.update({'class': 'form-control'})
    seccion.widget.attrs.update({'class': 'form-control'})
    area.widget.attrs.update({'class': 'form-control'})
    empresa.widget.attrs.update({'class': 'form-control'})
    password1.widget.attrs.update({'class': 'form-control'})
    password2.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'tipocontrato',
                  'cargo',
                  'seccion',
                  'area',
                  'empresa',
                  'password1',
                  'password2')