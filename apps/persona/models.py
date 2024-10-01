from django.db import models

# Create your models here.
class Persona (models.Model):
	nombre = models.CharField(max_length=50)
	id_rol = models.ForeignKey("rol.Rol", on_delete=models.CASCADE)
	correo = models.EmailField(max_length=50)
	telefono = models.CharField(max_length=10)
	documento = models.CharField(max_length=10)