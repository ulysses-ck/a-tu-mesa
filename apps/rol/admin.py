from django.contrib import admin
from apps.rol.models import Rol

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
