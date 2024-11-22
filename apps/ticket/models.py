from django.db import models
from apps.mesa.models import Mesa

class Ticket (models.Model):
	promocion = models.ForeignKey("promociones.Promociones", on_delete=models.CASCADE,  null=True, blank=True)
	mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, null=True, blank=True)
	fecha = models.DateTimeField()
	estado = models.CharField(max_length=10, choices=[('Abierto', 'Abierto'), ('Cerrado', 'Cerrado')], default='Abierto')
	notas = models.CharField(max_length=120)

	def __str__(self):
		if self.mesa:
			return f"Ticket {self.id} - Mesa {self.mesa.nro_mesa} ({self.estado})"
		else:
			return f"Ticket {self.id} - Sin mesa ({self.estado})"