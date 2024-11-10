from django.views.generic import TemplateView
from .models import Producto

class ProductoView(TemplateView):
    template_name = 'producto.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Producto.objects.all()
        return context