from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

#Create your models here.

class TipoContrato(models.Model):
    nombre_tipocontrato = models.CharField(max_length=55, null=False, blank=False)
    def __str__(self):
        return self.nombre_tipocontrato

class Cargo(models.Model):
    nombre_cargo = models.CharField(max_length=55, null=False, blank=False)
    def __str__(self):
        return self.nombre_cargo

class Seccion(models.Model):
    nombre_seccion = models.CharField(max_length=55, null=False, blank=False)
    def __str__(self):
        return self.nombre_seccion

class Area(models.Model):
    nombre_area = models.CharField(max_length=55, null=False, blank=False)
    def __str__(self):
        return self.nombre_area

class Empresa(models.Model):
    nombre_empresa = models.CharField(max_length=55, null=False, blank=False)
    def __str__(self):
        return self.nombre_empresa


class Usuario(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.usuario.username
    
@receiver(post_save, sender=User)
def crear_usuario(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_usuario(sender, instance, **kwargs):
    instance.usuario.save()