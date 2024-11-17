from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView

from .models import TipoDePedido

class TipoDePedidoView(TemplateView):
    name = 'TipoDePedido'
    template_name = 'tipo_pedido_read.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipoDePedidos'] = TipoDePedido.objects.all()
        return context

class CreateTipoDePedidoView(CreateView):
    model = TipoDePedido
    fields = ['nombre']
    template_name = 'tipo_pedido_create.html'
    success_url = '/tipoDePedido'

class UpdateTipoDePedidoView(UpdateView):
    model = TipoDePedido
    fields = ['nombre']
    template_name = 'tipo_pedido_update.html'
    success_url = '/tipoDePedido'

class DeleteTipoDePedidoView(DeleteView):
    model = TipoDePedido
    template_name = 'tipo_pedido_delete.html'
    success_url = '/tipoDePedido'