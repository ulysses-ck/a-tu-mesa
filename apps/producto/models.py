from django.db import models

# Create your models here.
class Producto (models.Model):
	precio = models.FloatField()
	nombre = models.CharField(max_length=50)
	tipo = models.ForeignKey("tipoProducto.TipoProducto", on_delete=models.CASCADE)
	imagen = models.ImageField(upload_to='productos', null=True, blank=True)
	
	def __str__(self):
		return self.nombre

class TipoProducto (models.Model):
	nombre = models.CharField(max_length=50)