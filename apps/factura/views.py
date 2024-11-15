from django.views.generic import TemplateView

# Create your views here.
class FacturaView(TemplateView):
    name = 'facturas'
    template_name = 'facturas.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context