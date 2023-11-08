from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Usuario(AbstractBaseUser):
    nombre = models.CharField(unique=True, max_length=100)
    correo = models.EmailField(unique=True, max_length=254)
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

class Eventos():
    pass

class Cursos():
    pass
