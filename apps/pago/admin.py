from django.contrib import admin
from apps.pago.models import Pago

# Register your models here.


@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('nro_autorizacion', 'fecha', 'pagador', 'forma_de_pago')
