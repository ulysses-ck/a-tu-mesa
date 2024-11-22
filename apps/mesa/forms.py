from django import forms

from apps.ticket.models import Ticket
from apps.promociones.models import Promociones
from apps.comanda.models import Comanda
class TicketForm(forms.ModelForm):
    promocion = forms.ModelChoiceField(
        queryset=Promociones.objects.all(),
        empty_label="Seleccione una promocion",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    

    class Meta:
        model = Ticket
        fields = ['fecha', 'notas']




class ComandaForm(forms.ModelForm):
    class Meta:
        model = Comanda
        fields = ['producto', 'cantidad', 'tipo_de_pedido', 'estado', 'fecha']