from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is customer', default=False)
    is_employee = models.BooleanField('Is employee', default=False)

class Unidad(models.Model):
    Nombre_U = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre_U

class Rol(models.Model):
    Nombre_R = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre_R

class Jerarquia(models.Model):
    Nombre_J = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre_J

class Usuario(models.Model):
    Nombre = models.CharField(max_length=50)
    Contraseña = models.CharField(max_length=50)
    Rol = models.ForeignKey(Rol, on_delete=models.PROTECT)
    Unidad = models.ForeignKey(Unidad, on_delete=models.PROTECT)
    Jerarquia = models.ForeignKey(Jerarquia, on_delete=models.PROTECT)

    def __str__(self):
        return self.Nombre

class Tarea(models.Model):
    Nombre_Tarea = models.CharField(max_length=50)
    Responsable = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    Fecha_desde = models.DateField()
    Fecha_hasta = models.DateField()
    Descripcion = models.TextField()

    def __str__(self):
        return self.Nombre_Tarea

class TareaSub(models.Model):
    Nombre_TareaS = models.CharField(max_length=50)
    ResponsableS = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    TareaMadreS = models.ForeignKey(Tarea, on_delete=models.PROTECT)
    Fecha_desdeS = models.DateField()
    Fecha_hastaS = models.DateField()
    DescripcionS = models.TextField()

    def __str__(self):
        return self.Nombre_TareaS