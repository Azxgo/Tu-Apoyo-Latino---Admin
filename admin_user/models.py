from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User



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

    def __str__(self):
        return self.nombre

class Eventos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True,max_length=100,verbose_name='Nombre')
    descripcion = models.TextField(blank=True)
    fechayhora = models.DateTimeField(null=False,verbose_name='Fecha y Hora')
    direccion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to="projects",verbose_name="Imagen")
    asistentes = models.ManyToManyField(Usuario,through='Asistente')
    
    class Meta:
        verbose_name="Evento"
        verbose_name_plural="Eventos"

    def __str__(self):
        return self.nombre

class Asistente(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    evento = models.ForeignKey(Eventos, on_delete=models.CASCADE)


class Actividad(models.Model):
    sender = models.ForeignKey(Usuario,related_name='Usuario',on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)
    target_ct = models.ForeignKey(ContentType, blank=True, null=True,
    related_name='target_obj', on_delete=models.CASCADE)
    target_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey('target_ct', 'target_id')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.pk 
  
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

class Mensaje(models.Model):
    id = models.AutoField(primary_key=True)
    remitente = models.ForeignKey(User,on_delete=models.CASCADE)
    asunto = models.CharField(max_length=200)
    mensaje = models.TextField(blank=False)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Mensaje"
        verbose_name_plural="Mensajes"
