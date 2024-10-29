from django.db import models

class Ticket (models.Model):
	promocion = models.ForeignKey("promociones.Promociones", on_delete=models.CASCADE)
	fecha = models.DateTimeField()
	notas = models.CharField(max_length=120)