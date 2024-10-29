from django.db import models

# Create your models here.
class Comanda (models.Model):
		producto = models.ForeignKey("producto.Producto", on_delete=models.CASCADE)
		cantidad = models.IntegerField()
		estado = models.ForeignKey("estado.Estado", on_delete=models.CASCADE)
		tipo_de_pedido = models.ForeignKey("tipoDePedido.TipoDePedido", on_delete=models.CASCADE)
		ticket = models.ForeignKey("ticket.Ticket", on_delete=models.CASCADE, null=True, blank=True)
		mesa = models.ForeignKey("mesa.Mesa", on_delete=models.CASCADE)
		fecha = models.DateTimeField()