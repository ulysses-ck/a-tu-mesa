from django.contrib import admin
from .models import TipoDePedido

@admin.register(TipoDePedido)
class TipoDePedidoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
