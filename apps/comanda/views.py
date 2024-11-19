from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .models import Comanda
from django.contrib.auth.mixins import LoginRequiredMixin

class ComandasView(LoginRequiredMixin ,TemplateView):
    login_url = '/login/' 
    name = 'comanda'
    template_name = 'comanda_read.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comandas'] = Comanda.objects.all()
        return context

class CreateComandaView(LoginRequiredMixin, CreateView):
    model = Comanda
    fields = [
        'producto',
        'cantidad',
        'estado',
        'tipo_de_pedido',
        'ticket',
        'mesa',
        'fecha'
    ]
    template_name = 'comanda_create.html'
    success_url = '/comanda'

class UpdateComandaView(LoginRequiredMixin, UpdateView):
    model = Comanda
    fields = [
        'producto',
        'cantidad',
        'estado',
        'tipo_de_pedido',
        'ticket',
        'mesa',
        'fecha'
    ]
    template_name = 'comanda_update.html'
    success_url = '/comanda'

class DeleteComandaView(LoginRequiredMixin, DeleteView):
    model = Comanda
    template_name = 'comanda_delete.html'
    success_url = '/comanda'