from django.contrib import admin

# Register your models here.
from apps.factura.models import Factura

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
	list_display = ('pago', 'ticket')
