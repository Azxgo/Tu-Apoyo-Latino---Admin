from django.contrib import admin
from .models import Usuario

class UsuarioDet(admin.ModelAdmin):
    fields = ["nombre","correo","password","creado"]
    readonly_fields = ('creado', )


admin.site.register(Usuario,UsuarioDet)
