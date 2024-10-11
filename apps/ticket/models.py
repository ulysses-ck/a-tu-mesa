from django.db import models

class Ticket (models.Model):
	id_promocion = models.ManyToManyField("promociones.Promociones")
	fecha = models.DateTimeField()
	notas = models.CharField(max_length=120)