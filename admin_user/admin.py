from django.contrib import admin
from .models import Usuario, Eventos, Cursos

class UsuarioDet(admin.ModelAdmin):
    fields = ["nombre","correo","password","creado"]
    readonly_fields = ('creado', )

class EventoDet(admin.ModelAdmin):
    fields = ["nombre","descripcion","fechayhora","direccion","imagen"]

class CursoDet(admin.ModelAdmin):
    fields = ["nombre","descripcion", "precio","archivo"]

admin.site.register(Usuario,UsuarioDet)
admin.site.register(Eventos,EventoDet)
admin.site.register(Cursos,CursoDet)


