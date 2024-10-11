from django.db import models

# Create your models here.
class TipoProducto(models.Model):
    nombre = models.CharField(max_length=25)
    
    def _str_(self):
        return self.nombre
