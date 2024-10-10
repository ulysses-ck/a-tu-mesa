from django.db import models

class Rol (models.Model):
    nombre = models.CharField(max_lenght=25)

    def __str__(self):
        return self.nombre