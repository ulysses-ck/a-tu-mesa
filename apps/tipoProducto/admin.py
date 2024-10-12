from django.contrib import admin

# Register your models here.
from apps.tipoProducto.models import TipoProducto

@admin.register(TipoProducto)
class TipoProductoAdmin(admin.ModelAdmin):
	list_display = ('nombre',)