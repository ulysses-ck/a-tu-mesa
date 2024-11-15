from django.db import models

# Create your models here.
class Persona (models.Model):
	nombre = models.CharField(max_length=50)
	rol = models.ForeignKey("rol.Rol", on_delete=models.CASCADE)
	correo = models.EmailField(max_length=50)
	telefono = models.CharField(max_length=10)
	documento = models.CharField(max_length=10)

	def __str__(self):
		return f"{self.nombre} - {self.rol.nombre}"