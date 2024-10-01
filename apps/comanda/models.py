from django.db import models

# Create your models here.
class Comanda (models.Model):
		id_producto = models.ForeignKey("producto", on_delete=models.CASCADE)
		cantidad = models.IntegerField()
		id_estado = models.ForeignKey("Estado", on_delete=models.CASCADE)
		
class Estado (models.Model):
		nombre = models.CharField(max_length=50)