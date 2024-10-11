from django.db import models

# Create your models here.
class Producto (models.Model):
	precio = models.FloatField()
	nombre = models.CharField(max_length=50)
	tipo = models.ForeignKey("tipoProducto.TipoProducto", on_delete=models.CASCADE)
	
class TipoProducto (models.Model):
	nombre = models.CharField(max_length=50)