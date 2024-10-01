from django.db import models

# Create your models here.
class Factura(models.Model):
	pago = models.FloatField()
	id_ticket = models.ForeignKey("ticket.Ticket", on_delete=models.CASCADE)