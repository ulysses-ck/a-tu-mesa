from django.views.generic import TemplateView
from .models import Comanda

class ComandasView(TemplateView):
    name = 'comanda'
    template_name = 'comanda.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comanda'] = Comanda.objects.all()
        return context
