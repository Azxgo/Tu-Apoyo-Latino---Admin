from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Usuario(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=100)
    correo = models.EmailField(unique=True, max_length=200)
    creado = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'nombre'
    REQUIRED_FIELDS = ['correo']

    class Meta:
            verbose_name="Usuario"
            verbose_name_plural="Usuarios"
            ordering=["nombre","correo","password","creado"]

    def __str__(self):
        return self.nombre

class Actividad():
    pass

class Eventos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True,max_length=100,verbose_name='nombre')
    descripcion = models.TextField(blank=True)
    fechayhora = models.DateTimeField(null=False)
    direccion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to="projects",verbose_name="imagen")
    asistentes = models.ManyToManyField("Usuario")

    class Meta:
        verbose_name="Evento"
        verbose_name_plural="Eventos"

    def __str__(self):
        return self.nombre
        
class Cursos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True,max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.IntegerField(blank=False,null=False)
    archivo = models.FileField(upload_to="uploads",verbose_name="archivo")

    class Meta:
        verbose_name="Curso"
        verbose_name_plural="Cursos"

    def __str__(self):
        return self.nombre
