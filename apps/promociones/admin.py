from django.contrib import admin
from apps.promociones.models import Promociones, Condiciones
# Register your models here.
@admin.register(Promociones)
class PromocionesAdmin(admin.ModelAdmin):
    list_display = ('descuento', 'descripcion', 'condiciones')

@admin.register(Condiciones)
class CondicionesAdmin(admin.ModelAdmin):
    list_display = ('inicio', 'expira', 'producto')
