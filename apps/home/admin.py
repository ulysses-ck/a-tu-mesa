from django.contrib import admin

from apps.home.models import Home

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('banner', 'botonMenu', 'botonReservation', 'botonSeguimientoDePedido')
    
