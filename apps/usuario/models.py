from django.db import models

# Create your models here.
class Usuario (models.Model):
    persona = models.OneToOneField("persona.Persona", on_delete=models.CASCADE)
    contraseña = models.CharField(max_length=25)

