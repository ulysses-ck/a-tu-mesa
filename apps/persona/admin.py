from django.contrib import admin
from apps.persona.models import Persona


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'id_rol', 'correo', 'telefono', 'documento')
