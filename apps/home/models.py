from django.db import models

class Home(models.Model):
    banner = models.ImageField(upload_to="home/")
    botonMenu = models.ImageField(upload_to="home/")
    botonReservation = models.ImageField(upload_to="home/")
    botonSeguimientoDePedido = models.ImageField(upload_to="home/")
    