from django.db import models

# Create your models here.
class Usuario (models.Model):
    persona = models.ForeignKey("persona.Persona", on_delete=models.CASCADE)
    contraseña = models.CharField(max_lenght=25)
    
