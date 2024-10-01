from django.db import models

# Create your models here.
class Promociones (models.Model):
		descuento = models.FloatField()
		descripcion = models.CharField(max_length=50)