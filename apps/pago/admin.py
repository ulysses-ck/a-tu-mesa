from django.contrib import admin
from apps.pago.models import Pago, FormaDePago

# Register your models here.


@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('nro_autorizacion', 'fecha', 'pagador', 'forma_de_pago')

@admin.register(FormaDePago)
class FormaDePagoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

