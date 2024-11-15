from django.db import models

# Create your models here.
class Mesa (models.Model):
    nro_mesa = models.IntegerField()

    def __str__(self):
        return f"Mesa {self.nro_mesa}"