from django.db import models

class Pago (models.Model):
	nro_autorizacion = models.IntegerField()
	fecha = models.DateTimeField()
	pagador = models.ForeignKey("persona.Persona", on_delete=models.CASCADE)
	id_forma_de_pago = models.ForeignKey("FormaDePago", on_delete=models.CASCADE)

class FormaDePago (models.Model):
	nombre = models.CharField(max_length=25)

	def __str__(self):
		return self.nombre
