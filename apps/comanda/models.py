from django.db import models

# Create your models here.
class Comanda (models.Model):
		id_producto = models.ForeignKey("producto.Producto", on_delete=models.CASCADE)
		cantidad = models.IntegerField()
		id_estado = models.ForeignKey("estado.Estado", on_delete=models.CASCADE)
		id_tipo_de_pedido = models.ForeignKey("tipoDePedido.TipoDePedido", on_delete=models.CASCADE)
		id_ticket = models.ForeignKey("ticket.Ticket", on_delete=models.CASCADE)
		fecha = models.DateTimeField()