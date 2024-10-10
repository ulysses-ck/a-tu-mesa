from django.db import models

# Create your models here.
class Mesa (models.Model):
    id_comanda = models.ForeignKey("comanda", on_delete=models.CASCADE)
    nro_mesa = models.IntegerField()