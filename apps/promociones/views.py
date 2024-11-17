from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .models import Promociones

class PromocionesView(TemplateView):
    name = 'promociones'
    template_name = 'promociones.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['promociones'] = Promociones.objects.all()
        return context

class CreatePromocionesView(CreateView):
    model = Promociones
    fields = [
        'descuento',
        'descripcion',
        'condiciones',
    ]
    template_name = 'promociones_create.html'
    success_url = '/promociones'

class UpdatePromocionesView(UpdateView):
    model = Promociones
    fields = [
        'descuento',
        'descripcion',
        'condiciones',
    ]
    template_name = 'promociones_update.html'
    success_url = '/promociones'

class DeletePromocionesView(DeleteView):
    model = Promociones
    template_name = 'promociones_delete.html'
    success_url = '/promociones'

