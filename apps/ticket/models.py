from django.db import models

class Ticket (models.Model):
	id_promocion = models.ForeignKey("promociones.Promociones", on_delete=models.CASCADE)
	fecha = models.DateTimeField()
	notas = models.CharField(max_length=120)