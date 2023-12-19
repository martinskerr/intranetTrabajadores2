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
    

class Trabajador(models.Model):
    rut_trabajador = models.CharField(max_length=12, null=False, blank=False)
    nombre_trabajador = models.CharField(max_length=55, null=False, blank=False)
    apellido_trabajador = models.CharField(max_length=55, null=False, blank=False)
    fecha_nacimiento = models.DateField(null=False, blank=False)
    telefono = models.CharField(max_length=55, null=False, blank=False)
    direccion = models.CharField(max_length=55, null=False, blank=False)
    fecha_inicio_contrato = models.DateField(null=False, blank=False)
    fecha_termino_contrato = models.DateField(null=False, blank=False)
    tipo_contrato = models.ForeignKey(TipoContrato, null=False, blank=False, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, null=False, blank=False, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, null=False, blank=False, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, null=False, blank=False, on_delete=models.CASCADE)
    usuario = models.OneToOneField(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_trabajador
    
class Solicitudes(models.Model):
    nombre_solicitud = models.CharField(max_length=55, null=False, blank=False)
    descripcion_solicitud = models.TextField(max_length=500, blank=True)
    fecha_inicio = models.DateField(null=False, blank=False)
    fecha_termino = models.DateField(null=False, blank=False)
    trabajador = models.ForeignKey('Trabajador', null=False, blank=False, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_solicitud    

    

class TareaTrabajador(models.Model):
    nombre_tarea = models.CharField(max_length=55, null=False, blank=False)
    descripcion_tarea = models.TextField(max_length=500, blank=True)
    fecha_inicio = models.DateField(null=False, blank=False)
    fecha_termino = models.DateField(null=False, blank=False)
    trabajador = models.ForeignKey('Trabajador', null=False, blank=False, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_tarea
    
@receiver(post_save, sender=User)
def crear_usuario(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_usuario(sender, instance, **kwargs):
    instance.usuario.save()