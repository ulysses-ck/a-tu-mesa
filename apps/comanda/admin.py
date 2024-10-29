from django.contrib import admin

# Register your models here.
from apps.comanda.models import Comanda

@admin.register(Comanda)
class ComandaAdmin(admin.ModelAdmin):
	list_display = (
		'producto',
		'cantidad',
		'estado',
		'tipo_de_pedido',
		'ticket',
		'mesa',
		'fecha'
	)

