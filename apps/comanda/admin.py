from django.contrib import admin

# Register your models here.
from apps.comanda.models import Comanda

@admin.register(Comanda)
class ComandaAdmin(admin.ModelAdmin):
	list_display = (
		'id_producto',
		'cantidad',
		'id_estado',
		'id_tipo_de_pedido',
		'id_ticket',
		'id_mesa',
		'fecha'
	)

