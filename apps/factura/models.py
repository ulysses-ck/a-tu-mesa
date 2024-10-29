from django.db import models

# Create your models here.
class Factura(models.Model):
	pago = models.ForeignKey("pago.Pago", on_delete=models.CASCADE)
	ticket = models.ForeignKey("ticket.Ticket", on_delete=models.CASCADE)