from django.db import models

class Home(models.Model):
    banner = models.CharField(max_length=300)
    botonMenu = models.CharField(max_length=300)
    botonReservation = models.CharField(max_length=300)
    botonSeguimientoDePedido = models.CharField(max_length=300)
    