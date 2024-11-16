from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .models import Producto

class ProductoView(TemplateView):
    name = 'producto'
    template_name = 'menu.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Producto.objects.all()
        return context
    
class ProductoAdminView(TemplateView):
    name = 'producto_admin'
    template_name = 'producto_read.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Producto.objects.all()
        return context

class CreateProductoView(CreateView):
    model = Producto
    fields = [
        'precio',
        'nombre',
        'tipo',
        'imagen',
    ]
    template_name = 'producto_create.html'
    success_url = '/productos'

class UpdateProductoView(UpdateView):
    model = Producto
    fields = [
        'precio',
        'nombre',
        'tipo',
        'imagen',
    ]
    template_name = 'producto_update.html'
    success_url = '/productos'

class DeleteProductoView(DeleteView):
    model = Producto
    template_name = 'producto_delete.html'
    success_url = '/productos'