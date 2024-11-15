from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Persona (models.Model):
<<<<<<< HEAD
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="persona",  null=True, blank=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50, null=True, blank=True)
    rol = models.ForeignKey("rol.Rol", on_delete=models.CASCADE, null=True, blank=True)
    correo = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=10)
    documento = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
=======
	nombre = models.CharField(max_length=50)
	rol = models.ForeignKey("rol.Rol", on_delete=models.CASCADE)
	correo = models.EmailField(max_length=50)
	telefono = models.CharField(max_length=10)
	documento = models.CharField(max_length=10)

	def __str__(self):
		return f"{self.nombre} - {self.rol.nombre}"
>>>>>>> 145a6bc0cb078dc4c3da26194150093b7a0c77be
