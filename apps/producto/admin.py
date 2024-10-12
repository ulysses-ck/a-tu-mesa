from django.contrib import admin
from apps.producto.models import Producto, TipoProducto

# Register your models here.
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'tipo',)

@admin.register(TipoProducto)
class TipoProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
