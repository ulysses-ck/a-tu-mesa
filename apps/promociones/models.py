from django.db import models

# Create your models here.
class Promociones (models.Model):
		descuento = models.FloatField()
		descripcion = models.CharField(max_length=50)
		condiciones = models.ForeignKey("Condiciones", on_delete=models.CASCADE)

		def __str__(self):
			return f"{self.descripcion} - {self.descuento}% de descuento"
		
class Condiciones (models.Model):
		inicio = models.DateTimeField()
		expira = models.DateTimeField()
		producto = models.ForeignKey("producto.Producto", on_delete=models.CASCADE)

		def __str__(self):
			return f"Condiciones para {self.producto.nombre} (Válido desde {self.inicio.strftime('%Y-%m-%d')} hasta {self.expira.strftime('%Y-%m-%d')})"
