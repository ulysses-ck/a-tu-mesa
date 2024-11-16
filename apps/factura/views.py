from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .models import Factura
# Create your views here.
class FacturaView(TemplateView):
    name = 'facturas'
    template_name = 'facturas.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['facturas'] = Factura.objects.all()
        return context

class CreateFacturaView(CreateView):
    model = Factura
    fields = [
        'pago',
        'ticket',
    ]
    template_name = 'factura_create.html'
    success_url = '/factura'

class UpdateFacturaView(UpdateView):
    model = Factura
    fields = [
        'pago',
        'ticket',
    ]
    template_name = 'factura_update.html'
    success_url = '/factura'

class DeleteFacturaView(DeleteView):
    model = Factura
    template_name = 'factura_delete.html'
    success_url = '/factura'   