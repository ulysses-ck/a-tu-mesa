from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Persona (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="persona",  null=True, blank=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50, null=True, blank=True)
    rol = models.ForeignKey("rol.Rol", on_delete=models.CASCADE, null=True, blank=True)
    correo = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=10)
    documento = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"