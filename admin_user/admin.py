from django.contrib import admin
from .models import Usuario,Eventos,Cursos,Actividad,Mensaje,Asistente

class UsuarioDet(admin.ModelAdmin):
    list_display = ("nombre","correo","creado")
    search_fields = ("nombre", )
    fields = ["nombre","correo","password","creado"]
    readonly_fields = ('creado', )

class AsistenteInline(admin.TabularInline):
    model = Asistente
    extra = 1

class EventoDet(admin.ModelAdmin):
    inlines = [AsistenteInline, ]
    list_display = ("nombre","fechayhora","direccion")
    search_fields = ("nombre", )
    fields = ["nombre","descripcion","fechayhora","direccion","imagen"]





class CursoDet(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre", )
    fields = ["nombre","descripcion", "precio","archivo"]

class MensajeDet(admin.ModelAdmin):
    readonly_fields = ('creado', )

admin.site.register(Usuario,UsuarioDet)
admin.site.register(Eventos,EventoDet)
admin.site.register(Cursos,CursoDet)
admin.site.register(Actividad)
admin.site.register(Mensaje,MensajeDet)


