from django.db import models

# Create your models here.
class Estado (models.Model):
    nombre = models.CharField(max_lenght=25)

    def __str__(self):
        return self.nombre